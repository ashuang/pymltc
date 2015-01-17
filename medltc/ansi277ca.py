"""Parses an ASC X12N Health Care Claim Acknowledgment (277) document.

Specifications document ASC X12N/005010X214 version 5, release 1.
"""

# pylint: disable=too-many-instance-attributes
# pylint: disable=too-few-public-methods
import argparse
import datetime
from decimal import Decimal
import sys
import traceback

from .x12 import ccyymmdd2date, X12Document, X12LoopSpec, X12SegmentSpec, \
        X12ElementEquals, X12ParseError
from . import x12
from . import x12adapters
from . import claim_status_codes
from . import claim_status_category_codes

TWOPLACES = Decimal('0.01')

def hhmmssdd_to_time(hhmm):
    if len(hhmm) < 4 or \
       len(hhmm) == 5 or \
       len(hhmm) > 8:
        raise ValueError("invalid string")
    hour = int(hhmm[0:2])
    minutes = int(hhmm[2:4])
    secs = 0
    microseconds = 0
    if len(hhmm) > 5:
        secs = int(hhmm[4:6])
    if len(hhmm) == 7:
        microseconds = int(hhmm[6:]) * 100000
    if len(hhmm) == 8:
        microseconds = int(hhmm[6:]) * 10000

    if hour < 0 or hour > 23 or \
       minutes < 0 or minutes > 59 or \
       secs < 0 or secs > 59 or \
       microseconds < 0 or microseconds > 1000000:
        raise ValueError("invalid time")

    return datetime.time(hour=hour, minute=minutes, second=secs,
        microsecond=microseconds)

def get_x12_spec_277ca():
    specs = \
      [X12SegmentSpec("ST", "R", 1, [X12ElementEquals(1, "277")]),
        X12SegmentSpec("BHT", "R", 1, [X12ElementEquals(1, "0085"),
                                        X12ElementEquals(2, "08"),
                                        X12ElementEquals(6, "TH")]),

        X12LoopSpec("2000A", 1,
            [X12SegmentSpec("HL", "R", 1, [X12ElementEquals(3, "20")]),

              X12LoopSpec("2100A", 1, [X12SegmentSpec("NM1"),]),

              X12LoopSpec("2200A", 1,
                        [X12SegmentSpec("TRN", "R", 1),
                          X12SegmentSpec("DTP", "R", 1),
                          X12SegmentSpec("DTP", "R", 1)
                       ]),
           ]),

        X12LoopSpec("2000B", 1,
            [X12SegmentSpec("HL", "R", 1, [X12ElementEquals(3, "21")]),

              X12LoopSpec("2100B", 1, [X12SegmentSpec("NM1"),]),

              X12LoopSpec("2200B", 1,
                  [X12SegmentSpec("TRN", "R", 1),
                    X12SegmentSpec("STC", "R", 999999),
                    X12SegmentSpec("QTY", "O", 1),
                    X12SegmentSpec("QTY", "O", 1),
                    X12SegmentSpec("AMT", "O", 1),
                    X12SegmentSpec("AMT", "O", 1),
                 ]),
           ]),

        X12LoopSpec("2000C", 999999,
            [X12SegmentSpec("HL", "O", 1, [X12ElementEquals(3, "19")]),

              X12LoopSpec("2100C", 1, [X12SegmentSpec("NM1"),]),

              X12LoopSpec("2200C", 1,
                  [X12SegmentSpec("TRN", "O", 1),
                    X12SegmentSpec("STC", "O", 999999),
                    X12SegmentSpec("REF", "O", 3),
                    X12SegmentSpec("QTY", "O", 1),
                    X12SegmentSpec("QTY", "O", 1),
                    X12SegmentSpec("AMT", "O", 1),
                    X12SegmentSpec("AMT", "O", 1),
                 ]),
           ]),

        X12LoopSpec("2000D", 999999,
            [X12SegmentSpec("HL", "O", 1, [X12ElementEquals(3, "PT")]),

              X12LoopSpec("2100D", 1, [X12SegmentSpec("NM1"),]),

              X12LoopSpec("2200D_claim_status_tracking_number", 999999,
                  [X12SegmentSpec("TRN", "R", 1),
                    X12SegmentSpec("STC", "R", 999999),
                    X12SegmentSpec("REF", "O", 1),
                    X12SegmentSpec("REF", "O", 1),
                    X12SegmentSpec("REF", "O", 1),
                    X12SegmentSpec("DTP", "R", 1),

                    X12LoopSpec("2200D_service_line_information", 1,
                        [X12SegmentSpec("SVC", "O", 1),
                          X12SegmentSpec("STC", "R", 999999),
                          X12SegmentSpec("REF", "R", 1),
                          X12SegmentSpec("REF", "S", 1),
                          X12SegmentSpec("DTP", "S", 1)
                       ]),
                 ]),
           ]),

        X12SegmentSpec("SE", "R", 1)]

    return X12LoopSpec("0", 1, specs)

def parse_x12_doc(file_object):
    return X12Document(file_object, get_x12_spec_277ca())

def is_file_ansi_277ca(file_object):
    try:
        parse_x12_doc(file_object)
    except X12ParseError:
        return False
    return True

class HealthCareClaimStatus(object):
    """Represents STC01, STC10, STC11"""
    def __init__(self, stc_segment, element_index):
        # health care claim status category code
        self.category_code = stc_segment.getSubElement(element_index, 1)
        self.industry_code = stc_segment.getSubElement(element_index, 2)
        if stc_segment.numSubElements(1) > 2:
            self.entity_identifier_code = \
                stc_segment.getSubElement(element_index, 3)
        else:
            self.entity_identifier_code = None

    def category_code_str(self):
        return claim_status_category_codes.code_to_str(self.category_code)

    def industry_code_str(self):
        return claim_status_codes.code_to_str(self.industry_code)

    def entity_code_str(self):
        return {"36" : "Employer",
                "40" : "Receiver",
                "41" : "Submitter",
                "AY" : "Clearinghouse",
                "PR" : "Payer"}[self.entity_identifier_code]

    def __str__(self):
        result = "category_code: %s, industry code: %s" % (self.category_code,
            self.industry_code)
        if self.entity_identifier_code:
            result += ", entity id: %s" % self.entity_identifier_code
        return result

class StatusInformation(object):
    """Describes an STC segment"""
    def __init__(self, stc_segment):
        self.statuses = [HealthCareClaimStatus(stc_segment, 1)]
        if stc_segment.numElements() >= 10 and len(stc_segment.getElement(10)):
            self.statuses.append(HealthCareClaimStatus(stc_segment, 10))
        if stc_segment.numElements() >= 11 and len(stc_segment.getElement(11)):
            self.statuses.append(HealthCareClaimStatus(stc_segment, 11))
        datestr = stc_segment.getElement(2).strip()
        if datestr:
            self.date = ccyymmdd2date(datestr)
        else:
            self.date = None
        self.action_code = stc_segment.getElement(3)
        if stc_segment.numElements() >= 4:
            self.monetary_amount = stc_segment.getElement(4)
        else:
            self.monetary_amount = 0

    def get_monetary_amount(self):
        return self.monetary_amount

    def is_accepted(self):
        return self.action_code == "WQ"

    def get_statuses(self):
        return self.statuses

    def __str__(self):
        lines = ["date: %s" % self.date,
                "action code: %s" % self.action_code,
                "monetary amount: %s" % self.monetary_amount]
        for status in self.statuses:
            lines.append("claim status: %s" % str(status))
        return "\n".join(["  %s" % line for line in lines])

class InformationSource(object):
    def __init__(self, loop):
        self.hl_id = None
        self.parent_hl_id = None

        self.nm1 = None
        self.reference_id = None
        self.received_date = None
        self.processed_date = None

        for child in loop.getChildren():
            if child.isSegment():
                assert child.getName() == "HL"
                self.hl_id = child.getElement(1)
                self.parent_hl_id = child.getElement(2)
                continue

            assert child.isLoop()
            if child.getLoopName() == "2100A":
                grandchildren = child.getChildren()
                assert len(grandchildren) == 1 and \
                    grandchildren[0].getName() == "NM1"
                self.nm1 = x12adapters.NM1(grandchildren[0])
            elif child.getLoopName() == "2200A":
                for grandchild in child.getChildren():
                    assert grandchild.isSegment()
                    if grandchild.getName() == "TRN":
                        self.reference_id = grandchild.getElement(2)
                    elif grandchild.getName() == "DTP" and \
                            grandchild.getElement(1) == "050":
                        self.received_date = \
                            x12adapters.DTP(grandchild).date
                    elif grandchild.getName() == "DTP" and \
                            grandchild.getElement(1) == "009":
                        self.processed_date = \
                            x12adapters.DTP(grandchild).date

    def dump(self):
        print "Information source:"
        print "  name: %s" % self.nm1.nameAsStr()
        print "  reference id: %s" % self.reference_id
        print "  received: %s" % self.received_date
        print "  processed: %s" % self.processed_date


class LineItemDetail(object):
    def __init__(self, loop):
        self.status = None
        self.ident = None
        self.pharmacy_prescription_number = None
        self.date = None

        self.procedure_code_qualifier = None
        self.procedure_code = None
        self.procedure_modifiers = []
        self.monetary_amount = 0

        for child in loop.getChildren():
            assert child.isSegment()
            if child.getName() == "SVC":
                self.procedure_code_qualifier = child.getSubElement(1, 1)
                self.procedure_code = child.getSubElement(1, 2)
                for offset in xrange(3):
                    if child.numSubElements(1) >= 3 + offset:
                        self.procedure_modifiers = \
                                child.getSubElement(1, 3 + offset)
                self.monetary_amount = \
                        Decimal(child.getElement(2)).quantize(TWOPLACES)
            elif child.getName() == "STC":
                self.status = StatusInformation(child)
            elif child.getName() == "REF" and \
                    child.getElement(1) == "FJ":
                self.ident = \
                        x12adapters.ReferenceInformation(child)
            elif child.getName() == "REF" and \
                    child.getElement(1) == "XZ":
                self.pharmacy_prescription_number = \
                        x12adapters.ReferenceInformation(child)
            elif child.getName() == "DTP":
                self.date = x12adapters.DTP(child)

    def dump(self):
        print "      %s" % str(self.ident)
        print "      date: %s" % str(self.date)
        if self.pharmacy_prescription_number:
            print "    pharmacy prescription #: %s" % \
                str(self.pharmacy_prescription_number)
        print "      procedure code: %s / %s" % (self.procedure_code_qualifier,
            self.procedure_code)
        print "      monetary amount: %s" % str(self.monetary_amount)
        print "      %s" % str(self.status)

class PatientClaimDetail(object):
    def __init__(self, loop):
        self.reference_id = None
        self.status = None
        self.payer_claim_contol_number = None
        self.intermediary_id = None
        self.institutional_bill_type_id = None
        self.service_date = None
        self.line_items = []

        for child in loop.getChildren():
            if child.isSegment():
                if child.getName() == "TRN":
                    self.reference_id = child.getElement(2)
                elif child.getName() == "STC":
                    self.status = StatusInformation(child)
                elif child.getName() == "REF" and \
                        child.getElement(1) == "1K":
                    self.payer_claim_contol_number = \
                            x12adapters.ReferenceInformation(child)
                elif child.getName() == "REF" and \
                        child.getElement(1) == "D9":
                    self.intermediary_id = \
                            x12adapters.ReferenceInformation(child)
                elif child.getName() == "REF" and \
                        child.getElement(1) == "BLT":
                    self.institutional_bill_type_id = \
                            x12adapters.ReferenceInformation(child)
                elif child.getName() == "DTP":
                    self.service_date = x12adapters.DTP(child)
            elif child.isLoop():
                assert child.getLoopName() == "2200D_service_line_information"
                self.line_items.append(LineItemDetail(child))

    def get_status(self):
        return self.status

    def dump(self):
        print "  claim:"
        print "  reference id: %s" % self.reference_id
        print "  status:\n%s" % str(self.status)
        if len(self.line_items):
            print "  line items:"
            for line_item in self.line_items:
                line_item.dump()

class PatientDetail(object):
    def __init__(self, loop):
        self.hl_id = None
        self.parent_hl_id = None
        self.nm1 = None

        self.claims = []

        for child in loop.getChildren():
            if child.isSegment():
                assert child.getName() == "HL" and child.getElement(3) == "PT"
                self.hl_id = child.getElement(1)
                self.parent_hl_id = child.getElement(2)
                continue

            assert child.isLoop()
            if child.getLoopName() == "2100D":
                grandchildren = child.getChildren()
                assert len(grandchildren) == 1 and \
                    grandchildren[0].getName() == "NM1"
                self.nm1 = x12adapters.NM1(grandchildren[0])
            elif child.getLoopName() == "2200D_claim_status_tracking_number":
                self.claims.append(PatientClaimDetail(child))

    def has_rejections(self):
        for claim in self.claims:
            if not claim.get_status().is_accepted():
                return True
        return False

    def get_claims(self):
        return self.claims

    def dump(self):
        print "Patient detail"
        print "  name: %s" % self.nm1.nameAsStr()
        for claim in self.claims:
            claim.dump()

class BillingProviderDetail(object):
    def __init__(self, loop):
        self.hl_id = None
        self.nm1 = None

        self.reference_id = None
        self.status = None
        self.secondary_id = None

        self.accepted_num = 0
        self.accepted_amt = 0
        self.rejected_num = 0
        self.rejected_amt = 0

        self.patient_details = []

        for child in loop.getChildren():
            if child.isSegment():
                assert child.getName() == "HL" and child.getElement(3) == "19"
                self.hl_id = child.getElement(1)
                self.parent_hl_id = child.getElement(2)
                continue

            assert child.isLoop()
            if child.getLoopName() == "2100C":
                grandchildren = child.getChildren()
                assert len(grandchildren) == 1 and \
                    grandchildren[0].getName() == "NM1"
                self.nm1 = x12adapters.NM1(grandchildren[0])
            elif child.getLoopName() == "2200C":
                for grandchild in child.getChildren():
                    assert grandchild.isSegment()
                    if grandchild.getName() == "TRN":
                        self.reference_id = grandchild.getElement(2)
                    elif grandchild.getName() == "STC":
                        self.status = StatusInformation(grandchild)
                    elif grandchild.getName() == "REF":
                        self.secondary_id = \
                                x12adapters.ReferenceInformation(grandchild)
                    elif grandchild.getName() == "QTY" and \
                            grandchild.getElement(1) == "QA":
                        elem_2 = grandchild.getElement(2)
                        self.accepted_num = int(elem_2)
                    elif grandchild.getName() == "QTY" and \
                            grandchild.getElement(1) == "QC":
                        elem_2 = grandchild.getElement(2)
                        self.rejected_num = int(elem_2)
                    elif grandchild.getName() == "AMT" and \
                            grandchild.getElement(1) == "YU":
                        elem_2 = grandchild.getElement(2)
                        self.accepted_amt = Decimal(elem_2).quantize(TWOPLACES)
                    elif grandchild.getName() == "AMT" and \
                            grandchild.getElement(1) == "YY":
                        elem_2 = grandchild.getElement(2)
                        self.rejected_amt = Decimal(elem_2).quantize(TWOPLACES)

    def add_patient_detail(self, patient_detail):
        self.patient_details.append(patient_detail)

    def get_patient_details(self):
        return self.patient_details

    def has_rejections(self):
        for patient_detail in self.patient_details:
            if patient_detail.has_rejections():
                return True
        return False

    def get_nm1(self):
        return self.nm1

    def dump(self):
        print "Billing provider"
        print "  name: %s" % self.nm1.nameAsStr()
        print "  reference id: %s" % self.reference_id
        if self.secondary_id:
            print "  secondary id: %s" % str(self.secondary_id)
        print "  accepted: %s (%s)" % (self.accepted_num, self.accepted_amt)
        print "  rejected: %s (%s)" % (self.rejected_num, self.rejected_amt)
#        print "  status:\n%s" % str(self.status)

        if self.patient_details:
            print "  Patients:"
            for patient_detail in self.patient_details:
                patient_detail.dump()

class InformationReceiver(object):
    def __init__(self, loop):
        self.hl_id = None
        self.parent_hl_id = None

        self.nm1 = None
        self.reference_id = None

        self.status = None

        self.accepted_num = 0
        self.rejected_num = 0
        self.accepted_amt = 0
        self.rejected_amt = 0

        for child in loop.getChildren():
            if child.isSegment():
                assert child.getName() == "HL"
                self.hl_id = child.getElement(1)
                self.parent_hl_id = child.getElement(2)
            elif child.isLoop():
                if child.getLoopName() == "2100B":
                    grandchildren = child.getChildren()
                    assert len(grandchildren) == 1 and \
                        grandchildren[0].getName() == "NM1"
                    self.nm1 = x12adapters.NM1(grandchildren[0])
                elif child.getLoopName() == "2200B":
                    for grandchild in child.getChildren():
                        assert grandchild.isSegment()
                        if grandchild.getName() == "TRN":
                            self.reference_id = grandchild.getElement(2)
                        elif grandchild.getName() == "STC":
                            self.status = StatusInformation(grandchild)
                        elif grandchild.getName() == "QTY" and \
                                grandchild.getElement(1) == "90":
                            elem_2 = grandchild.getElement(2)
                            self.accepted_num = int(elem_2)
                        elif grandchild.getName() == "QTY" and \
                                grandchild.getElement(1) == "AA":
                            elem_2 = grandchild.getElement(2)
                            self.rejected_num = int(elem_2)
                        elif grandchild.getName() == "AMT" and \
                                grandchild.getElement(1) == "YU":
                            elem_2 = grandchild.getElement(2)
                            self.accepted_amt = \
                                    Decimal(elem_2).quantize(TWOPLACES)
                        elif grandchild.getName() == "AMT" and \
                                grandchild.getElement(1) == "YY":
                            elem_2 = grandchild.getElement(2)
                            self.rejected_amt = \
                                    Decimal(elem_2).quantize(TWOPLACES)

    def dump(self):
        print "Receiver"
        print "  name: %s" % self.nm1.nameAsStr()
        print "  reference id: %s" % self.reference_id
        print "  claims accepted: %s ($%s)" % (self.accepted_num,
                self.accepted_amt)
        print "  claims rejected: %s ($%s)" % (self.rejected_num,
                self.rejected_amt)

class Ansi277caTransactionSet(object):
    def __init__(self, x12ts):
        root = x12ts.getRootLoop()

        self.reference_id = None
        self.information_source = None
        self.information_receiver = None
        self.billing_providers = []

        for child in root.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "ST":
                    self.control_num = child.getElement(2)
                elif segname == "BHT":
                    self.reference_id = child.getElement(3)
                    self.ts_create_date = ccyymmdd2date(child.getElement(4))
                    self.ts_create_time = hhmmssdd_to_time(child.getElement(5))
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2000A":
                    self.information_source = InformationSource(child)
                elif loopname == "2000B":
                    self.information_receiver = \
                        InformationReceiver(child)
                elif loopname == "2000C":
                    self.billing_providers.append(BillingProviderDetail(child))
                elif loopname == "2000D":
                    patient_detail = PatientDetail(child)
                    for provider in self.billing_providers:
                        if provider.hl_id == patient_detail.parent_hl_id:
                            provider.add_patient_detail(patient_detail)

    def has_rejections(self):
        for provider in self.billing_providers:
            if provider.has_rejections():
                return True
        return False

    def dump(self):
        print "Claim acknowledgment. Original claim:"
        print "  reference id: %s" % self.reference_id
        print "  claim creation date: %s" % self.ts_create_date
        print "  claim creation time: %s" % self.ts_create_time
        self.information_source.dump()
        self.information_receiver.dump()
        for provider in self.billing_providers:
            provider.dump()

class Ansi277caFunctionalGroup(object):
    def __init__(self, x12fg):
        self.transaction_sets = [Ansi277caTransactionSet(tset) for tset in \
                x12fg.getTransactionSets()]

    def dump(self):
        print ""
        for tset in self.transaction_sets:
            tset.dump()

class Ansi277caDocument(object):
    def __init__(self, file_obj):
        x12doc = X12Document(file_obj, get_x12_spec_277ca())

        self.isa_date = x12doc.getDocumentDate()
        self.isa_time = x12doc.getDocumentTime()
        self.isa_sender = x12doc.getSenderID()
        self.isa_sender_type = x12doc.getSenderIDType()
        self.isa_version = x12doc.getControlVersion()

        self.functional_groups = [Ansi277caFunctionalGroup(fgroup) for \
                fgroup in x12doc.getFunctionalGroups()]
        self.x12doc = x12doc

    def dump(self):
        print "ANSI277ca Document Date: %s  %s" % (self.isa_date, self.isa_time)
        print "Sender: %s" % self.isa_sender
        print "Document version: %s" % self.isa_version

        for fgroup in self.functional_groups:
            fgroup.dump()

def _report_patient(patient):
    for claim in patient.get_claims():
        if claim.get_status().is_accepted():
            continue

        print ""
        print "patient: %s" % patient.nm1.nameAsStr()
        print "claim id: %s" % claim.reference_id
        for status in claim.status.get_statuses():
            print "  status: (%s) %s" % (status.category_code,
                    status.category_code_str())
            print "  detail: (%s) / %s" % (status.industry_code,
                    status.industry_code_str())

        for line_item in claim.line_items:
            if not line_item.status.is_accepted():
                print "  line item: %s" % \
                        line_item.ident.identification
                for li_status in line_item.status.get_statuses():
                    print "    status: (%s) %s" % (li_status.category_code,
                            li_status.category_code_str())
                    print "    detail: (%s) %s" % (li_status.industry_code,
                            li_status.industry_code_str())

def text_report(doc):
    print "277CA Document version: %s From: %s Time: %s %s" % (doc.isa_version,
            doc.isa_sender, doc.isa_date, doc.isa_time)

    for fgroup in doc.functional_groups:
        for tset in fgroup.transaction_sets:
            print "  reference id: %s" % tset.reference_id
            print "  837 creation date: %s" % tset.ts_create_date
            print "  837 creation time: %s" % tset.ts_create_time
            tset.information_source.dump()
            tset.information_receiver.dump()
            for provider in tset.billing_providers:
                if not provider.has_rejections():
                    continue

                for patient in provider.get_patient_details():
                    _report_patient(patient)

def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--show-parse', dest='show_parse',
            action='store_true',
            help='Show parsed document')
    arg_parser.add_argument('filename', metavar='filename',
            help='ANSI X12 277CA document filename')
    args = arg_parser.parse_args()

    file_obj = open(args.filename, 'r')

    try:
        a277cadoc = Ansi277caDocument(file_obj)
    except ValueError:
        print "file does not appear to be an ANSI 277ca file!"
        traceback.print_exc()
        sys.exit(1)

    if args.show_parse:
        file_obj.seek(0, 0)
        x12.print_document(parse_x12_doc(file_obj))
        sys.exit(0)

    for fgroup in a277cadoc.functional_groups:
        for tset in fgroup.transaction_sets:
            if tset.has_rejections():
                text_report(a277cadoc)

if __name__ == "__main__":
    main()

#    text_report(a277cadoc)
#
#    if a277cadoc.functional_groups[0].transaction_sets[0] \
#        .information_receiver.rejected_num > 0:
#        sys.exit(1)
