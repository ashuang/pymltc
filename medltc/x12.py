import sys
from datetime import date, time
import types

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

class X12Segment(object):
    def __init__(self, name, elements):
        self.name = name
        self.elements = elements
        # segment position within transaction set.
        self.st_seg_pos = 0

        for e in elements:
            te = type(e)
            assert te == types.StringType or te == types.TupleType

    def isSegment(self):
        return True

    def isLoop(self):
        return False

    def dump(self, indent=0):
        print ("%s%s" % (("  " * indent), self.name))

    def __elemToStr(self, elem, subelem_separator):
        if type(elem) == types.TupleType:
            return subelem_separator.join(elem)
        else:
            return str(elem)

    def format(self, elem_separator="*", subelem_separator=":", segment_terminator="~"):
        return "%s%s%s%s" % (self.name, elem_separator, 
                elem_separator.join([ self.__elemToStr(e, subelem_separator) for e in self.elements ]),
                segment_terminator)

    def getName(self):
        return self.name

    def getElement(self, index):
        return self.elements[index-1]

    def getElements(self):
        return self.elements

    def numElements(self):
        return len(self.elements)

    def getSubElement(self, index, sub_index):
        e = self.elements[index-1]
        if type(e) != types.TupleType:
            if sub_index == 1:
                return e
            raise ValueError("%s%02d (pos %d) does not have sub-elements" % \
                    (self.name, index, self.st_seg_pos))
        return e[sub_index-1]

    def numSubElements(self, index):
        e = self.elements[index-1]
        if type(e) != types.TupleType:
            return 1
        else:
            return len(e)

    def setSegmentPosition(self, pos):
        self.st_seg_pos = pos

class X12Loop(object):
    def __init__(self, loop_name):
        self.loop_name = loop_name

        # Each object in self.children must be either an X12Loop or X12Segment
        # object
        self.children = []

    def isSegment(self):
        return False

    def isLoop(self):
        return True

    def dump(self, indent = 0):
        assert len(self.children)
        pfx = "  " * indent
        print("%sLoop %s [" % (pfx, self.loop_name))
        for item in self.children:
            item.dump(indent + 1)
        print("%s]" % pfx)

    def getLoopName(self):
        return self.loop_name

    def add(self, segment_or_loop):
        if len(self.children) == 0:
            assert segment_or_loop.isSegment()
        else:
            assert segment_or_loop.isLoop() or segment_or_loop.isSegment()

        self.children.append(segment_or_loop)

    def getChildren(self):
        return self.children

    def getSubLoopsByName(self, loop_name):
        return [ c for c in self.children \
                if c.isLoop() and c.getLoopName() == loop_name ]

    def getSegmentsByName(self, seg_name):
        return [ c for c in self.children \
                if c.isSegment() and c.getName() == seg_name ]

class X12ParseError(ValueError):
    pass

class X12Handler(object):
    def startInterchangeControl(self, isa_segment):
        pass

    def endInterchangeControl(self, iea_segment):
        pass

    def startFunctionalGroup(self, gs_segment):
        pass

    def endFunctionalGroup(self, ge_segment):
        pass

    def startTransactionSet(self, st_segment):
        pass
    
    def endTransactionSet(self, se_segment):
        pass

    def interchangeAcknowledgment(self, ta1):
        pass

    def segment(self, segname, seg):
        pass

class SimpleHandler(X12Handler):
    def __init__(self):
        pass

    def startInterchangeControl(self, isa_segment):
        print "[ISA]"

    def endInterchangeControl(self, iea_segment):
        print "[IEA]"

    def startFunctionalGroup(self, gs_segment):
        print "  [GS]"

    def endFunctionalGroup(self, ge_segment):
        print "  [GE]"

    def startTransactionSet(self, st_segment):
        print "    [ST]"
    
    def endTransactionSet(self, se_segment):
        print "    [SE]"

    def interchangeAcknowledgment(self, ta1):
        print "  [TA1]"

    def segment(self, segname, seg):
        print "      [%s]" % segname

class X12ElementSpec(object):
    def __init__(self, index, *values):
        self.index = index
        self.values = values

    def getIndex(self):
        return self.index

    def getValues(self):
        return self.values

class X12SegmentSpec(object):
    def __init__(self, name, usage = "R", max_repeat = 1, element_specs = []):
        self.name = name
        self.usage = usage
        self.max_repeat = max_repeat
        self.elem_specs = element_specs
        if len(name) < 2:
            raise ValueError("Invalid name")
        if usage not in "RSO":
            raise ValueError("Segment usage must be 'R', 'S', or 'O'")
        if max_repeat < 1:
            raise ValueError("Invalid max_repeat")

#        assert(all([isinstance(es, X12ElementSpec) for es in element_specs]))

    def isSegmentSpec(self):
        return True

    def isLoopSpec(self):
        return False

    def getSegName(self):
        return self.name

    def getUsage(self):
        return self.usage

    def isRequired(self):
        return self.usage == "R"

    def getMaxSegmentRepeat(self):
        return self.max_repeat

    def getElementSpecs(self):
        return self.element_specs

    def matchesSegment(self, seg):
        if seg.name != self.name: return False
        for espec in self.elem_specs:
            if seg.getElement(espec.index) not in espec.values:
                return False
        return True

    def dump(self, indent = 0):
        print ("%s%s" % (("  " * indent), self.name))

class X12LoopSpec(object):
    def __init__(self, loop_name, loop_repeat, segment_and_loop_specs):
        self.loop_name = loop_name
        self.specs  = segment_and_loop_specs
        self.loop_repeat = loop_repeat

        assert self.specs[0].isSegmentSpec()
        assert self.specs[0].getMaxSegmentRepeat() == 1

#        assert(all([isinstance(sl, X12LoopSpec) or isinstance(sl, X12SegmentSpec) \
        #                for sl in segment_and_loop_specs]))

    def getLoopName(self):
        return self.loop_name

    def getSpecs(self):
        return self.specs

    def getMaxLoopRepeat(self):
        return self.loop_repeat

    def getSegName(self):
        return self.specs[0].getSegName()

    def matchesSegment(self, seg):
        return self.specs[0].matchesSegment(seg)

    def isRequired(self):
        return self.specs[0].isRequired()

    def isSegmentSpec(self):
        return False

    def isLoopSpec(self):
        return True

    def dump(self, indent = 0):
        print ("%sLoop %s" % (("  " * indent), self.loop_name))
        for spec in self.specs:
            spec.dump(indent+1)
    
class X12Parser(object):
    def __init__(self):
        pass

    def parse(self, f, handler):
        self.num_segments_parsed = 0
        self.f = f
        self.elem_sep = None
        self.subelem_sep = None
        self.segment_sep = None
        self.handler = handler
        self.st_seg_pos = 0
        self.in_st = False

        # ========= parse the ISA segment ==========

        # check that the first three bytes read "ISA"
        segname = f.read(3)
        if segname != "ISA":
            raise X12ParseError("Expected ISA, not \"%s\"" % segname)

        # the first element separator defines the element separator to be used
        # throughout the entire interchange
        self.elem_sep = f.read(1)
        
        # read the ISA fields into an array
        elements = []
        # read in the next 15 fields all at once.  Field lengths are defined in
        # ANSI X12 spec
        for i in [ 2, 10, 2, 10, 2, 15, 2, 15, 6, 4, 1, 5, 9, 1, 1 ]:
            s = f.read(i)
            c = f.read(1)
            if c != self.elem_sep: 
                raise X12ParseError("element separator not found! %s" % c)
            elements.append(s)
        elements.append(f.read(1))

#        authorization_information_qualifier = elements[0]
#        authorization_information = elements[1]
#        security_information_qualifier = self.isa[2]
#        self.senderid = self.isa[3]
#        self.receiverqual = self.isa[4]
#        self.receiverid = self.isa[5]
#        self.date = splitdate(self.isa[6])
#        self.time = hhmm2time(self.isa[7])
#        self.production = (self.isa[8] == "P")
        self.subelem_sep = elements[15]
        self.segment_sep = self.f.read(1)
#        if authorization_information_qualifier not in ("00", "03"):
#            self.__warn("invalid ISA01")

        # TODO validation

        # ========== remaining segments =============

        self.num_segments_parsed += 1
        self.handler.startInterchangeControl(X12Segment("ISA", elements))

        n_functional_groups = 0
        while True:
            # expect GS on first loop.  On subsequent loops, IEA is ok.  
            # TA1 is also ok
            seg = self.__readSegment()
            if seg.getName() == "GS":
                self.handler.startFunctionalGroup(seg)
                n_functional_groups += 1
            elif seg.getName() == "TA1":
                self.handler.interchangeAcknowledgment(seg)
                continue
            elif n_functional_groups == 0:
                self.__fail("Expected GS segment, got [%s]\n" % seg.getName())
            elif seg.getName() == "IEA":
                self.handler.endInterchangeControl(seg)
                break
            else:
                self.__fail("Expected GS or IEA segment, got [%s]\n" % seg.getName())

            # count the number of transaction sets within a functional group
            n_transaction_sets = 0

            while True:
                # expect ST on first loop.  On subsequent loops, GT is ok
                seg = self.__readSegment()
                if seg.getName() == "ST":
                    self.handler.startTransactionSet(seg)
                    seg.setSegmentPosition(1)
                    self.st_seg_pos += 1
                    n_transaction_sets += 1
                elif n_transaction_sets == 0:
                    self.__fail("Expected ST segment, got [%s]\n" % seg.getName())
                elif seg.getName() == "GE":
                    self.handler.endFunctionalGroup(seg)
                    break
                else:
                    self.__fail("Expected ST or GE segment, got [%s]\n" % seg.getName())

                while True:
                    seg = self.__readSegment()
                    seg.setSegmentPosition(self.st_seg_pos)
                    self.st_seg_pos += 1
                    if seg.getName() == "SE":
                        self.handler.endTransactionSet(seg)
                        break
                    else:
                        self.handler.segment(seg.getName(), seg)

    def __readSegment(self):
        """assumes that self.f is positioned on the beginning of a segment
        (i.e. right after a segment terminator).  Reads the entire segment, 
        and returns with self.f positioned at the beginning of the next
        segment.  Returns an array, one entry per segment element.  
        """
        segname = None
        elements = []
        self.num_segments_parsed += 1
        more_elements = True
        while more_elements:
            elem_chars = []
            has_subelems = False
            c = ""
            while True:
                c = self.f.read(1)

                # HACK -- allow newlines in between segment separator
                while not segname and not elem_chars and c in "\r\n":
                    c = self.f.read(1)

                if len(c) != 1:
                    self.__fail("error reading element/segment separator")

                if not elements and not elem_chars and c.isspace():
                    # allow whitespace in between segments
                    continue
                if c == self.elem_sep:
                    break
                elif c == self.segment_sep:
                    more_elements = False
                    break
                elif c == self.subelem_sep:
                    has_subelems = True
                elem_chars.append(c)

            if has_subelems:
                elem = tuple("".join(elem_chars).split(self.subelem_sep))
            else:
                elem = "".join(elem_chars)

            if segname is None:
                segname = elem
            else:
                elements.append(elem)

        return X12Segment(segname, elements)

    def __warn(self, txt):
        # TODO
        sys.stderr.write("%s\n" % txt)
        pass

    def __fail(self, txt):
        raise X12ParseError("segment %d:  %s\n" % \
                (self.num_segments_parsed, txt))

class _LoopParseStatus(object):
    def __init__(self, loopSpec, loop):
        self.loopSpec = loopSpec
        self.index = 0
        self.loop_repeat = 1
        self.loop = loop
        self.segment_repeat = 0

class _X12DocumentHandler(X12Handler):
    def __init__(self, document, spec):
        self.doc = document
        self.spec = spec

        self.loopStack = []

    def __warn(self, msg):
        sys.stderr.write("WARNING: %s\n" % msg)

    def startInterchangeControl(self, isa):
        self.doc.isaSenderIDType = isa.getElement(5)
        self.doc.isaSenderID = isa.getElement(6)
        self.doc.isaReceiverIDType = isa.getElement(7)
        self.doc.isaReceiverID = isa.getElement(8)
        self.doc.isaDate = yymmdd2date(isa.getElement(9))
        self.doc.isaTime = hhmm2time(isa.getElement(10))
        
        self.doc.isaControlVersion = isa.getElement(12)

        if self.doc.isaControlVersion == "00501":
            self.doc.isaRepetitionSeparator = isa.getElement(11)
        elif self.doc.isaControlVersion == "00401":
            self.doc.isaRepetitionSeparator = None
            icsi = isa.getElement(11)
            if icsi != "U":
                raise X12ParseError("Invalid ISA11: [%s]" % icsi)
        else:
            icvn = self.doc.isaControlVersion
            raise X12ParseError("Invalid ISA12: [%s]" % icvn)

        self.doc.isaICN = isa.getElement(13)

        ui = isa.getElement(15)
        if ui not in "PT":
            raise X12ParseError("Invalid ISA15: [%s]" % ui)
        self.doc.isaProduction = (ui == "P")
        pass

    def endInterchangeControl(self, iea):
        # TODO check number of functional groups

        icn = iea.getElement(2)
        if icn != self.doc.isaICN:
            self.__warn("IEA02 does not match ISA13: %s / %s" % \
                    (icn, self.doc.isaICN))

    def startFunctionalGroup(self, gs_segment):
        fg = X12FunctionalGroup(gs_segment)
        self.doc.functional_groups.append(fg)

    def endFunctionalGroup(self, ge_segment):
        pass

    def startTransactionSet(self, st):
        if len(self.loopStack) > 0:
            raise X12ParseError("Unexpected ST")

        stobj = X12TransactionSet(st)
        self.doc.functional_groups[-1].transaction_sets.append(stobj)
        self.loopStack = [ _LoopParseStatus(self.spec, stobj.loop0) ]

        self.segment(st.getName(), st)

    def endTransactionSet(self, se):
        self.segment(se.getName(), se)
        self.loopStack = []

    def interchangeAcknowledgment(self, ta1):
        self.doc.ta1ICN = ta1.getElement(1)
        self.doc.ta1Date = yymmdd2date(ta1.getElement(2))
        self.doc.ta1Time = hhmm2time(ta1.getElement(3))
        self.doc.ta1Status = ta1.getElement(4)
        self.doc.ta1Code = ta1.getElement(5)

    def matchSegment(self, segname, seg, lp):
        # is there more in this loop?
        specs = lp.loopSpec.getSpecs()
        while lp.index < len(specs):
            spec = specs[lp.index]

            if spec.matchesSegment(seg):
                # matched the next spec.

                if spec.isLoopSpec():
                    dbg("   entering loop %s" % spec.getLoopName())
                    newloop = X12Loop(spec.getLoopName())
                    newloop.add(seg)
                    newlp = _LoopParseStatus(spec, newloop)
                    newlp.index += 1
                    newlp.segment_repeat = 0

                    lp.loop.add(newloop)
                    self.loopStack.append(newlp)
                else:
                    lp.loop.add(seg)
                    lp.segment_repeat += 1
                    if lp.segment_repeat >= spec.getMaxSegmentRepeat():
                        lp.segment_repeat = 0
                        lp.index += 1

                return True
            elif spec.isRequired() and lp.segment_repeat == 0:
                # a segment can only be required once

                # uh oh.  did not match a required segment.
#                print "  Unable to match %s to a loop" % segname
                raise X12ParseError("In loop %s - error matching on segment %s\n[%s]" % \
                        (lp.loopSpec.getLoopName(), segname, seg.format()))
            else:
#                dbg("  skipping [%s]" % spec.getSegName())
                # did not match, but the next segment was not required
                # try the next spec in this loop (or bottom out of the loop)
                lp.index += 1
                lp.segment_repeat = 0

        # reached the end of the loop.  Can either repeat, or pop out
        if lp.loop_repeat >= lp.loopSpec.getMaxLoopRepeat():
            # hit repeat limit.  do not try to repeat the loop
            return False
        else:
            if lp.loopSpec.matchesSegment(seg):
                lp.loop_repeat += 1
                lp.index = 1
                lp.segment_repeat = 0
                
                newloop = X12Loop(lp.loopSpec.getLoopName())
                newloop.add(seg)
                self.loopStack[-2].loop.add(newloop)
                lp.loop = newloop
                return True

    def segment(self, segname, seg):
        dbg("[%s]" % segname)
        # is there more in this loop?
        while not self.matchSegment(segname, seg, self.loopStack[-1]):
            dbg("   leaving loop %s" % self.loopStack[-1].loopSpec.getLoopName())
            self.loopStack.pop(-1)

            if len(self.loopStack) == 0:
                raise X12ParseError("Don't know what to do with segment %s" % \
                        segname)
            else:
                self.loopStack[-1].index += 1
        self.doc.all_segments.append(seg)

class X12TransactionSet(object):
    def __init__(self, st_seg):
        self.tsid = st_seg.getElement(1)
        self.tscn = st_seg.getElement(2)
        self.loop0 = X12Loop("ST")

    def getTransactionSetControlNumber(self):
        return self.tscn

    def getRootLoop(self):
        return self.loop0

    def dump(self):
        self.loop0.dump()

class X12FunctionalGroup(object):
    def __init__(self, gs_seg):
        self.fic = gs_seg.getElement(1)
        self.gcn = gs_seg.getElement(6)
        self.transaction_sets = []

    def getGroupControlNumber(self):
        return self.gcn

    def getTransactionSets(self):
        return self.transaction_sets

    def dump(self):
        # TODO
        for ts in self.transaction_sets:
            ts.dump()

class X12Document(object):
    def __init__(self, f, spec):
        self.isaSenderID = None
        self.isaSenderIDType = "ZZ"
        self.isaReceiverID = None
        self.isaReceiverIDType = "ZZ"
        self.isaDate = None
        self.isaTime = None
        self.isaICN = None
        self.isaProduction = False
        self.isaControlVersion = None
        self.isaRepetitionSeparator = None
        self.all_segments = []

        self.ta1ICN = None
        self.ta1Date = None
        self.ta1Time = None
        self.ta1Status = None
        self.ta1Code = None

        self.functional_groups = []

        handler = _X12DocumentHandler(self, spec)

        parser = X12Parser()
        parser.parse(f, handler)

    def getDocumentDate(self):
        return self.isaDate

    def getDocumentTime(self):
        return self.isaTime

    def getSenderID(self):
        return self.isaSenderID

    def getSenderIDType(self):
        return self.isaSenderIDType

    def getReceiverID(self):
        return self.isaReceiverID

    def getReceiverIDType(self):
        return self.isaReceiverIDType

    def getInterchangeControlNumber(self):
        return self.isaICN

    def isProductionMode(self):
        return self.isaProduction

    def hasTA1(self):
        return self.ta1ICN is not None

    def getTA1ICN(self):
        assert(self.ta1ICN is not None)
        return self.ta1ICN

    def getTA1Date(self):
        return self.ta1Date

    def getTA1Time(self):
        return self.ta1Time

    def getTA1AcknowledgementCode(self):
        return self.ta1Status

    def getTA1NoteCode(self):
        return self.ta1Code

    def getFunctionalGroups(self):
        return self.functional_groups

    def getControlVersion(self):
        return self.isaControlVersion

#    def getRepetitionSeparator(self):
#        return self.isaRepetitionSeparator

    def dump(self):
        for fg in self.functional_groups:
            for ts in fg.transaction_sets:
                ts.dump()

__ta1_note_codes = { \
        '000' : 'No error',
        '001' : 'The Interchange Control Number in the Header and Trailer Do Not Match. The Value From the Header is Used in the Acknowledgment.',
        '002' : 'This Standard as Noted in the Control Standards Identifier is Not Supported.',
        '003' : 'This Version of the Controls is Not Supported',
        '004' : 'The Segment Terminator is Invalid',
        '005' : 'Invalid Interchange ID Qualifier for Sender',
        '006' : 'Invalid Interchange Sender ID',
        '007' : 'Invalid Interchange ID Qualifier for Receiver',
        '008' : 'Invalid Interchange Receiver ID',
        '009' : 'Unknown Interchange Receiver ID',
        '010' : 'Invalid Authorization Information Qualifier Value',
        '011' : 'Invalid Authorization Information Value',
        '012' : 'Invalid Security Information Qualifier Value',
        '013' : 'Invalid Security Information Value',
        '014' : 'Invalid Interchange Date Value',
        '015' : 'Invalid Interchange Time Value',
        '016' : 'Invalid Interchange Standards Identifier Value',
        '017' : 'Invalid Interchange Version ID Value',
        '018' : 'Invalid Interchange Control Number Value',
        '019' : 'Invalid Acknowledgment Requested Value',
        '020' : 'Invalid Test Indicator Value',
        '021' : 'Invalid Number of Included Groups Value',
        '022' : 'Invalid Control Structure',
        '023' : 'Improper (Premature) End-of-File (Transmission)',
        '024' : 'Invalid Interchange Content (e.g., Invalid GS Segment)',
        '025' : 'Duplicate Interchange Control Number',
        '026' : 'Invalid Data Element Separator',
        '027' : 'Invalid Component Element Separator',
        '028' : 'Invalid Delivery Date in Deferred Delivery Request',
        '029' : 'Invalid Delivery Time in Deferred Delivery Request',
        '030' : 'Invalid Delivery Time Code in Deferred Delivery Request',
        '031' : 'Invalid Grade of Service Code' }

__ta1_acknowledgment_codes = { \
        'A' : 'The Transmitted Interchange Control Structure Header and Trailer Have Been Received and Have No Errors.',
        'E' : 'The Transmitted Interchange Control Structure Header and Trailer Have Been Received and Are Accepted But Errors Are Noted. This Means the Sender Must Not Resend This Data.',
        'R' : 'The Transmitted Interchange Control Structure Header and Trailer are Rejected Because of Errors.' }

def ta1NoteCodeToStr(note_code):
    return __ta1_note_codes[note_code]

def ta1AcknowledgmentCodeToStr(acknowledgment_code):
    return __ta1_acknowledgment_codes[acknowledgment_code]

def dbg(text):
    pass
#    sys.stderr.write("%s\n" % text)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("usage: x12.py <edifact_file>\n")
        sys.exit(1)

    f = file(sys.argv[1], "r")
    p = X12Parser()
    p.parse(f, SimpleHandler())
