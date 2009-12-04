import sys
from decimal import *

import x12
import ansi837p

if len(sys.argv) < 2:
    sys.stderr.write("usage: show_837_claims <ansi837_file>\n")
    sys.exit(1)

fname = sys.argv[1]
f = file(fname, 'r')
doc = ansi837p.parse837p(f)

print "ANSI837P"
print "ISA ICN:  %s" % doc.getInterchangeControlNumber()
print "Date:     %s" % doc.getDocumentDate()
print "Time:     %s" % doc.getDocumentTime()
print "Receiver: %s" % doc.getReceiverID()
print "================"

root = doc.getRootLoop()

for loop2000a in root.getSubLoopsByName("2000A"):
    for loop2000b in loop2000a.getSubLoopsByName("2000B"):

        # find subscriber information
        loop2010ba = loop2000b.getSubLoopsByName("2010BA")[0]
        subscriber_nm1 = loop2010ba.getSegmentsByName("NM1")[0]
        subscriber_lname = subscriber_nm1.getElement(3)
        subscriber_fname = subscriber_nm1.getElement(4)
#        print subscriber_lname, subscriber_fname

        # is the patient not the subscriber?
        loop2000c_list = loop2000b.getSubLoopsByName("2000C")
        if len(loop2000c_list):
            patient_nm1 = loop2000c_list[0].getSegmentsByName("NM1")
        else:
            patient_nm1 = subscriber_nm1

        patient_lname = patient_nm1.getElement(3)
        patient_fname = patient_nm1.getElement(4)

        print "Patient:  %s, %s" % (patient_lname, patient_fname)

        for loop2300 in loop2000b.getSubLoopsByName("2300"):
            # each repeat of loop 2300 corresponds to one claim
            clm = loop2300.getChildren()[0]
            assert clm.isSegment() and clm.getName() == "CLM"
            claim_id = clm.getElement(1)
            claim_amount = Decimal(clm.getElement(2))
            print "  Claim [%s] -- %s" % (claim_id, claim_amount)
            
            for loop2400 in loop2300.getSubLoopsByName("2400"):
                # each repeat of loop 2400 corresponds to one line item

                # service code(s) and amount
                sv1 = loop2400.getSegmentsByName("SV1")[0]
                svc_code = sv1.getSubElement(1, 2)
                line_item_charge = Decimal(sv1.getElement(2))

                svc_dtp = loop2400.getSegmentsByName("DTP")[0]
                svc_date = x12.ccyymmdd2date(svc_dtp.getElement(3))

                # find the LICN if it exists
                ref_list = [ ref for ref in loop2400.getSegmentsByName("REF") \
                        if ref.getElement(1) == "6R" ]
                if len(ref_list):
                    assert len(ref_list) == 1
                    licn_ref = ref_list[0]
                else:
                    licn_ref = None
                    licn = ""

                if licn_ref:
                    licn = licn_ref.getElement(2)

                print "    %s / %s / %6.2f / %s" % (svc_code, svc_date, line_item_charge, licn)
