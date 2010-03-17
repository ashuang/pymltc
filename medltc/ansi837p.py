import sys
import getopt
import traceback

from x12 import *

_ansi837p_spec = None

def _elemSpec1(*vals):
    return [ X12ElementSpec(1, *vals) ]
def _elemSpec2(*vals):
    return [ X12ElementSpec(2, *vals) ]
def _elemSpec3(*vals):
    return [ X12ElementSpec(3, *vals) ]

_2010AA_BP_ES = _elemSpec1("0B", "1A", "1B", "1C", "1D", "1G", "1H", "1J", 
                    "B3", "BQ", "EI", "FH", "G2", "G5", "LU", "SY", 
                    "U3", "X5")

_2010AA_CC_ES = _elemSpec1("06", "8U", "EM", "IJ", "LU", "RB", "ST", "TT")

_PATSUB_SI_ES = _elemSpec1("1W", "23", "IG", "SY")

_SVC_FAC_NM1_ES = _elemSpec1("77", "FA", "LI", "TL")

def getX12Spec837p():
    if _ansi837p_spec is not None:
        return _ansi837p_spec

    loop0_specs = \
      [ X12SegmentSpec("ST", "R", 1, _elemSpec1("837")), 
        X12SegmentSpec("BHT"),
        X12SegmentSpec("REF"),

        # loop 1000A - Submitter name
        X12LoopSpec("1000A", 1,
          [ X12SegmentSpec("NM1"),
            X12SegmentSpec("N2", "S"),
            X12SegmentSpec("PER") ]),

        # loop 1000B - Receiver name
        X12LoopSpec("1000B", 1,
          [ X12SegmentSpec("NM1"),
            X12SegmentSpec("N2", "S") ]),

        # loop 2000A - Billing/Pay-to provider
        X12LoopSpec("2000A", 999999,
          [ X12SegmentSpec("HL"),
            X12SegmentSpec("PRV", "S"),
            X12SegmentSpec("CUR", "S"),

            # loop 2010AA : Billing provider name
            X12LoopSpec("2010AA", 1,
              [ X12SegmentSpec("NM1"),
                X12SegmentSpec("N2", "S"),
                X12SegmentSpec("N3"),
                X12SegmentSpec("N4"),
                X12SegmentSpec("REF", "S", 8, _2010AA_BP_ES),
                X12SegmentSpec("REF", "S", 8, _2010AA_CC_ES),
                X12SegmentSpec("PER", "S", 2) ]),

            # loop 2010AB : Pay-to provider name
            X12LoopSpec("2010AB", 1,
              [ X12SegmentSpec("NM1", "S"),
                X12SegmentSpec("N2", "S"),
                X12SegmentSpec("N3"),
                X12SegmentSpec("N4"),
                X12SegmentSpec("REF", "S", 5) ]),
        
            # loop 2000B - Subscriber
            X12LoopSpec("2000B", 999999,
              [ X12SegmentSpec("HL", "R", 1, _elemSpec3("22")),
                X12SegmentSpec("SBR"),
                X12SegmentSpec("PAT", "S"),

                # loop 2010BA - Subscriber name
                X12LoopSpec("2010BA", 1,
                  [ X12SegmentSpec("NM1", "R", 1, _elemSpec1("IL")),
                    X12SegmentSpec("N2", "S"),
                    X12SegmentSpec("N3", "S"),
                    X12SegmentSpec("N4", "S"),
                    X12SegmentSpec("DMG", "S"),
                    X12SegmentSpec("REF", "S", 4, _PATSUB_SI_ES),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("Y4")) ]),

                # loop 2010BB - Payer name
                X12LoopSpec("2010BB", 1,
                  [ X12SegmentSpec("NM1", "R", 1, _elemSpec1("PR")),
                    X12SegmentSpec("N2", "S"),
                    X12SegmentSpec("N3", "S"),
                    X12SegmentSpec("N4", "S"),
                    X12SegmentSpec("REF", "S", 3) ]),

                # loop 2010BC - Responsible party name
                X12LoopSpec("2010BC", 1,
                  [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("QD")),
                    X12SegmentSpec("N2", "S"),
                    X12SegmentSpec("N3"),
                    X12SegmentSpec("N4") ]),

                # loop 2010BD - Credit/Debit card holder name
                X12LoopSpec("2010BD", 1,
                  [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("AO")),
                    X12SegmentSpec("N2", "S"),
                    X12SegmentSpec("REF", "S", 2) ]),

                # loop 2000C - Patient
                X12LoopSpec("2000C", 1,
                  [ X12SegmentSpec("HL", "S", 1, _elemSpec3("23")),
                    X12SegmentSpec("PAT"),

                    # loop 2010CA - Patient name
                    X12LoopSpec("2010CA", 1,
                        [ X12SegmentSpec("NM1"),
                          X12SegmentSpec("N2", "S"),
                          X12SegmentSpec("N3"),
                          X12SegmentSpec("N4"),
                          X12SegmentSpec("DMG"),
                          X12SegmentSpec("REF", "S", 5, _PATSUB_SI_ES),
                          X12SegmentSpec("REF", "S", 1, 
                              _elemSpec1("Y4")) ]) ]),
              
                # loop 2300 - Claim information
                X12LoopSpec("2300", 100,
                  [ X12SegmentSpec("CLM"),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("938")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("454")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("330")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("304")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("431")),
                    X12SegmentSpec("DTP", "S", 5, _elemSpec1("453")),
                    X12SegmentSpec("DTP", "S", 10, _elemSpec1("438")),
                    X12SegmentSpec("DTP", "S", 10, _elemSpec1("439")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("484")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("455")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("ABC")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("471")),
                    X12SegmentSpec("DTP", "S", 5, _elemSpec1("360")),
                    X12SegmentSpec("DTP", "S", 5, _elemSpec1("361")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("297")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("296")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("435")),
                    X12SegmentSpec("DTP", "S", 1, _elemSpec1("096")),
                    X12SegmentSpec("DTP", "S", 2, _elemSpec1("090", "091")),
                    X12SegmentSpec("PWK", "S", 10),
                    X12SegmentSpec("CN1", "S"),
                    X12SegmentSpec("AMT", "S", 1, _elemSpec1("MA")),
                    X12SegmentSpec("AMT", "S", 1, _elemSpec1("F5")),
                    X12SegmentSpec("AMT", "S", 1, _elemSpec1("NE")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("4N")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("F5")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("EW")),
                    X12SegmentSpec("REF", "S", 2, _elemSpec1("9F", "G1")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("F8")),
                    X12SegmentSpec("REF", "S", 3, _elemSpec1("X4")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("9A")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("9C")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("LX")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("D9")),
                    X12SegmentSpec("REF", "S", 4, _elemSpec1("1S")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("EA")),
                    X12SegmentSpec("REF", "S", 1, _elemSpec1("P4")),
                    X12SegmentSpec("K3", "S", 10),
                    X12SegmentSpec("NTE", "S"),
                    X12SegmentSpec("CR1", "S"),
                    X12SegmentSpec("CR2", "S"),
                    X12SegmentSpec("CRC", "S", 3, _elemSpec1("07")),
                    X12SegmentSpec("CRC", "S", 3, _elemSpec1("E1", "E2", "E3")),
                    X12SegmentSpec("CRC", "S", 1, _elemSpec1("75")),
                    X12SegmentSpec("CRC", "S", 1, _elemSpec1("75")),
                    X12SegmentSpec("HI", "S"),
                    X12SegmentSpec("HCP", "S"),

                    # loop 2305 - Home health care plan information
                    X12LoopSpec("2305", 6,
                      [ X12SegmentSpec("CR7", "S"),
                        X12SegmentSpec("HSD", "S", 3) ]),

                    # loop 2310A - Referring provider name
                    X12LoopSpec("2310A", 2,
                      [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DN", "P3")),
                        X12SegmentSpec("PRV", "S"),
                        X12SegmentSpec("N2", "S"),
                        X12SegmentSpec("REF", "S", 5) ]),

                    # loop 2310B - Rendering provider name
                    X12LoopSpec("2310B", 1,
                      [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("82")),
                        X12SegmentSpec("PRV"),
                        X12SegmentSpec("N2", "S"),
                        X12SegmentSpec("REF", "S", 5) ]),

                    # loop 2310C - Purchased service provider
                    X12LoopSpec("2310C", 1,
                      [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("QB")),
                        X12SegmentSpec("REF", "S", 5) ]),

                    # loop 2310D - Service facility location
                    X12LoopSpec("2310D", 1,
                      [ X12SegmentSpec("NM1", "S", 1, _SVC_FAC_NM1_ES),
                        X12SegmentSpec("N2", "S"),
                        X12SegmentSpec("N3"),
                        X12SegmentSpec("N4"),
                        X12SegmentSpec("REF", "S", 5) ]),

                    # loop 2310E - Supervising provider name
                    X12LoopSpec("2310E", 1,
                      [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DQ")),
                        X12SegmentSpec("N2", "S"),
                        X12SegmentSpec("REF", "S", 5) ]),

                    # loop 2320 - Other subscriber information
                    X12LoopSpec("2320", 10,
                      [ X12SegmentSpec("SBR", "S"),
                        X12SegmentSpec("CAS", "S", 5),
                        X12SegmentSpec("AMT", "S", 10), # TODO expand this
                        X12SegmentSpec("DMG", "S", 1),
                        X12SegmentSpec("OI"),
                        X12SegmentSpec("MOA", "S"),

                        # loop 2330A - Other subscriber name
                        X12LoopSpec("2330A", 1,
                          [ X12SegmentSpec("NM1"),
                            X12SegmentSpec("N2", "S"),
                            X12SegmentSpec("N3", "S"),
                            X12SegmentSpec("N4", "S"),
                            X12SegmentSpec("REF", "S", 3) ]),

                        # loop 2330B - Other payer name
                        X12LoopSpec("2330B", 1,
                          [ X12SegmentSpec("NM1"),
                            X12SegmentSpec("N2", "S"),
                            X12SegmentSpec("PER", "S"),
                            X12SegmentSpec("DTP", "S"),
                            X12SegmentSpec("REF", "S", 6) ]), # TODO expand this

                        # loop 2330C - Other payer patient information
                        X12LoopSpec("2330C", 1,
                          [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("QC")),
                            X12SegmentSpec("REF", "S", 3) ]),

                        # loop 2330D - Other payer referring provider
                        X12LoopSpec("23230D", 2,
                          [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DN", "P3")),
                            X12SegmentSpec("REF", "R", 3) ]),

                        # loop 2330E - Other paye rendering provider
                        X12LoopSpec("2330E", 1,
                          [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("82")),
                            X12SegmentSpec("REF", "R", 3) ]),

                        # loop 2330F - Other payer purchased service provider
                        X12LoopSpec("2330F", 1,
                          [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("QB")),
                            X12SegmentSpec("REF", "R", 3) ]),

                        # loop 2330G - Other payer purchased service provider
                        X12LoopSpec("2330G", 1,
                          [ X12SegmentSpec("NM1", "S", 1, _SVC_FAC_NM1_ES),
                            X12SegmentSpec("REF", "R", 3) ]),

                        # loop 2330H - Other payer purchased service provider
                        X12LoopSpec("2330H", 1,
                          [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DQ")),
                            X12SegmentSpec("REF", "R", 3) ]),
                      ]),

                      # loop 2400 - Service line
                      X12LoopSpec("2400", 50,
                        [ X12SegmentSpec("LX"),
                          X12SegmentSpec("SV1"),
                          X12SegmentSpec("SV4", "S"), # removed in A1
                          X12SegmentSpec("SV5", "S"),
                          X12SegmentSpec("PWK", "S"),
                          X12SegmentSpec("CR1", "S"),
                          X12SegmentSpec("CR2", "S"),
                          X12SegmentSpec("CR3", "S"),
                          X12SegmentSpec("CR5", "S"),
                          X12SegmentSpec("CRC", "S", 6), # TODO expand this
                          X12SegmentSpec("DTP"),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("607")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("330")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("463")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("461")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("938")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("304")),
                          X12SegmentSpec("DTP", "S", 2, _elemSpec1("738", "739")),
                          X12SegmentSpec("DTP", "S", 3, _elemSpec1("119", "480", "481")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("011")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("431")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("455")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("453")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("454")),
                          X12SegmentSpec("DTP", "S", 1, _elemSpec1("438")),
                          X12SegmentSpec("QTY", "S", 5),
                          X12SegmentSpec("MEA", "S", 20),
                          X12SegmentSpec("CN1", "S"),
                          X12SegmentSpec("REF", "S", 15), # TODO expand this
                          X12SegmentSpec("AMT", "S", 3), # TODO expand this
                          X12SegmentSpec("K3", "S", 10),
                          X12SegmentSpec("NTE", "S"),
                          X12SegmentSpec("PS1", "S"),
                          X12SegmentSpec("HSD", "S"),
                          X12SegmentSpec("HCP", "S"),

                          # loop 2410 - Drug identification
                          X12LoopSpec("2410", 25,
                            [ X12SegmentSpec("LIN", "S"),
                              X12SegmentSpec("CTP", "S"),
                              X12SegmentSpec("REF", "S") ]),

                          # loop 2420A - Rendering provider name
                          X12LoopSpec("2420A", 1,
                            [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("82")),
                              X12SegmentSpec("PRV"),
                              X12SegmentSpec("N2", "S"),
                              X12SegmentSpec("REF", "S", 5) ]),

                          # loop 2420B - Purchased service provider
                          X12LoopSpec("2420B", 1,
                            [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("QB")),
                              X12SegmentSpec("REF", "S", 5) ]),

                          # loop 2420C - Service facility location
                          X12LoopSpec("2420C", 1,
                            [ X12SegmentSpec("NM1", "S", 1, _SVC_FAC_NM1_ES),
                              X12SegmentSpec("N2", "S"),
                              X12SegmentSpec("N3"),
                              X12SegmentSpec("N4"),
                              X12SegmentSpec("REF", "S", 5) ]),

                          # loop 2420D - Supervising provider name
                          X12LoopSpec("2420D", 1,
                            [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DQ")),
                              X12SegmentSpec("N2", "S"),
                              X12SegmentSpec("REF", "S", 5) ]),

                          # loop 2420E - Ordering provider name
                          X12LoopSpec("2420E", 1,
                            [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("DK")),
                              X12SegmentSpec("N2", "S"),
                              X12SegmentSpec("N3", "S"),
                              X12SegmentSpec("N4", "S"),
                              X12SegmentSpec("REF", "S", 5),
                              X12SegmentSpec("PER", "S") ]),

                          # loop 2420F - Referring provider name
                          X12LoopSpec("2420F", 2,
                            [ X12SegmentSpec("NM1", "S", 1, 
                                _elemSpec1("DN", "P3")),
                              X12SegmentSpec("PRV", "S"),
                              X12SegmentSpec("N2", "S"),
                              X12SegmentSpec("REF", "S", 5) ]),

                          # loop 2420G - Other payer prior authorization or 
                          #              referral number
                          X12LoopSpec("2420G", 4,
                            [ X12SegmentSpec("NM1", "S", 1, _elemSpec1("PR")),
                              X12SegmentSpec("REF", "R", 2) ]),

                          # loop 2430 - Line adjudication information
                          X12LoopSpec("2430", 25,
                            [ X12SegmentSpec("SVD", "S"),
                              X12SegmentSpec("CAS", "S", 99),
                              X12SegmentSpec("DTP") ]),

                          # loop 2440 - Form identification code
                          X12LoopSpec("2440", 5,
                            [ X12SegmentSpec("LQ", "S"),
                              X12SegmentSpec("FRM", "R", 99) ])
                        ])
                  ])
              ])
          ]),

          X12SegmentSpec("SE")
      ]
    __ansi837_spec = X12LoopSpec("0", 1, loop0_specs)
    return __ansi837_spec

def parse837p(file_obj):
    return X12Document(file_obj, getX12Spec837p())

def isFileAnsi837p(file_obj):
    try:
        a = parse837p(file_obj)
    except X12ParseError:
        return False
    return True

__facility_codes = { \
        '11' : 'Office',
        '12' : 'Home',
        '21' : 'Inpatient Hospital',
        '22' : 'Outpatient Hospital',
        '23' : 'Emergency Room - Hospital',
        '24' : 'Ambulatory Surgical Center',
        '25' : 'Birthing Center',
        '26' : 'Military Treatment Facility',
        '31' : 'Skilled Nursing Facility',
        '32' : 'Nursing Facility',
        '33' : 'Custodial Care Facility',
        '34' : 'Hospice',
        '41' : 'Ambulance - Land',
        '42' : 'Ambulance - Air or Water',
        '51' : 'Inpatient Psychiatric Facility',
        '52' : 'Psychiatric Facility Partial Hospitalization',
        '53' : 'Community Mental Health Center',
        '54' : 'Intermediate Care Facility/Mentally Retarded',
        '55' : 'Residential Substance Abuse Treatment Facility',
        '56' : 'Psychiatric Residential Treatment Center',
        '50' : 'Federally Qualified Health Center',
        '60' : 'Mass Immunization Center',
        '61' : 'Comprehensive Inpatient Rehabilitation Facility',
        '62' : 'Comprehensive Outpatient Rehabilitation Facility',
        '65' : 'End Stage Renal Disease Treatment Facility',
        '71' : 'State or Local Public Health Clinic',
        '72' : 'Rural Health Clinic',
        '81' : 'Independent Laboratory',
        '99' : 'Other Unlisted Facility',
}

def facilityCodeToStr(code):
    return __facility_codes[code]

def usage():
    usage_str="""usage:  ansi837p.py [options] <filename>

    filename should be an ASC X12N 837p (004010X091) file

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
    f = file(fname, 'r')
    try:
        a = parse837p(f)
        a.dump()
    except ValueError, e:
        print "file does not appear to be an ANSI 837 file!"
        traceback.print_exc()
        sys.exit(1)

#    print "DATE: %s TIME: %s" % (a.date, a.time)
#    print
#    for v in a.rawtext.values():
#        print v
#    print 
#    for claim in a.claims:
#        print claim.prettyStr()
