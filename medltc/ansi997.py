import sys
import getopt
import traceback

from x12 import *

_ansi997_spec = None

def getX12Spec997():
    if _ansi997_spec is not None:
        return _ansi997_spec

    loop0_specs = \
      [ X12SegmentSpec("ST", "R", 1, [ X12ElementSpec(1, "997") ]), 
        X12SegmentSpec("AK1", "R", 1),

        # loop AK2
        X12LoopSpec("AK2", 999999,
            [ X12SegmentSpec("AK2", "O", 1),

              # loop AK2/AK3
              X12LoopSpec("AK2/AK3", 999999, 
                  [ X12SegmentSpec("AK3", "O", 1),
                    X12SegmentSpec("AK4", "O", 99) ]),
              X12SegmentSpec("AK5",  "R", 1) ]),
        X12SegmentSpec("AK9", "R", 1),
        X12SegmentSpec("SE", "R", 1) ]

    __ansi997_spec = X12LoopSpec("0", 1, loop0_specs)
    return __ansi997_spec

def parse997(file_object):
    return X12Document(file_object, getX12Spec997())

def isFileAnsi997(file_object):
    try:
        a = parse997(file_object)
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
        '23' : 'Transaction Set Control Number Not Unique within the Functional Group',
        '24' : 'S3E Security End Segment Missing for S3S Security Start Segment',
        '25' : 'S3S Security Start Segment Missing for S3E Security End Segment',
        '26' : 'S4E Security End Segment Missing for S4S Security Start Segment',
        '27' : 'S4S Security Start Segment Missing for S4E Security End Segment' }

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
        '23' : 'S3E Security End Segment Missing for S3S Security Start Segment',
        '24' : 'S3S Security Start Segment Missing for S3E End Segment',
        '25' : 'S4E Security End Segment Missing for S4S Security Start Segment',
        '26' : 'S4S Security Start Segment Missing for S4E Security End Segment' }

__segment_syntax_codes = { \
        '1' : 'Unrecognized segment ID',
        '2' : 'Unexpected segment',
        '3' : 'Mandatory segment missing',
        '4' : 'Loop Occurs Over Maximum Times',
        '5' : 'Segment Exceeds Maximum Use',
        '6' : 'Segment Not in Defined Transaction Set',
        '7' : 'Segment Not in Proper Sequence',
        '8' : 'Segment Has Data Element Errors' }

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
        '10' : 'Exclusion Condition Violated' }


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

if __name__ == "__main__":
    def usage():
        usage_str="""usage:  ansi997.py [options] <filename>

    filename should be an ASC X12N 997 (004010X091) file

    If no options are specified, then the file is parsed into human-readable 
    text.

OPTIONS:
    -h, --help      shows this help text\n"""
        print usage_str

    if len(sys.argv) < 2:
        sys.exit(1)

    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help' ])
    
    fname = args[0]
    f = file(fname, 'r')
    try:
        a997 = parse997(f)
        a997.dump()
    except ValueError, e:
        print "file does not appear to be an ANSI 997 file!"
        traceback.print_exc()
        sys.exit(1)

#    print "DATE: %s TIME: %s" % (a.date, a.time)
#    print
#    for v in a.rawtext.values():
#        print v
#    print 
#    for claim in a.claims:
#        print claim.prettyStr()
