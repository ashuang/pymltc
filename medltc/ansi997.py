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

def parse997(fname):
    return X12Document(file(fname, "r"), getX12Spec997())

def isFileAnsi997(fname):
    try:
        a = parse997(fname)
    except X12ParseError:
        return False
    return True

def usage():
    usage_str="""usage:  ansi997.py [options] <filename>

    filename should be an ASC X12N 997 (004010X091) file

    If no options are specified, then the file is parsed into human-readable 
    text.

OPTIONS:
    -h, --help      shows this help text
"""

    print usage_str

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    opts, args = getopt.getopt(sys.argv[1:], 'h', [ 'help' ])
    
    fname = args[0]
    try:
        a997 = parse997(fname)
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
