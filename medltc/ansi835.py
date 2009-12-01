import os
import sys
import string
import getopt
import traceback

import x12codes

from datetime import date
from datetime import time

def ccyymmdd2date(ccyymmdd):
    if len(ccyymmdd) != 8:
        raise ValueError("invalid ccyymmdd date string [%s]" % ccyymmdd)
    year = int(ccyymmdd[0:4])
    month = int(ccyymmdd[4:6])
    day = int(ccyymmdd[6:8])

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("invalid date")

    return date(year, month, day)

def yymmdd2date(yymmdd):
    if len(yymmdd) != 6:
        raise ValueError("invalid yymmdd date string - [%s]" % yymmdd)
    year = int(yymmdd[0:2]) + 2000
    month = int(yymmdd[2:4])
    day = int(yymmdd[4:6])

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("invalid date - %s" % yymmdd)

    return date(year, month, day)

def splitdate(datestring):
    if len(datestring) == 6:
        return yymmdd2date(datestring)
    elif len(datestring) == 8:
        return ccyymmdd2date(datestring)
    else:
        raise ValueError("invalid date string [%s]" % datestring)


def hhmm2time(hhmm):
    if len(hhmm) != 4:
        raise ValueError("invalid string")
    hour = int(hhmm[0:2])
    min = int(hhmm[2:4])
    if hour < 0 or hour > 23 or min < 0 or min > 60:
        raise ValueError("invalid time")

    return time(hour=hour, minute=min)

def find_835_files_in_dir (dirname, recursive = False):
    def checkdir (matched, dirname, names):
        for fname in names:
            try: 
                fullname = os.path.join(dirname, fname)
                if os.path.isfile(fullname):
                    obj = ansi835(fullname, quiet = True)
                    matched.append((fullname, obj))
            except FileFormatError:
                pass

    matched = []
    if recursive:
        os.path.walk(dirname, checkdir, matched)
    else:
        checkdir(matched, dirname, os.listdir(dirname))
    return matched

class FileFormatError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class ClaimService:
    def __init__(self, code):
        self.code = code
        self.reasons = []
        self.remark_codes = []
        self.rendering_provider = None
        self.rendering_provider_id_type = "0"
        self.date = None
        self.allowed = 0
        self.start_date = None
        self.end_date = None
        self.licn = ""
        self.location_code = ""
        self.late_deduction = 0

    def prettyStr(self):
        s = "service code: %s\r\n" % self.code
        s += "  date: %s - %s\r\n" % (self.start_date, self.end_date)
#        s += "  rendering provider id: %s\r\n" % self.rendering_provider
        s += "  allowed: %s\r\n" % self.allowed
        s += "  reasons: \r\n"
        for code, amount in self.reasons:
            s += "     $%s (%3s) %s\r\n" % \
                    (amount, code, x12codes.ClaimAdjustmentReasonToStr(code))
        if self.remark_codes:
            s += "   remarks: \r\n"
            for rc in self.remark_codes:
                code = rc.strip().upper()
                if code in x12codes.remarks:
                    desc = x12codes.remarks[code]
                else:
                    desc = "UNKNOWN"
                s += "    %s - %s\r\n" % (code, desc)

        return s

class ClaimStatus:
    def __init__(self, id, status, charge, paid, patient_responsible, \
            payer_ref_id):
        self.code = status.lstrip("0")
        self.id = id
        self.charge = charge
        self.paid = paid
        self.patient_responsible = patient_responsible
        self.payer_ref_id = payer_ref_id
        self.lname = ""
        self.fname = ""
        self.insured_id = None
        self.insured_id_type = None
        self.allowed = 0
        self.services = []
        self.date_received = None
        self.service_provider = ""
        self.service_provider_id_type = ""
        self.rendering_provider = ""
        self.rendering_provider_id_type = ""
        self.crossover_name = ""
        self.crossover_id_type = ""
        self.crossover_id = ""
        self.patient_id_type = ""
        self.patient_id = ""

    def prettyStr(self):
        s = "%s, %s\r\n" % ( self.lname, self.fname )
        s += "id: [%s]   status: [%s] %s\r\n" % \
                (self.id, self.code, x12codes.ClaimStatusToStr(self.code))
        s += "charges: %s  paid: %s  allowed: %s patient resp: %s\r\n" % \
                (self.charge, self.paid, self.allowed, self.patient_responsible)
        s += "payer assigned id: %s\r\n" % self.payer_ref_id
        for service in self.services:
            s += service.prettyStr()
        s += "\r\n"
        return s

class ansi835:
    def __init__ (self, filename, quiet = False):
        self.rawtext = {}
        self.claims = []
        self.segno = 0
        self.prod_date = None

        self.payer_name = ""
        self.payer_address = ""
        self.payer_city = ""
        self.payer_state = ""
        self.payer_zip = ""

        self.payee_name = ""
        self.payee_address = ""
        self.payee_city = ""
        self.payee_state = ""
        self.payee_zip = ""

        self.payer_transaction_id = ""

        self._quiet = quiet
        self._filename = filename

        try:
            self.f = file(filename, 'r')
        except IOError:
            if not self._quiet: print "error opening [%s]!" % filename
            return

        self.process()

        # XXX HACK to deal with medicare files that have more than one ISA/IEA
        # loop
        try:
            while True:
                self.process()
        except FileFormatError:
            pass

        self.f.close()
        self.f = None

    def process(self):
        # eat whitespace
        while True:
            c = self.f.read(1)
            if not c:
                raise FileFormatError("End of file reached before ISA header")
            if not c.isspace():
                break
        self.f.seek(-1, 1)

        self.readISA()

        gs = self.readSegment()
        self.rawtext["GS"] = string.join(gs, self.elem_sep)

        if gs[0] != "GS": raise FileFormatError("expected GS")

        while True:
            seg = self.readSegment()
            if seg[0] == "ST":
                self.processST( seg )
            elif seg[0] == "GE":
                ge = seg
                iea = self.readSegment(expect="IEA")
                self.rawtext["GE"] = string.join(ge, self.elem_sep)
                self.rawtext["IEA"] = string.join(ge, self.elem_sep)
                break
            else:
                raise FileFormatError("unexpected segment %s" % seg[0])

    def processST(self, st):
        # sanity checks
        if st[1] != "835":
            raise FileFormatError("Not an 835 file! ST[0] is '%s'" % st[0])

        # BPR always follows ST
        seg = self.readSegment( expect = "BPR" )
        self.rawtext["BPR"] = string.join(seg, self.elem_sep)
        # TODO do something with ST

        # TRN always follows BPR
        seg = self.readSegment( expect = "TRN") 
        if seg[1] != "1":
            raise FileFormatError("invalid TRN segment")
        self.payer_transaction_id = seg[2]
        self.rawtext["TRN"] = string.join(seg, self.elem_sep)
        # TODO do something with BPR

        cs = None

        n1mode = None

        curloop = 0

        while True:
            try:
                # ignore all segments until we get a CLP, which is really the
                # only thing we care about
                seg = self.scanSegments(("CLP","SE","NM1","CAS","REF","DTM",\
                        "SVC", "AMT", "N1", "N3", "N4", "PER", "LQ" ))

                if seg[0] == "CLP":
                    #           if cs is not None:
                    #               self.prettyStr += "%s\n" % cs.prettyStr()
                        #print cs.prettyStr()
                    seg_charge = 0
                    seg_paid = 0
                    seg_ptresp = 0
                    try: seg_charge = float(seg[3]) 
                    except ValueError: pass
                    try: seg_paid = float(seg[4]) 
                    except ValueError: pass
                    try: seg_ptresp = float(seg[5]) 
                    except ValueError: pass
                    cs = ClaimStatus(id=seg[1], status=seg[2], 
                            charge=seg_charge, paid=seg_paid, 
                            patient_responsible=seg_ptresp,
                            payer_ref_id=seg[7])
                    self.claims.append(cs)
                    curloop = 2100
                elif seg[0] == "NM1":
                    if seg[1] == "QC":
                        cs.lname = seg[3]
                        cs.fname = seg[4]
                        cs.patient_id_type = seg[8]
                        cs.patient_id = seg[9]
                    elif seg[1] == "IL":
                        cs.insured_id_type = seg[8]
                        cs.insured_id = seg[9]
                    elif seg[1] == "74":
                        pass
                        # XXX ignore corrected/insured info (loop 2100)
                    elif seg[1] == "82":
                        cs.service_provider = seg[9]
                        cs.service_provider_id_type = seg[8]
                    elif seg[1] == "TT":
                        cs.crossover_name = seg[3]
                        cs.crossover_id_type = seg[8]
                        cs.crossover_id = seg[9]
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                elif seg[0] == "CAS":
#                    car = ClaimAdjustmentReason( seg )
                    seg.pop(0)

                    cs.services[-1].reasons = []
                    while len(seg) > 0:
                        cs.services[-1].reasons.append((seg[1], float(seg[2])))
                        seg = seg[3:]

                elif seg[0] == "REF":
                    if seg[1] in [ "1A", "1B", "1C", "1D", "1G", "1H", "D3", \
                            "G2" ] and cs is not None:

                        if curloop == 2100:
                            cs.rendering_provider = seg[2]
                            cs.rendering_provider_id_type = seg[1]
                        elif curloop == 2110:
                            cs.services[-1].rendering_provider = seg[2]
                            cs.services[-1].rendering_provider_id_type = seg[1]
                    elif seg[1] == "ZZ" and cs is not None and \
                            len(cs.services) > 0:
                        # XXX this isn't in the specification, but BCBS
                        # arkansas seems to do it this way.
                        allowed_amt = float(seg[2])
                        cs.services[-1].allowed = allowed_amt
                        cs.allowed += allowed_amt
                    elif seg[1] == "6R":
                        cs.services[-1].licn = seg[2]
                    elif seg[1] == "LU":
                        cs.services[-1].location_code = seg[2]
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                elif seg[0] == "DTM":
                    if seg[1] == "150":
                        d = splitdate(seg[2])
                        cs.services[-1].start_date = d
                    elif seg[1] == "151":
                        d = splitdate(seg[2])
                        cs.services[-1].end_date = d
                    elif seg[1] == "472":
                        d = splitdate(seg[2])
                        cs.services[-1].start_date = d
                        cs.services[-1].end_date = d
                    elif seg[1] == "405":
                        d = splitdate(seg[2])
                        self.prod_date = d
                    elif seg[1] == "050" and cs.date_received is None:
                        d = splitdate(seg[2])
                        cs.date_received = d
                    else:
                        if not self._quiet: print "ignoring [%s]" % str(seg)

                elif seg[0] == "SVC":
                    # BCBS Arkansas sends us busted files, so try to code
                    # around it
                    if seg[1] == "HC":
                        # busted file
                        service_code = seg[2]
                    else:
                        subfields = seg[1].split(self.subfield_sep)
                        service_code = subfields[1]
                    cs.services.append( ClaimService( service_code ) )
                    cs.services[-1].rendering_provider = cs.rendering_provider
                    cs.services[-1].rendering_provider_id_type = \
                            cs.rendering_provider_id_type
                    curloop = 2110
                elif seg[0] == "AMT":
                    if seg[1] == "B6":
                        allowed_amt = float(seg[2])
                        cs.services[-1].allowed = allowed_amt
                        cs.allowed += allowed_amt
                    elif seg[1] == "KH":
                        cs.services[-1].late_deduction = float(seg[2])
                    else:
                        if not self._quiet: print "ignoring [%s]" % str(seg)
                elif seg[0] == "N1":
                    if seg[1] == "PR":
                        self.payer_name = seg[2]
                        n1mode = "PR"
                    elif seg[1] == "PE":
                        self.payee_name = seg[2]
                        n1mode = "PE"
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                elif seg[0] == "N3":
                    if n1mode == "PR":
                        self.payer_address = seg[1]
                    elif n1mode == "PE":
                        self.payee_address = seg[1]
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                elif seg[0] == "N4":
                    if n1mode == "PR":
                        self.payer_city = seg[1]
                        self.payer_state = seg[2]
                        self.payer_zip = seg[3]
                    elif n1mode == "PE":
                        self.payee_city = seg[1]
                        self.payee_state = seg[2]
                        self.payee_zip = seg[3]
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                        n4 = self.readSegment( expect="N4" )
                elif seg[0] == "PER":
                    if seg[1] == "CX":
                        pass
                    else:
                        if not self._quiet: print "ignoring %s" % str(seg)
                elif seg[0] == "LQ":
                    if seg[1] == "HE":
                        cs.services[-1].remark_codes.append(seg[2].strip().upper())
                else:
                    #                self.prettyStr += "%s\n" % cs.prettyStr()
                    return
            except Exception, e:
                if not self._quiet: 
                    print "file: %s" % self._filename
                    print "Error while processing segment"
                    print "%s" % seg
                    print "------"
                    traceback.print_exc()
                    print "-----"
                    print "%s appears to be a corrupted ANSI 835 file" % \
                            self._filename
                return


    def readISA(self):
        self.segno += 1
        f = self.f
        # check that the first three bytes read "ISA"
        rawisa = ""
        isa = f.read(3)
        rawisa += isa
        if( isa != "ISA" ):
            raise FileFormatError("ISA not found [%s]" % isa)

        # the first element separator defines the element separator to be used
        # throughout the entire interchange
        self.elem_sep = f.read(1)
        rawisa += self.elem_sep
        
        # read the ISA fields into an array
        self.isa = [ "ISA" ]
        # read in the next 15 fields all at once.  Field lengths are defined in
        # ANSI 835 spec
        for i in [ 2, 10, 2, 10, 2, 15, 2, 15, 6, 4, 1, 5, 9, 1, 1 ]:
            s = f.read(i)
            c = f.read(1)
            rawisa += s
            rawisa += c
            if c != self.elem_sep: 
                raise FileFormatError("element separator not found! %s" % c)
            self.isa.append(s)
        self.isa.append( f.read(1) )
        rawisa += self.isa[-1]

        self.senderqual = self.isa[3]
        self.senderid = self.isa[4]
        self.receiverqual = self.isa[5]
        self.receiverid = self.isa[6]
        self.date = splitdate(self.isa[9])
        self.time = hhmm2time(self.isa[10])
        self.production = (self.isa[15] == "P")
        self.subfield_sep = self.isa[16]
        self.segment_sep = self.f.read(1)
        rawisa += self.segment_sep
        self.rawtext["ISA"] = rawisa

    def scanSegments(self, expectList):
        """Repeatedly calls readSegment() and discards read segments until a
        segment matching one in expectList is found.  Obviously, this isn't a
        very good idea
        """
        while True:
            seg = self.readSegment()
            if seg[0] in expectList: return seg
            elif seg[0] not in ["MOA"]: 
                if not self._quiet: sys.stderr.write("ignoring %s\n" % seg)

    def readSegment(self, expect = None):
        """assumes that self.f is positioned on the beginning of a segment
        (i.e. right after a segment terminator).  Reads the entire segment, 
        and returns with self.f positioned at the beginning of the next
        segment.  Returns an array, one entry per segment element.  
        If expect is not None, then readSegment will check that the first 
        element is the same as expect, and raises a FileFormatError if 
        it isn't
        """
        seg = []
        self.segno += 1
        more = True
        while more:
            nf, more = self.nextField()
            seg.append(nf)
        if expect is not None and seg[0] != expect:
            raise FileFormatError("expected %s segment, got %s" % \
                    (expect, seg[0]))
        return seg

    def nextField(self):
        """
        assumes self.f is positioned at the beginning of an element, and
        reads that element.  returns with self.f positioned after either the
        next element separator or the next segment terminator.  returns a 
        tuple (field, more_in_segment).  more_in_segment is true if there are
        more fields in the segment to be read, and false if the segment 
        terminator has been read
        """
        assert self.elem_sep is not None
        field = ""
        c = ""
        while True:
            c = self.f.read(1)
            if len(c) != 1:
                raise FileFormatError("error reading element/segment separator")
            if c == self.elem_sep:
                return (field, True)
            elif c == self.segment_sep:
                return (field, False)
            field += c

__prov_id_map = {
    "0" : "", # XXX for nonexistant id type
    "1A" : "Blue Cross Provider Number",
    "1B" : "Blue Shield Provider Number",
    "1C" : "Medicare Provider Number", 
    "1D" : "Medicaid Provider Number", 
    "1G" : "Provider UPIN Number", 
    "1H" : "CHAMPUS Identification Number", 
    "D3" : "Boards of Pharmacy Number", 
    "G2" : "Provider Comercial Number",
    "BD" : "Blue Cross Provider Number",
    "BS" : "Blue Shield Provider Number",
    "FI" : "Federal Tax ID / SS#",
    "MC" : "Medicaid Provider Number",
    "PC" : "Provider Commercial Number",
    "SL" : "State License Number",
    "UP" : "UPIN",
    "XX" : "HCFA National Provider ID"
    }
def ProviderIDTypeToStr(code):
    return __prov_id_map[code]

def fname_zdrive_hack (fname):
    if os.path.exists(fname):
        return fname
    else:
        import zdrive
        bname = os.path.basename(fname)
        zname = os.path.join(zdrive.ANSI835_NEW_DIR, bname)
        if os.path.exists(zname):
            return zname
    return None

def usage():
    usage_str="""usage:  ansi835.py [options] <filename>

    filename should be an ASC X12N 835 (004010X091) file

    If no options are specified, then the file is parsed into human-readable 
    text.

OPTIONS:
    --breakonly        processes the file so that each segment is on its own
                       line, but individual segments are not parsed or
                       interpreted

    --extract-refid    outputs two columns of text, separated by a comma.  The
                       first column is the provider assigned claim id (LICN).
                       The second is the payer assigned claim id.

    -h, --help      shows this help text
"""
#    --setlog           outputs a comma delimited file for easy importing

    print usage_str

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    opts, args = getopt.getopt(sys.argv[1:], 'h', \
            [ 'breakonly', 'help', 'extract-refid', 'setlog' ])
    
    breakonly = False
    extract_refid = False
    setlog = False
    
    for o,a in opts:
        if o == '--breakonly': breakonly = True
        if o == '--extract-refid': extract_refid = True
        if o == '--setlog': setlog = True
        if o in ["-h", "--help"]:
            usage()
            sys.exit(0)

    try:
        # XXX HACK
        fname = fname_zdrive_hack(args[0])
        if fname is None:
            print "%s not found" % args[0]
            sys.exit(1)

        a = ansi835(fname)
    except FileFormatError:
        print "file does not appear to be an ANSI 835 file!"
        sys.exit(1)

    if breakonly:
        # don't want to print out our pretty representation.  Just replace the
        # segment separators with newlines.
        f = file(args[0], 'r')
        for line in f:
            result = string.replace(line, a.segment_sep, "\n")
            result = string.replace(result, a.elem_sep, "_")
            print result
        f.close()
    elif extract_refid:
        for claim in a.claims:
            print "%s, %s" % (claim.id, claim.payer_ref_id)
    elif setlog:
        for claim in a.claims:
            print claim.comma_separated_string()
    else:
        print "DATE: %s TIME: %s" % (a.date, a.time)
        print
        for v in a.rawtext.values():
            print v
        print 
        for claim in a.claims:
            print claim.prettyStr()
