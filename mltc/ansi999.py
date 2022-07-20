import sys
import getopt
import traceback

from x12 import *

_ansi999_spec = None

def getX12Spec999():
    if _ansi999_spec is not None:
        return _ansi999_spec

    loop0_specs = \
      [ X12SegmentSpec("ST", "R", 1, [ X12ElementIsOneOfSpec(1, "999") ]), 
        X12SegmentSpec("AK1", "R", 1),

        # loop AK2
        X12LoopSpec("2000-AK2", 999999,
            [ X12SegmentSpec("AK2", "O", 1),

              # loop AK2/AK3
              X12LoopSpec("2100-AK2/AK3", 999999, 
                  [ X12SegmentSpec("IK3", "O", 1),
                    X12SegmentSpec("CTX", "O", 10),
                    X12LoopSpec("2110-AK2/IK3/IK4", 99999,
                        [ X12SegmentSpec("IK4", "O", 1),
                            X12SegmentSpec("CTX", "O", 10) ]), ]),
              X12SegmentSpec("IK5",  "R", 1) ]),
        X12SegmentSpec("AK9", "R", 1),
        X12SegmentSpec("SE", "R", 1) ]

    __ansi999_spec = X12LoopSpec("0", 1, loop0_specs)
    return __ansi999_spec

def parse999(file_object):
    return X12Document(file_object, getX12Spec999())

def isFileAnsi999(file_object):
    try:
        a = parse999(file_object)
    except X12ParseError:
        return False
    return True

__transaction_set_ack_codes = { \
        'A' : 'Accepted',
        'E' : 'Accepted But Errors Were Noted',
        'M' : 'Rejected, Message Authentication Code (MAC) Failed',
        'R' : 'Rejected',
        'W' : 'Rejected, Assurance Failed Validity Tests',
        'X' : 'Rejected, Content After Decryption Could Not Be Analyzed' }

__transaction_set_syntax_codes = { \
        '1'  : 'Transaction Set Not Supported',
        '2'  : 'Transaction Set Trailer Missing',
        '3'  : 'Transaction Set Control Number in Header and Trailer Do Not Match',
        '4'  : 'Number of Included Segments Does Not Match Actual Count',
        '5'  : 'One or More Segments in Error',
        '6'  : 'Missing or Invalid Transaction Set Identifier',
        '7'  : 'Missing or Invalid Transaction Set Control Number',
        '8'  : 'Authentication Key Name Unknown',
        '9'  : 'Encryption Key Name Unknown',
        '10' : 'Requested Service (Authentication or Encrypted) Not Available',
        '11' : 'Unknown Security Recipient',
        '12' : 'Incorrect Message Length (Encryption Only)',
        '13' : 'Message Authentication Code Failed',
        '15' : 'Unknown Security Originator',
        '16' : 'Syntax Error in Decrypted Text',
        '17' : 'Security Not Supported',
        '18' : 'Transaction Set not in Functional Group',
        '19' : 'Invalid Transaction Set Implementation Convention Reference',
        '23' : 'Transaction Set Control Number Not Unique within the Functional Group',
        '24' : 'S3E Security End Segment Missing for S3S Security Start Segment',
        '25' : 'S3S Security Start Segment Missing for S3E Security End Segment',
        '26' : 'S4E Security End Segment Missing for S4S Security Start Segment',
        '27' : 'S4S Security Start Segment Missing for S4E Security End Segment',
        'I5' : 'Implementation One or More Segments in Error',
        'I6' : 'Implementation Convention not Supported' }

__functional_group_ack_codes = { \
        'A' : 'Accepted',
        'E' : 'Accepted, But Errors Were Noted.',
        'M' : 'Rejected, Message Authentication Code (MAC) Failed',
        'P' : 'Partially Accepted, At Least One Transaction Set Was Rejected',
        'R' : 'Rejected',
        'W' : 'Rejected, Assurance Failed Validity Tests',
        'X' : 'Rejected, Content After Decryption Could Not Be Analyzed' }

__functional_group_syntax_codes = { \
        '1' : 'Functional Group Not Supported',
        '2' : 'Functional Group Version Not Supported',
        '3' : 'Functional Group Trailer Missing',
        '4' : 'Group Control Number in the Functional Group Header and Trailer Do Not Agree',
        '5' : 'Number of Included Transaction Sets Does Not Match Actual Count',
        '6' : 'Group Control Number Violates Syntax',
        '10' : 'Authentication Key Name Unknown',
        '11' : 'Encryption Key Name Unknown',
        '12' : 'Requested Service (Authentication or Encryption) Not Available',
        '13' : 'Unknown Security Recipient',
        '14' : 'Unknown Security Originator',
        '15' : 'Syntax Error in Decrypted Text',
        '16' : 'Security Not Supported',
        '17' : 'Incorrect Message Length (Encryption Only)',
        '18' : 'Message Authentication Code Failed',
        '19' : 'Functional Group Control Number not Unique within Interchange',
        '23' : 'S3E Security End Segment Missing for S3S Security Start Segment',
        '24' : 'S3S Security Start Segment Missing for S3E End Segment',
        '25' : 'S4E Security End Segment Missing for S4S Security Start Segment',
        '26' : 'S4S Security Start Segment Missing for S4E Security End Segment' }

__segment_syntax_codes = { \
        '1' : 'Unrecognized segment ID',
        '2' : 'Unexpected segment',
        '3' : 'Required segment missing',
        '4' : 'Loop Occurs Over Maximum Times',
        '5' : 'Segment Exceeds Maximum Use',
        '6' : 'Segment Not in Defined Transaction Set',
        '7' : 'Segment Not in Proper Sequence',
        '8' : 'Segment Has Data Element Errors',
        'I4' : 'Implementation "Not Used" Segment Present',
        'I6' : 'Implementation Dependent Segment Missing',
        'I7' : 'Implementation Loop Occurs Under Minimum Times',
        'I8' : 'Implementation Segment Below Minimum Use',
        'I9' : 'Implementation Dependent "Not Used" Segment Present' }

__element_syntax_codes = { \
        '1' : 'Mandatory data element missing',
        '2' : 'Conditional required data element missing.',
        '3' : 'Too many data elements.',
        '4' : 'Data element too short.',
        '5' : 'Data element too long.',
        '6' : 'Invalid character in data element.',
        '7' : 'Invalid code value.',
        '8' : 'Invalid Date',
        '9' : 'Invalid Time',
        '10' : 'Exclusion Condition Violated',
        '12' : 'Too Many Repetitions',
        '13' : 'Too Many Components',
        'I10' : 'Implementation "Not Used" Data Element Present',
        'I11' : 'Implementation Too Few Repetitions',
        'I12' : 'Implementation Pattern Match Failure',
        'I13' : 'Implementation Dependent "Not Used" Data Element Present',
        'I6' : 'Code Value Not Used in Implementation',
        'I9' : 'Implementation Dependent Data Element Missing' }


def transactionSetAckCodeToStr(code):
    return __transaction_set_ack_codes[code]

def transactionSetSyntaxCodeToStr(code):
    return __transaction_set_syntax_codes[code]

def functionalGroupAckCodeToStr(code):
    return __functional_group_ack_codes[code]

def functionalGroupSyntaxCodeToStr(code):
    return __functional_group_syntax_codes[code]

def segmentSyntaxCodeToStr(code):
    return __segment_syntax_codes[code]

def elementSyntaxCodeToStr(code):
    return __element_syntax_codes[code]

class Ansi999SegmentElementContext(object):
    def __init__(self, child):
        self.reference = None
        if child.numSubElements(1) > 1:
            self.reference = child.getSubElement(1, 2)

        self.seg_id = child.getElement(2)
        self.seg_pos_in_ts = child.getElement(3)
        self.loop_id = None
        self.pos_in_seg = None
        self.ref_in_seg = None
        if child.numElements() > 3:
            self.loop_id = child.getElement(4)
        if child.numElements() > 4:
            self.pos_in_seg = child.getElement(5)
        if child.numElements() > 5:
            self.ref_in_seg = child.getElement(6)

    def dump(self, indent):
        if self.reference is None:
            return
        line = [ self.reference ]
        if self.loop_id is not None:
            line.append("Loop: %s" % self.loop_id)
        if self.pos_in_seg is not None:
            line.append("Seg pos: %s" % self.pos_in_seg)
        if self.ref_in_seg is not None:
            line.append("Seg ref: %s" % self.ref_in_seg)
        print "%sContext: %s" % (", ".join(line))

class Ansi999DataElementNote(object):
    def __init__(self, loop):

        self.element_contexts = []

        for child in loop.getChildren():
            if not child.isSegment():
                # should never happen
                continue
            segname = child.getName()
            nelem = child.numElements()
            if segname == "IK4":
                self.pos = child.getElement(1)
                self.elem_pos = child.getSubElement(1, 1)
                self.comp_pos = None
                self.rep_pos = None
                if child.numSubElements(1) > 1:
                    self.comp_pos = child.getSubElement(1, 2)
                if child.numSubElements(1) > 2:
                    self.rep_pos = child.getSubElement(1, 3)
                
                self.ref_num = child.getElement(2)
                self.err_code = child.getElement(3)
                self.err_code_str = elementSyntaxCodeToStr(self.err_code)
                self.bad_elem = None
                if child.numElements() >= 4:
                    self.bad_elem = child.getElement(4)
            if segname == "CTX":
                self.element_contexts.append(Ansi999SegmentElementContext(child))

    def dump(self):
        print ""
        print "     Position: %s" % str(self.pos)
        print "     Error:    %s" % str(self.err_code_str)
        if self.bad_elem:
            print "     Bad Element: %s" % self.bad_elem
        for elem_ctx in self.element_contexts:
            elem_ctx.dump("     ")

class Ansi999DataSegmentNote(object):
    def __init__(self, loop):

        self.seg_id_code = None
        self.seg_pos = None
        self.loop_id_code = ""
        self.seg_err_code = None
        self.seg_err_code_str = ""
        self.segment_contexts = []
        self.context_id = None
        self.context_reference = None
        self.data_element_notes = []

        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                nelem = child.numElements()

                if segname == "IK3":
                    self.seg_id_code = child.getElement(1)
                    self.seg_pos = child.getElement(2)
                    if nelem >= 3:
                        self.loop_id_code = child.getElement(3)
                    if nelem >= 4:
                        ec = child.getElement(4)
                        self.seg_err_code = ec
                        self.seg_err_code_str = segmentSyntaxCodeToStr(ec)
                elif segname == "CTX":
                    # is this segment context or a business unit identifier?
                    if child.getSubElement(1, 1) == "SITUATIONAL TRIGGER":
                        self.segment_contexts.append(Ansi999SegmentElementContext(child))
                    else:
                        self.context_id = child.getSubElement(1, 1)
                        self.context_reference = child.getSubElement(1, 2)
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2110-AK2/IK3/IK4":
                    self.data_element_notes.append(Ansi999DataElementNote(child))

    def dump(self):
        print ""
        print "  Data segment %s (position %s)" % (self.seg_id_code, self.seg_pos)
        print "  %s" % self.seg_err_code_str
        for segctx in self.segment_contexts:
            segctx.dump("    ")
        if self.context_id is not None:
            print "  %s, %s" % (self.context_id, self.context_reference)
        for den in self.data_element_notes:
            den.dump()

class Ansi999TransactionSetResponse(object):
    def __init__(self, loop):
        self.ts_id_code = None
        self.ts_control_num = None
        self.ts_ack_code = None
        self.ts_ack_code_str = ""
        self.ts_err_codes = []
        self.ts_err_codes_str = []
        self.data_segment_notes = []

        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                nelem = child.numElements()
                if segname == "AK2":
                    self.ts_id_code = child.getElement(1)
                    self.ts_control_num = child.getElement(2)
                elif segname == "IK5":
                    self.ts_ack_code = child.getElement(1)
                    self.ts_ack_code_str = transactionSetAckCodeToStr(self.ts_ack_code)
                    for i in range(nelem - 1):
                        ec = child.getElement(i+2)
                        self.ts_err_codes.append(ec)
                        self.ts_err_codes_str.append(transactionSetSyntaxCodeToStr(ec))

            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2100-AK2/AK3":
                    self.data_segment_notes.append(Ansi999DataSegmentNote(child))

    def dump(self):
        print ""
        print "  Transaction set %s: %s" % (self.ts_control_num, self.ts_ack_code_str)
        for tsec in self.ts_err_codes_str:
            print "  %s" % tsec
        for dsn in self.data_segment_notes:
            dsn.dump()

class Ansi999TransactionSet(object):
    def __init__(self, x12ts):
        root = x12ts.getRootLoop()

        self.control_num = None
        self.functional_id_code = None
        self.fg_control_num = None
        self.fg_version_code = None

        self.fg_ack_code = None
        self.fg_ack_code_str = ""
        self.fg_err_codes = []
        self.fg_err_codes_str = []
        self.ts_num_included = None
        self.ts_num_received = None
        self.ts_num_accepted = None
        self.ts_responses = []

        for child in root.getChildren():
            if child.isSegment():
                segname = child.getName()
                nelem = child.numElements()
                if segname == "ST":
                    self.control_num = child.getElement(2)
                elif segname == "AK1":
                    self.functional_id_code = child.getElement(1)
                    self.fg_control_num = child.getElement(2)
                    self.fg_version_code = child.getElement(3)
                elif segname == "AK9":
                    self.fg_ack_code = child.getElement(1)
                    self.fg_ack_code_str = functionalGroupAckCodeToStr(self.fg_ack_code)
                    self.ts_num_included = int(child.getElement(2))
                    self.ts_num_received = int(child.getElement(3))
                    self.ts_num_accepted = int(child.getElement(4))
                    for i in range(nelem - 4):
                        ec = child.getElement(i+5)
                        self.fg_err_codes.append(ec)
                        self.fg_err_codes_str.append(functionalGroupSyntaxCodeToStr(ec))
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2000-AK2":
                    self.ts_responses.append(Ansi999TransactionSetResponse(child))

    def dump(self):
        print "Functional group %s: %s" % (self.fg_control_num, self.fg_ack_code_str)
        for fgec in self.fg_err_codes_str:
            print "  %s" % fgec
        for tsr in self.ts_responses:
            tsr.dump()

class Ansi999FunctionalGroup(object):
    def __init__(self, x12fg):
        self.transaction_sets = \
                [ Ansi999TransactionSet(ts) for ts in x12fg.getTransactionSets() ]

    def dump(self):
        print ""
        for ts in self.transaction_sets:
            ts.dump()

class Ansi999Document(object):
    def __init__(self, x12doc):
        self.isa_date = x12doc.getDocumentDate()
        self.isa_time = x12doc.getDocumentTime()
        self.isa_sender = x12doc.getSenderID()
        self.isa_sender_type = x12doc.getSenderIDType()
        self.isa_version = x12doc.getControlVersion()

        self.functional_groups = \
                [ Ansi999FunctionalGroup(fg) for fg in x12doc.getFunctionalGroups() ]

    def dump(self):
        print "ANSI999 Document Date: %s  %s" % (self.isa_date, self.isa_time)
        print "Sender: %s" % self.isa_sender
        print "Document version: %s" % self.isa_version

        for fg in self.functional_groups:
            fg.dump()

if __name__ == "__main__":
    def usage():
        usage_str="""usage:  ansi999.py [options] <filename>

    filename should be an ASC X12N 999 file

    If no options are specified, then the file is parsed into human-readable 
    text.

OPTIONS:
    -h, --help      shows this help text\n"""
        usage()
        print usage_str

    if len(sys.argv) < 2:
        sys.exit(1)

    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help' ])
    
    fname = args[0]
    f = file(fname, 'r')
    try:
        a999x12 = parse999(f)
        a999doc = Ansi999Document(a999x12)
        a999doc.dump()
    except ValueError, e:
        print "file does not appear to be an ANSI 999 file!"
        traceback.print_exc()
        sys.exit(1)

#    print "DATE: %s TIME: %s" % (a.date, a.time)
#    print
#    for v in a.rawtext.values():
#        print v
#    print 
#    for claim in a.claims:
#        print claim.prettyStr()
