import sys
import getopt
import traceback

from x12 import *

_ansi835_spec = None

def getX12Spec835():
    if _ansi835_spec is not None:
        return _ansi835_spec

    loop0_specs = \
      [ X12SegmentSpec("ST", "R", 1, [ X12ElementSpec(1, "835") ]), 
        X12SegmentSpec("BPR"),
        X12SegmentSpec("TRN"),
        X12SegmentSpec("CUR", "O"),
        X12SegmentSpec("REF", "O", 2),
        X12SegmentSpec("DTM", "O"),

        # loop 1000A
        X12LoopSpec("1000A", 1,
          [ X12SegmentSpec("N1"),
            X12SegmentSpec("N3"),
            X12SegmentSpec("N4"),
            X12SegmentSpec("REF", "O", 4),
            X12SegmentSpec("PER", "O", 3) ]),

        # loop 1000B
        X12LoopSpec("1000B", 1,
          [ X12SegmentSpec("N1"),
            X12SegmentSpec("N3", "O"),
            X12SegmentSpec("N4", "O"),
            X12SegmentSpec("REF", "O", 999),
            X12SegmentSpec("PER", "O") ]),

        # loop 2000
        X12LoopSpec("2000", 999999,
          [ X12SegmentSpec("LX", "O"),
            X12SegmentSpec("TS3", "O"),
            X12SegmentSpec("TS2", "O"),

            X12LoopSpec("2100", 999999,
              [ X12SegmentSpec("CLP"),
                X12SegmentSpec("CAS", "O", 99),
                X12SegmentSpec("NM1"),
                X12SegmentSpec("NM1", "O", 6),
                X12SegmentSpec("MIA", "O", 1),
                X12SegmentSpec("MOA", "O", 1),
                X12SegmentSpec("REF", "O", 15),
                X12SegmentSpec("DTM", "O", 4),
                X12SegmentSpec("PER", "O", 3),
                X12SegmentSpec("AMT", "O", 14),
                X12SegmentSpec("QTY", "O", 15),

                X12LoopSpec("2110", 999,
                  [ X12SegmentSpec("SVC", "O"),
                    X12SegmentSpec("DTM", "O", 3),
                    X12SegmentSpec("CAS", "O", 99),
                    X12SegmentSpec("REF", "O", 17),
                    X12SegmentSpec("AMT", "O", 12),
                    X12SegmentSpec("QTY", "O", 6),
                    X12SegmentSpec("LQ", "O", 99) ]) ]) ]),

        X12SegmentSpec("PLB", "O", 99999),
        X12SegmentSpec("SE") ]

    __ansi835_spec = X12LoopSpec("0", 1, loop0_specs)
    return __ansi835_spec

def parse835(file_object):
    return X12Document(file_object, getX12Spec835())

def isFileAnsi835(file_object):
    try:
        a = parse835(file_object)
    except X12ParseError:
        return False
    return True

if __name__ == "__main__":
    def usage():
        usage_str="""usage:  ansi835.py [options] <filename>

    filename should be an ASC X12N 835 (004010X091) file

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
        a835 = parse835(f)
        a835.dump()
    except ValueError, e:
        print "file does not appear to be an ANSI 835 file!"
        traceback.print_exc()
        sys.exit(1)

#    print "DATE: %s TIME: %s" % (a.date, a.time)
#    print
#    for v in a.rawtext.values():
#        print v
#    print 
#    for claim in a.claims:
#        print claim.prettyStr()
