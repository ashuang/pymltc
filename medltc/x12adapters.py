from decimal import Decimal

import x12
import ansi837p
import ansi835
import ansi835codes
import ansi997

class NM1(object):
    def __init__(self, nm1_seg):
        nelem = nm1_seg.numElements()

        self.nm1_code = nm1_seg.getElement(1)
        self.entity_type_code = nm1_seg.getElement(2)
        self.name_last = ""
        self.name_first = ""
        self.name_mid = ""
        self.name_suffix = ""
        self.name_prefix = ""
        self.id_code_type = None
        self.id_code = None
        if nelem > 2:
            self.name_last = nm1_seg.getElement(3)
        if nelem > 3:
            self.name_first = nm1_seg.getElement(4)
        if nelem > 4:
            self.name_mid = nm1_seg.getElement(5)
        if nelem > 5:
            self.name_suffix = nm1_seg.getElement(6)
        if nelem > 6:
            self.name_prefix = nm1_seg.getElement(7)
        if nelem > 7:
            self.id_code_type = nm1_seg.getElement(8)
        if nelem > 8:
            self.id_code = nm1_seg.getElement(9).strip()

        self.__namestr = ""
        if self.name_prefix:
            self.__namestr = self.name_prefix + " "
        if self.name_last:
            self.__namestr += self.name_last
        if self.name_first:
            self.__namestr += ", " + self.name_first
        if self.name_mid:
            self.__namestr += " " + self.name_mid
        if self.name_suffix:
            self.__namestr += " " + self.name_suffix

    def nameAsStr(self):
        return self.__namestr
        
    def nameAndId(self):
        if self.id_code:
            idstr = "[%s] %s" % (self.id_code_type, self.id_code)
        else:
            idstr = ""

        if self.__namestr and idstr:
            return "%s -- %s" % (self.__namestr, idstr)
        elif self.__namestr and not idstr:
            return self.__namestr
        elif not self.__namestr and idstr:
            return idstr
        else:
            return "[???]"

    def isEmpty(self):
        return not (self.name_last or self.name_first or self.name_mid or self.name_suffix or self.name_prefix or self.id_code)

class NameAndAddress(object):
    def __init__(self, subloop):
        self.entity_code = None
        self.name = None
        self.id_code_type = None
        self.id_code = None
        self.address1 = None
        self.address2 = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.nm1 = None

        self.contact_type = None
        self.contact_name = None
        self.contacts = {}
        self.refcodes = {}

        for child in subloop.getChildren():
            if not child.isSegment():
                continue

            nelem = child.numElements()
            segname = child.getName()
            if segname == "N1":
                self.entity_code = child.getElement(1)
                self.name = child.getElement(2)
                if nelem >= 4:
                    self.id_code = child.getElement(4)
                    self.id_code_type = child.getElement(3) or "XV"
            elif segname == "NM1":
                self.nm1 = NM1(child)
            elif segname == "N3":
                self.address1 = child.getElement(1)
                if nelem >= 2:
                    self.address2 = child.getElement(2)
            elif segname == "N4":
                self.city = child.getElement(1)
                self.state = child.getElement(2)
                self.zip_code = child.getElement(3)
            elif segname == "REF":
                self.refcodes[child.getElement(1)] = child.getElement(2)
            elif segname == "DMG":
                # TODO
                pass
            elif segname == "PER":
                self.contact_type = child.getElement(1)
                if nelem >= 2: self.contact_name = child.getElement(2)
                for i in (3, 5, 7):
                    if nelem < i+1:
                        break
                    self.contacts[child.getElement(i)] = child.getElement(i+1)

class DTP(object):
    def __init__(self, dtp_seg):
        self.code = dtp_seg.getElement(1)
        self.format = dtp_seg.getElement(2)
        d = dtp_seg.getElement(3)

        self.date = None
        self.start_date = None
        self.end_date = None

        try:
            if self.format == "D8":
                self.date = medltc.x12.ccyymmdd2date(d)
                self.start_date = self.date
                self.end_date = self.date
            elif self.format == "RD8":
                sd, ed = d.split("-")
                self.start_date = medltc.x12.ccyymmdd2date(sd)
                self.end_date = medltc.x12.ccyymmdd2date(ed)
                self.date = self.start_date
            else:
                raise ValueError("Unrecognized date format [%s]" % self.format)
        except Exception, ex:
            raise ValueError("DTP (pos %d) - Invalid date: %s" % (dtp_seg.st_seg_pos, str(ex)))


class Ansi835Remark(object):
    def __init__(self, lq):
        self.code_list = lq.getElement(1)
        self.code = lq.getElement(2)

    def asStr(self):
        return medltc.ansi835codes.RemarkCodeToStr(self.code_list, self.code)

class Ansi835Adjustment(object):
    def __init__(self, group_code, reason_code, amount, quantity):
        self.group_code = group_code
        self.reason_code = reason_code
        self.amount = amount
        self.quantity = quantity

    def reasonAsStr(self):
        return medltc.ansi835codes.ClaimAdjustmentReasonToStr(self.reason_code)

def _make_835_adjustments(cas):
    results = []
    group_code = cas.getElement(1)
    nadj = cas.numElements() / 3
    for i in range(nadj):
        reason = cas.getElement(2 + i*3)
        try: 
            amount = Decimal(cas.getElement(3 + i*3))
        except: 
            amount = 0
        try: 
            quantity = Decimal(cas.getElement(4 + i*3))
        except: 
            quantity = 0
        results.append(Ansi835Adjustment(group_code, reason, amount, quantity))
    return results

class Ansi835LineItemReport(object):
    def __init__(self, x12loop):

        self.svc_start_date = None
        self.svc_end_date = None
        self.qualifer = None
        self.code = None
        self.charged = None
        self.paid = None
        self.adjustments = []
        self.licn = None
        self.remarks = []

        self.amt_allowed = None

        for seg in x12loop.getChildren():
            if not seg.isSegment():
                continue
            segname = seg.getName()
            if segname == "SVC":
                self.qualifier = seg.getSubElement(1, 1)
                self.code = seg.getSubElement(1, 2)
                self.charged = Decimal(seg.getElement(2))
                self.paid = Decimal(seg.getElement(3))
            elif segname == "DTM":
                dval = medltc.x12.ccyymmdd2date(seg.getElement(2))
                dtype = seg.getElement(1)
                if dtype == "150":
                    self.svc_start_date = dval
                elif dtype == "151":
                    self.svc_end_date = dval
                else:
                    self.svc_start_date = dval
                    self.svc_end_date = dval
            elif segname == "CAS":
                self.adjustments.extend(_make_835_adjustments(seg))
            elif segname == "REF":
                ref_qualifier = seg.getElement(1)
                if ref_qualifier == "6R":
                    self.licn = seg.getElement(2)
                elif ref_qualifier in [ "1A", "1B", "1C", "1D", "1G", "1H", "1J", "HPI", "SY", "TJ" ]:
                    # TODO
                    pass
                else:
                    # TODO
                    pass
            elif segname == "AMT":
                amt_code = seg.getElement(1)
                amt_val = Decimal(seg.getElement(2))
                if amt_code == "B6":
                    self.amt_allowed = amt_val
                # TODO
            elif segname == "QTY":
                # TODO
                pass
            elif segname == "LQ":
                self.remarks.append(Ansi835Remark(seg))

class Ansi835ClaimReport(object):
    def __init__(self, x12loop, index_835):
        self.index_835 = index_835
        self.line_item_reports = []

        self.claim_id = None
        self.clp_status_code = None
        self.charged = 0
        self.paid = 0
        self.patient_responsible = 0

        self.patient = None
        self.insured = None
        self.corrected = None
        self.provider = None
        self.xover = None
        self.priority_payer = None

        self.expire_date = None
        self.received_date = None
        self.claim_period_start = None
        self.claim_period_end = None

        self.amt_allowed = None


        self.refcodes = {}

        self.adjustments = []

        for child in x12loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "CLP":
                    self.claim_id = child.getElement(1)
                    self.clp_status_code = child.getElement(2)
                    self.charged = Decimal(child.getElement(3))
                    self.paid = Decimal(child.getElement(4))

                    if child.getElement(5):
                        self.patient_responsible = Decimal(child.getElement(5))
                elif segname == "CAS":
                    self.adjustments.extend(_make_835_adjustments(cas))

                elif segname == "NM1":
                    nm1_type = child.getElement(1)
                    if nm1_type == "QC":
                        self.patient = NM1(child)
                    elif nm1_type == "IL":
                        self.insured = NM1(child)
                    elif nm1_type == "74":
                        self.corrected = NM1(child)
                        if self.corrected.isEmpty():
                            self.corrected = None
                    elif nm1_type == "82":
                        self.provider = NM1(child)
                    elif nm1_type == "TT":
                        self.xover = NM1(child)
                    elif nm1_type == "PR":
                        self.priority_payer = NM1(child)
                elif segname == "MIA":
                    # TODO inpatient adjudication information
                    pass
                elif segname == "MOA":
                    # TODO outpatient adjudication information
                    pass
                elif segname == "REF":
                    # other claim related information, rendering provider information
                    self.refcodes[child.getElement(1)] = child.getElement(2)
                elif segname == "DTM":
                    dtm_type = child.getElement(1)
                    dtm_val = medltc.x12.ccyymmdd2date(child.getElement(2))
                    if dtm_type == "036": # expiration
                        self.expire_date = dtm_val
                    elif dtm_type == "050": # received
                        self.received_date = dtm_val
                    elif dtm_type == "232": # claim period start
                        self.claim_period_start = dtm_val
                    elif dtm_type == "233": # claim period end
                        self.claim_period_end = dtm_val
                elif segname == "PER":
                    # TODO claim contact information
                    pass
                elif segname == "AMT":
                    amt_code = child.getElement(1)
                    amt_val = Decimal(child.getElement(2))
                    if amt_code == "B6":
                        self.amt_allowed = amt_val
                    # TODO claim supplemental information
                elif segname == "QTY":
                    # TODO claim supplemental information
                    pass
                else:
                    # TODO unrecognized segment
                    pass
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2110":
                    lir = Ansi835LineItemReport(child)
                    self.line_item_reports.append(lir)
                else:
                    # TODO
                    pass

    def statusAsStr(self):
        return medltc.ansi835codes.CLPStatusCodeToStr(self.clp_status_code)

class Ansi835Loop2000(object):
    def __init__(self, x12loop, first_report_index):
        self.claim_reports = []
        self.num_reports = 0
        for sl in x12loop.getSubLoopsByName("2100"):
            acr = Ansi835ClaimReport(sl, first_report_index + self.num_reports)
            self.claim_reports.append(acr)
            self.num_reports += 1

class Ansi835TransactionSet(object):
    def __init__(self, x12ts, first_report_index):
        rl = x12ts.getRootLoop()

        self.control_number = None
        self.handling_code = None
        self.amount = None
        self.credit_debit = None
        self.payment_method = None
        self.payment_date = None
        self.payer = None
        self.payee = None

        self.num_reports = 0

        self.eft_trace_number = None
        self.trn_payer_id = None

        self.currency_code = None

        self.receiver_id = None

        self.production_date = None

        self.loop2000s = []

        for child in rl.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "ST":
                    self.control_number = child.getElement(2)
                elif segname == "BPR":
                    self.handling_code = child.getElement(1)
                    self.amount = Decimal(child.getElement(2))
                    self.credit_debit = child.getElement(3)
                    self.payment_method = child.getElement(4)
                    self.payment_date = child.getElement(16)
                elif segname == "TRN":
                    self.eft_trace_number = child.getElement(2)
                    self.trn_payer_id = child.getElement(3)
                elif segname == "CUR":
                    self.currency_code = child.getElement(2)
                elif segname == "REF":
                    ref_qualifier = child.getElement(1)
                    ref_val = child.getElement(2)
                    if ref_qualifier == "EV":
                        self.receiver_id = ref_val.strip()
                    # TODO "F2"
                elif segname == "DTM":
                    dval = medltc.x12.ccyymmdd2date(child.getElement(2))
                    if child.getElement(1) == "405":
                        self.production_date = dval
                elif segname == "PLB":
                    # TODO
                    pass
                elif segname == "SE":
                    pass
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "1000A":
                    self.payer = NameAndAddress(child)
                elif loopname == "1000B":
                    self.payee = NameAndAddress(child)
                if loopname == "2000":
                    loop2k = Ansi835Loop2000(child, self.num_reports + first_report_index)
                    self.loop2000s.append(loop2k)
                    self.num_reports += loop2k.num_reports

class Ansi835FunctionalGroup(object):
    def __init__(self, x12fg, first_report_index):
        self.num_reports = 0
        self.transaction_sets = []
        for ts in x12fg.getTransactionSets():
            ats = Ansi835TransactionSet(ts, self.num_reports + first_report_index)
            self.transaction_sets.append(ats)
            self.num_reports += ats.num_reports

class Ansi835Document(object):
    def __init__(self, x12doc):
        self.num_reports = 0
        self.functional_groups = []
        for fg in x12doc.getFunctionalGroups():
            afg = Ansi835FunctionalGroup(fg, self.num_reports)
            self.functional_groups.append(afg)
            self.num_reports += afg.num_reports

class Ansi837pServiceLoop(object):
    def __init__(self, loop):
        self.procedure_code_type = None
        self.procedure_code = None
        self.licn = None
        self.charged = None
        self.dates = {}
        self.service_date = None

        self.rendering_provider = None
        self.purchased_service_provider = None
        self.service_facility = None
        self.supervisor = None
        self.ordering_provider = None
        self.referring_provider = None

        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                nelem = child.numElements()
                if segname == "SV1":
                    e1 = child.getElement(1)
                    self.procedure_code_type = e1[0]
                    self.procedure_code = e1[1]
                    self.charged = Decimal(child.getElement(2))
                elif segname == "REF":
                    ref_qualifier = child.getElement(1)
                    ref_val = child.getElement(2)
                    if ref_qualifier == "6R":
                        self.licn = ref_val
                elif segname == "DTP":
                    dtp = DTP(child)
                    self.dates[dtp.code] = dtp
                    if dtp.code == "472":
                        self.service_date = dtp.date
                # TODO
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2420A":
                    self.rendering_provider = NameAndAddress(child)
                elif loopname == "2420B":
                    self.purchased_service_provider = NameAndAddress(child)
                elif loopname == "2420C":
                    self.service_facility = NameAndAddress(child)
                elif loopname == "2420D":
                    self.supervisor = NameAndAddress(child)
                elif loopname == "2420E":
                    self.ordering_provider = NameAndAddress(child)
                elif loopname == "2420F":
                    self.referring_provider = NameAndAddress(child)
                # TODO

class Ansi837pDiagnosis(object):
    def __init__(self, code_list_code, code):
        self.code_list_code = code_list_code
        self.code = code

    def name(self):
        return "TODO"

class Ansi837pClaimLoop(object):
    def __init__(self, loop, index_837p):
        # index of the claim within the ANSI837p document.
        self.index_837p = index_837p

        self.services = []
        self.claim_id = None
        self.amount = None
        self.facility_code = None
        self.frequency_type_code = None
        self.diagnoses = []

        self.charged = Decimal(0)
        self.dates = {}

        self.referring_provider = None
        self.rendering_provider = None
        self.service_facility = None
        self.supervisor = None
        self.purchased_service_provider = None

        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                nelem = child.numElements()
                if segname == "CLM":
                    self.claim_id = child.getElement(1)
                    self.amount = Decimal(child.getElement(2))

                    e5 = child.getElement(5)
                    self.facility_code = e5[0]
                    self.frequency_type_code = e5[2]

                    # TODO
                    pass
                elif segname == "DTP":
                    dtp = DTP(child)
                    self.dates[dtp.code] = dtp
                elif segname == "PWK":
                    # TODO
                    pass
                elif segname == "CN1":
                    # TODO
                    pass
                elif segname == "AMT":
                    # TODO
                    pass
                elif segname == "REF":
                    # TODO
                    pass
                elif segname == "K3":
                    # TODO
                    pass
                elif segname == "NTE":
                    # TODO
                    pass
                elif segname == "CR1":
                    # TODO
                    pass
                elif segname == "CR2":
                    # TODO
                    pass
                elif segname == "CRC":
                    # TODO
                    pass
                elif segname == "HI":
                    for i in range(nelem):
                        if child.numSubElements(i+1) > 1:
                            e1 = child.getSubElement(i+1, 1)
                            e2 = child.getSubElement(i+1, 2)
                            self.diagnoses.append(Ansi837pDiagnosis(e1, e2))
                elif segname == "HCP":
                    # TODO
                    pass
                # TODO
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2310A":
                    self.referring_provider = NameAndAddress(child)
                elif loopname == "2310B":
                    self.rendering_provider = NameAndAddress(child)
                elif loopname == "2310C":
                    self.purchased_service_provider = NameAndAddress(child)
                elif loopname == "2310D":
                    self.service_facility = NameAndAddress(child)
                elif loopname == "2310E":
                    self.supervisor = NameAndAddress(child)
                elif loopname == "2320":
                    # TODO
                    pass
                elif loopname == "2400":
                    sloop = Ansi837pServiceLoop(child)
                    self.services.append(sloop)
                    self.charged += sloop.charged

    def facilityCodeAsStr(self):
        return medltc.ansi837p.facilityCodeToStr(self.facility_code)

class Ansi837pSubscriberLoop(object):
    def __init__(self, loop, first_claim_index):

        self.claims = []

        self.subscriber = None
        self.payer = None
        self.responsible_party = None
        self.card_holder = None

        self.patient_hl = None
        self.patient_pat = None
        self.patient = None

        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "HL":
                    # TODO
                    pass
                elif segname == "SBR":
                    # TODO
                    pass
                elif segname == "PAT":
                    # TODO
                    pass
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2010BA":
                    self.subscriber = NameAndAddress(child)
                elif loopname == "2010BB":
                    self.payer = NameAndAddress(child)
                elif loopname == "2010BC":
                    self.responsible_party = NameAndAddress(child)
                elif loopname == "2010BD":
                    self.card_holder = NameAndAddress(child)
                elif loopname == "2000C":
#                    self.patient_loop = Ansi837pPatientLoop(child)
                    for child2 in loop.getChildren():
                        if child2.isSegment():
                            segname2 = child2.getName()
                            if segname2 == "HL":
                                # TODO HL
                                pass
#                                self.patient_hl = child
                            elif segname == "PAT":
                                # TODO
                                pass
#                                self.patient_pat = child
                        elif child2.isLoop():
                            if child2.getLoopName() == "2010CA":
                                self.patient = NameAndAddress(child)
                elif loopname == "2300":
                    claim_index = first_claim_index + len(self.claims)
                    self.claims.append(Ansi837pClaimLoop(child, claim_index))

        if self.patient is None:
            self.patient = self.subscriber
                # TODO HL, PAT
#                self.patient_hl = self.subscriber_hl
#                self.patient_pat = self.subscriber_pat

class Ansi837pTransactionSet(object):
    def __init__(self, x12ts, first_claim_index):
        rl = x12ts.getRootLoop()
        self.control_number = None

        self.submitter = None
        self.receiver = None
        self.billing_provider = None
        self.pay_to_provider = None

        self.subscriber_loops = []
        self.num_claims = 0
        self.first_claim_index = first_claim_index
        self.total_charged = Decimal(0)

        for child in rl.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "ST":
                    self.control_number = child.getElement(2)
                elif segname == "BHT":
                    # TODO
                    pass
                elif segname == "REF":
                    # TODO
                    pass
                elif segname == "SE":
                    # TODO
                    pass
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "1000A":
                    self.submitter = NameAndAddress(child)
                elif loopname == "1000B":
                    self.receiver = NameAndAddress(child)
                elif loopname == "2000A":
                    self.__parse_2000a(child)

    def __parse_2000a(self, loop):
        for child in loop.getChildren():
            if child.isSegment():
                segname = child.getName()
                if segname == "HL":
                    # TODO
                    pass
                elif segname == "PRV":
                    # TODO
                    pass
                elif segname == "CUR":
                    # TODO
                    pass
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "2010AA":
                    self.billing_provider = NameAndAddress(child)
                elif loopname == "2010AB":
                    self.pay_to_provider = NameAndAddress(child)
                elif loopname == "2000B":
                    sloop = Ansi837pSubscriberLoop(child, self.num_claims + self.first_claim_index)
                    self.subscriber_loops.append(sloop)
                    self.num_claims += len(sloop.claims)
                    for claim in sloop.claims:
                        self.total_charged += claim.charged
    
class Ansi837pFunctionalGroup(object):
    def __init__(self, x12fg, first_claim_index):
        self.gcn = x12fg.gcn
        self.num_claims = 0
        self.transaction_sets = []
        for ts in x12fg.getTransactionSets():
            ats = Ansi837pTransactionSet(ts, first_claim_index + self.num_claims)
            self.transaction_sets.append(ats)
            self.num_claims += ats.num_claims

class Ansi837pDocument(object):
    def __init__(self, x12doc):
        self.num_claims = 0
        self.functional_groups = []
        for fg in x12doc.getFunctionalGroups():
            afg = Ansi837pFunctionalGroup(fg, self.num_claims)
            self.functional_groups.append(afg)
            self.num_claims += afg.num_claims

class Ansi997DataElementNote(object):
    def __init__(self, ak4_seg):
        if ak4_seg.numSubElements(1) > 1:
            self.pos = ak4_seg.getSubElement(1, 1)
            self.comp_pos = ak4_seg.getSubElement(1, 2)
        else:
            self.pos = ak4_seg.getElement(1)
            self.comp_pos = None
        
        self.ref_num = ak4_seg.getElement(2)
        self.err_code = ak4_seg.getElement(3)
        self.err_code_str = medltc.ansi997.elementSyntaxCodeToStr(self.err_code)
        if ak4_seg.numElements() >= 4:
            self.bad_elem = ak4_seg.getElement(4)
        else:
            self.bad_elem = None

class Ansi997DataSegmentNote(object):
    def __init__(self, loop):

        self.seg_id_code = None
        self.seg_pos = None
        self.loop_id_code = ""
        self.seg_err_code = None
        self.seg_err_code_str = ""
        self.data_element_notes = []

        for child in loop.getChildren():
            if not child.isSegment():
                # shouldn't ever happen...
                continue

            segname = child.getName()
            nelem = child.numElements()

            if segname == "AK3":
                self.seg_id_code = child.getElement(1)
                self.seg_pos = child.getElement(2)
                if nelem >= 3:
                    self.loop_id_code = child.getElement(3)
                if nelem >= 4:
                    ec = child.getElement(4)
                    self.seg_err_code = ec
                    self.seg_err_code_str = medltc.ansi997.segmentSyntaxCodeToStr(ec)
            elif segname == "AK4":
                self.data_element_notes.append(Ansi997DataElementNote(child))


class Ansi997TransactionSetResponse(object):
    def __init__(self, loop):
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
                    self.ts_control_num = child.getElement(2)
                elif segname == "AK5":
                    self.ts_ack_code = child.getElement(1)
                    self.ts_ack_code_str = medltc.ansi997.transactionSetAckCodeToStr(self.ts_ack_code)
                    for i in range(nelem - 1):
                        ec = child.getElement(i+2)
                        self.ts_err_codes.append(ec)
                        self.ts_err_codes_str.append(medltc.ansi997.transactionSetSyntaxCodeToStr(ec))

            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "AK2/AK3":
                    self.data_segment_notes.append(Ansi997DataSegmentNote(child))

class Ansi997TransactionSet(object):
    def __init__(self, x12ts):
        root = x12ts.getRootLoop()

        self.control_num = None
        self.fg_control_num = None
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
                    self.fg_control_num = child.getElement(2)
                elif segname == "AK9":
                    self.fg_ack_code = child.getElement(1)
                    self.fg_ack_code_str = medltc.ansi997.functionalGroupAckCodeToStr(self.fg_ack_code)
                    self.ts_num_included = int(child.getElement(2))
                    self.ts_num_received = int(child.getElement(3))
                    self.ts_num_accepted = int(child.getElement(4))
                    for i in range(nelem - 4):
                        ec = child.getElement(i+5)
                        self.fg_err_codes.append(ec)
                        self.fg_err_codes_str.append(medltc.ansi997.functionalGroupSyntaxCodeToStr(ec))
            elif child.isLoop():
                loopname = child.getLoopName()
                if loopname == "AK2":
                    self.ts_responses.append(Ansi997TransactionSetResponse(child))

class Ansi997FunctionalGroup(object):
    def __init__(self, x12fg):
        self.transaction_sets = \
                [ Ansi997TransactionSet(ts) for ts in x12fg.getTransactionSets() ]

class Ansi997Document(object):
    def __init__(self, x12doc):
        self.functional_groups = \
                [ Ansi997FunctionalGroup(fg) for fg in x12doc.getFunctionalGroups() ]

