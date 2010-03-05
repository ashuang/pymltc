def __get_remarks():
    from xml.dom import minidom

    doc = minidom.parseString(__xml)
    rnode = doc.documentElement

    codes = rnode.getElementsByTagName("CODE")
    descriptions = rnode.getElementsByTagName("DESCRIPTION")

    result = {}
    for cnode, dnode in zip(codes, descriptions):
        code = cnode.childNodes[0].data.strip().upper()
        desc = dnode.childNodes[0].data.strip()
        result[code] = desc

    return result

__xml = """
<remarks>
<CODE>M1   </CODE><DESCRIPTION>X-ray not taken within the past 12 months or near enough to the start of treatment.</DESCRIPTION>

<CODE>M2   </CODE><DESCRIPTION>Not paid separately when the patient is an inpatient.</DESCRIPTION>

<CODE>M3   </CODE><DESCRIPTION>Equipment is the same or similar to equipment already being used.</DESCRIPTION>

<CODE>M4   </CODE><DESCRIPTION>Alert: This is the last monthly installment payment for this durable medical equipment.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M5   </CODE><DESCRIPTION>Monthly rental payments can continue until the earlier of the 15th month from the first rental month, or the month when the equipment is no longer needed.</DESCRIPTION>

<CODE>M6   </CODE><DESCRIPTION>Alert: You must furnish and service this item for as long as the patient continues to need it.  We can pay for maintenance and/or servicing for every 6 month period after the end of the 15th paid rental month or the end of the warranty period.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M7   </CODE><DESCRIPTION>No rental payments after the item is purchased, or after the total of issued rental payments equals the purchase price.</DESCRIPTION>

<CODE>M8   </CODE><DESCRIPTION>We do not accept blood gas tests results when the test was conducted by a medical supplier or taken while the patient is on oxygen.</DESCRIPTION>

<CODE>M9   </CODE><DESCRIPTION>Alert: This is the tenth rental month. You must offer the patient the choice of changing the rental to a purchase agreement.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M10  </CODE><DESCRIPTION>Equipment purchases are limited to the first or the tenth month of medical necessity.</DESCRIPTION>

<CODE>M11  </CODE><DESCRIPTION>DME, orthotics and prosthetics must be billed to the DME carrier who services the patient's zip code.</DESCRIPTION>

<CODE>M12  </CODE><DESCRIPTION>Diagnostic tests performed by a physician must indicate whether purchased services are included on the claim.</DESCRIPTION>

<CODE>M13  </CODE><DESCRIPTION>Only one initial visit is covered per specialty per medical group.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>M14  </CODE><DESCRIPTION>No separate payment for an injection administered during an office visit, and no payment for a full office visit if the patient only received an injection.</DESCRIPTION>

<CODE>M15  </CODE><DESCRIPTION>Separately billed services/tests have been bundled as they are considered components of the same procedure. Separate payment is not allowed.</DESCRIPTION>

<CODE>M16  </CODE><DESCRIPTION>Alert: Please see our web site, mailings, or bulletins for more details concerning this policy/procedure/decision.<br /><i>Note: (Reactivated 4/1/04, Modified 11/18/05, 4/1/07)</i></DESCRIPTION>

<CODE>M17  </CODE><DESCRIPTION>Alert: Payment approved as you did not know, and could not reasonably have been expected to know, that this would not normally have been covered for this patient.  In the future, you will be liable for charges for the same service(s) under the same or similar conditions.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M18  </CODE><DESCRIPTION>Certain services may be approved for home use.  Neither a hospital nor a Skilled Nursing Facility (SNF) is considered to be a patient's home.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>M19  </CODE><DESCRIPTION>Missing oxygen certification/re-certification.<br /><i>Note: (Modified 2/28/03) Related to N234</i></DESCRIPTION>

<CODE>M20  </CODE><DESCRIPTION>Missing/incomplete/invalid HCPCS.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M21  </CODE><DESCRIPTION>Missing/incomplete/invalid place of residence for this service/item provided in a home.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M22  </CODE><DESCRIPTION>Missing/incomplete/invalid number of miles traveled.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M23  </CODE><DESCRIPTION>Missing invoice.<br /><i>Note: (Modified 8/1/05)</i></DESCRIPTION>

<CODE>M24  </CODE><DESCRIPTION>Missing/incomplete/invalid number of doses per vial.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M25  </CODE><DESCRIPTION>The information furnished does not substantiate the need for this level of service.  If you believe the service should have been fully covered as billed, or if you did not know and could not reasonably have been expected to know that we would not pay for this level of service, or if you notified the patient in writing in advance that we would not pay for this level of service and he/she agreed in writing to pay, ask us to review your claim within 120 days of the date of this notice.  If you do not request a appeal, we will, upon application from the patient, reimburse him/her for the amount you have collected from him/her in excess of any deductible and coinsurance amounts.  We will recover the reimbursement from you as an overpayment.<br /><i>Note: (Modified 10/1/02, 6/30/03, 8/1/05, 11/5/07)</i></DESCRIPTION>

<CODE>M26  </CODE><DESCRIPTION>The information furnished does not substantiate the need for this level of service. If you have collected any amount from the patient for this level of service /any amount that exceeds the limiting charge for the less extensive service, the law requires you to refund that amount to the patient within 30 days of receiving this notice. <br /><br />The requirements for refund are in 1824(I) of the Social Security Act and 42CFR411.408. The section specifies that physicians who knowingly and willfully fail to make appropriate refunds may be subject to civil monetary penalties and/or exclusion from the program. If you have any questions about this notice, please contact this office.<br /><i>Note: (Modified 10/1/02, 6/30/03, 8/1/05, 11/5/07. Also refer to N356)</i></DESCRIPTION>

<CODE>M27  </CODE><DESCRIPTION>Alert: The patient has been relieved of liability of payment of these items and services under the limitation of liability provision of the law. The provider is ultimately liable for the patient's waived charges, including any charges for coinsurance, since the items or services were not reasonable and necessary or constituted custodial care, and you knew or could reasonably have been expected to know, that they were not covered. You may appeal this determination. You may ask for an appeal regarding both the coverage determination and the issue of whether you exercised due care. The appeal request must be filed within 120 days of the date you receive this notice. You must make the request through this office.<br /><i>Note: (Modified 10/1/02, 8/1/05, 4/1/07, 8/1/07)</i></DESCRIPTION>

<CODE>M28  </CODE><DESCRIPTION>This does not qualify for payment under Part B when Part A coverage is exhausted or not otherwise available.</DESCRIPTION>

<CODE>M29  </CODE><DESCRIPTION>Missing operative report.<br /><i>Note: (Modified 2/28/03) Related to N233</i></DESCRIPTION>

<CODE>M30  </CODE><DESCRIPTION>Missing pathology report.<br /><i>Note: (Modified 8/1/04, 2/28/03) Related to N236</i></DESCRIPTION>

<CODE>M31  </CODE><DESCRIPTION>Missing radiology report.<br /><i>Note: (Modified 8/1/04, 2/28/03) Related to N240</i></DESCRIPTION>

<CODE>M32  </CODE><DESCRIPTION>Alert: This is a conditional payment made pending a decision on this service by the patient's primary payer. This payment may be subject to refund upon your receipt of any additional payment for this service from another payer. You must contact this office immediately upon receipt of an additional payment for this service.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M36  </CODE><DESCRIPTION>This is the 11th rental month.  We cannot pay for this until you indicate that the patient has been given the option of changing the rental to a purchase.</DESCRIPTION>

<CODE>M37  </CODE><DESCRIPTION>Service not covered when the patient is under age 35.</DESCRIPTION>

<CODE>M38  </CODE><DESCRIPTION>The patient is liable for the charges for this service as you informed the patient in writing before the service was furnished that we would not pay for it, and the patient agreed to pay.</DESCRIPTION>

<CODE>M39  </CODE><DESCRIPTION>Alert: The patient is not liable for payment for this service as the advance notice of non-coverage you provided the patient did not comply with program requirements.<br /><i>Note: (Modified 2/1/04, 4/1/07)</i></DESCRIPTION>

<CODE>M40  </CODE><DESCRIPTION>Claim must be assigned and must be filed by the practitioner's employer.</DESCRIPTION>

<CODE>M41  </CODE><DESCRIPTION>We do not pay for this as the patient has no legal obligation to pay for this.</DESCRIPTION>

<CODE>M42  </CODE><DESCRIPTION>The medical necessity form must be personally signed by the attending physician.</DESCRIPTION>

<CODE>M44  </CODE><DESCRIPTION>Missing/incomplete/invalid condition code.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M45  </CODE><DESCRIPTION>Missing/incomplete/invalid occurrence code(s).<br /><i>Note: (Modified 12/2/04) Related to N299</i></DESCRIPTION>

<CODE>M46  </CODE><DESCRIPTION>Missing/incomplete/invalid occurrence span code(s).<br /><i>Note: (Modified 12/2/04) Related to N300</i></DESCRIPTION>

<CODE>M47  </CODE><DESCRIPTION>Missing/incomplete/invalid internal or document control number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M49  </CODE><DESCRIPTION>Missing/incomplete/invalid value code(s) or amount(s).<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M50  </CODE><DESCRIPTION>Missing/incomplete/invalid revenue code(s).<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M51  </CODE><DESCRIPTION>Missing/incomplete/invalid procedure code(s).<br /><i>Note: (Modified 12/2/04) Related to N301</i></DESCRIPTION>

<CODE>M52  </CODE><DESCRIPTION>Missing/incomplete/invalid from date(s) of service.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M53  </CODE><DESCRIPTION>Missing/incomplete/invalid days or units of service.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M54  </CODE><DESCRIPTION>Missing/incomplete/invalid total charges.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M55  </CODE><DESCRIPTION>We do not pay for self-administered anti-emetic drugs that are not administered with a covered oral anti-cancer drug.</DESCRIPTION>

<CODE>M56  </CODE><DESCRIPTION>Missing/incomplete/invalid payer identifier.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M59  </CODE><DESCRIPTION>Missing/incomplete/invalid to date(s) of service.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M60  </CODE><DESCRIPTION>Missing Certificate of Medical Necessity.<br /><i>Note: (Modified 8/1/04, 6/30/03) Related to N227</i></DESCRIPTION>

<CODE>M61  </CODE><DESCRIPTION>We cannot pay for this as the approval period for the FDA clinical trial has expired.</DESCRIPTION>

<CODE>M62  </CODE><DESCRIPTION>Missing/incomplete/invalid treatment authorization code.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M64  </CODE><DESCRIPTION>Missing/incomplete/invalid other diagnosis.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M65  </CODE><DESCRIPTION>One interpreting physician charge can be submitted per claim when a purchased diagnostic test is indicated. Please submit a separate claim for each interpreting physician.</DESCRIPTION>

<CODE>M66  </CODE><DESCRIPTION>Our records indicate that you billed diagnostic tests subject to price limitations and the procedure code submitted includes a professional component. Only the technical component is subject to price limitations.  Please submit the technical and professional components of this service as separate line items.</DESCRIPTION>

<CODE>M67  </CODE><DESCRIPTION>Missing/incomplete/invalid other procedure code(s).<br /><i>Note: (Modified 12/2/04) Related to N302</i></DESCRIPTION>

<CODE>M69  </CODE><DESCRIPTION>Paid at the regular rate as you did not submit documentation to justify the modified procedure code.<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>M70  </CODE><DESCRIPTION>Alert: The NDC code submitted for this service was translated to a HCPCS code for processing, but please continue to submit the NDC on future claims for this item.<br /><i>Note: (Modified 4/1/2007, 8/1/07)</i></DESCRIPTION>

<CODE>M71  </CODE><DESCRIPTION>Total payment reduced due to overlap of tests billed.</DESCRIPTION>

<CODE>M73  </CODE><DESCRIPTION>The HPSA/Physician Scarcity bonus can only be paid on the professional component of this service. Rebill as separate professional and technical components. <br /><i>Note: (Modified 8/1/04)</i></DESCRIPTION>

<CODE>M74  </CODE><DESCRIPTION>This service does not qualify for a HPSA/Physician Scarcity bonus payment.<br /><i>Note: (Modified 12/2/04)</i></DESCRIPTION>

<CODE>M75  </CODE><DESCRIPTION>Multiple automated multichannel tests performed on the same day combined for payment.<br /><i>Note: (Modified 11/5/07)</i></DESCRIPTION>

<CODE>M76  </CODE><DESCRIPTION>Missing/incomplete/invalid diagnosis or condition.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M77  </CODE><DESCRIPTION>Missing/incomplete/invalid place of service.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M79  </CODE><DESCRIPTION>Missing/incomplete/invalid charge.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M80  </CODE><DESCRIPTION>Not covered when performed during the same session/date as a previously processed service for the patient.<br /><i>Note: (Modified 10/31/02)</i></DESCRIPTION>

<CODE>M81  </CODE><DESCRIPTION>You are required to code to the highest level of specificity.<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>M82  </CODE><DESCRIPTION>Service is not covered when patient is under age 50.</DESCRIPTION>

<CODE>M83  </CODE><DESCRIPTION>Service is not covered unless the patient is classified as at high risk.</DESCRIPTION>

<CODE>M84  </CODE><DESCRIPTION>Medical code sets used must be the codes in effect at the time of service<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>M85  </CODE><DESCRIPTION>Subjected to review of physician evaluation and management services.</DESCRIPTION>

<CODE>M86  </CODE><DESCRIPTION>Service denied because payment already made for same/similar procedure within set time frame.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>M87  </CODE><DESCRIPTION>Claim/service(s) subjected to CFO-CAP prepayment review.</DESCRIPTION>

<CODE>M89  </CODE><DESCRIPTION>Not covered more than once under age 40.</DESCRIPTION>

<CODE>M90  </CODE><DESCRIPTION>Not covered more than once in a 12 month period.</DESCRIPTION>

<CODE>M91  </CODE><DESCRIPTION>Lab procedures with different CLIA certification numbers must be billed on separate claims.</DESCRIPTION>

<CODE>M93  </CODE><DESCRIPTION>Information supplied supports a break in therapy.  A new capped rental period began with delivery of this equipment.</DESCRIPTION>

<CODE>M94  </CODE><DESCRIPTION>Information supplied does not support a break in therapy.  A new capped rental period will not begin.</DESCRIPTION>

<CODE>M95  </CODE><DESCRIPTION>Services subjected to Home Health Initiative medical review/cost report audit.</DESCRIPTION>

<CODE>M96  </CODE><DESCRIPTION>The technical component of a service furnished to an inpatient may only be billed by that inpatient facility. You must contact the inpatient facility for technical component reimbursement.  If not already billed, you should bill us for the professional component only.</DESCRIPTION>

<CODE>M97  </CODE><DESCRIPTION>Not paid to practitioner when provided to patient in this place of service.  Payment included in the reimbursement issued the facility.</DESCRIPTION>

<CODE>M99  </CODE><DESCRIPTION>Missing/incomplete/invalid Universal Product Number/Serial Number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M100 </CODE><DESCRIPTION>We do not pay for an oral anti-emetic drug that is not administered for use immediately before, at, or within 48 hours of administration of a covered chemotherapy drug.</DESCRIPTION>

<CODE>M102 </CODE><DESCRIPTION>Service not performed on equipment approved by the FDA for this purpose.</DESCRIPTION>

<CODE>M103 </CODE><DESCRIPTION>Information supplied supports a break in therapy.  However, the medical information we have for this patient does not support the need for this item as billed.  We have approved payment for this item at a reduced level, and a new capped rental period will begin with the delivery of this equipment.</DESCRIPTION>

<CODE>M104 </CODE><DESCRIPTION>Information supplied supports a break in therapy.  A new capped rental period will begin with delivery of the equipment.  This is the maximum approved under the fee schedule for this item or service.</DESCRIPTION>

<CODE>M105 </CODE><DESCRIPTION>Information supplied does not support a break in therapy.  The medical information we have for this patient does not support the need for this item as billed. We have approved payment for this item at a reduced level, and a new capped rental period will not begin.</DESCRIPTION>

<CODE>M107 </CODE><DESCRIPTION>Payment reduced as 90-day rolling average hematocrit for ESRD patient exceeded 36.5%.</DESCRIPTION>

<CODE>M109 </CODE><DESCRIPTION>We have provided you with a bundled payment for a teleconsultation. You must send 25 percent of the teleconsultation payment to the referring practitioner. </DESCRIPTION>

<CODE>M111 </CODE><DESCRIPTION>We do not pay for chiropractic manipulative treatment when the patient refuses to have an x-ray taken.</DESCRIPTION>

<CODE>M112 </CODE><DESCRIPTION>Reimbursement for this item is based on the single payment amount required under the DMEPOS Competitative Bidding Program for the area where the patient resides.<br /><i>Note: (Modified 11/5/07)</i></DESCRIPTION>

<CODE>M113 </CODE><DESCRIPTION>Our records indicate that this patient began using this item/service prior to the current contract period for the DMEPOS Competitive Bidding Program.<br /><i>Note: (Modified 11/5/07)</i></DESCRIPTION>

<CODE>M114 </CODE><DESCRIPTION>This service was processed in accordance with rules and guidelines under the DMEPOS Competitive Bidding Program or a Demonstration Project.  For more information regarding these projects, contact your local contractor.<br /><i>Note: (Modified 8/1/06, 11/5/07)</i></DESCRIPTION>

<CODE>M115 </CODE><DESCRIPTION>This item is denied when provided to this patient by a non-contract or non-demonstration supplier.<br /><i>Note: (Modified 11/5/2007)</i></DESCRIPTION>

<CODE>M116 </CODE><DESCRIPTION>Paid under the Competitive Bidding Demonstration project. Project is ending, and future services may not be paid under this project.<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>M117 </CODE><DESCRIPTION>Not covered unless submitted via electronic claim.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>M118 </CODE><DESCRIPTION>Alert: Letter to follow containing further information.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>M119 </CODE><DESCRIPTION>Missing/incomplete/invalid/ deactivated/withdrawn National Drug Code (NDC).<br /><i>Note: (Modified 2/28/03, 4/1/04)</i></DESCRIPTION>

<CODE>M121 </CODE><DESCRIPTION>We pay for this service only when performed with a covered cryosurgical ablation.</DESCRIPTION>

<CODE>M122 </CODE><DESCRIPTION>Missing/incomplete/invalid level of subluxation.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M123 </CODE><DESCRIPTION>Missing/incomplete/invalid name, strength, or dosage of the drug furnished.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M124 </CODE><DESCRIPTION>Missing indication of whether the patient owns the equipment that requires the part or supply.<br /><i>Note: (Modified 2/28/03) Related to N230</i></DESCRIPTION>

<CODE>M125 </CODE><DESCRIPTION>Missing/incomplete/invalid information on the period of time for which the service/supply/equipment will be needed.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M126 </CODE><DESCRIPTION>Missing/incomplete/invalid individual lab codes included in the test.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M127 </CODE><DESCRIPTION>Missing patient medical record for this service.<br /><i>Note: (Modified 2/28/03) Related to N237</i></DESCRIPTION>

<CODE>M129 </CODE><DESCRIPTION>Missing/incomplete/invalid indicator of x-ray availability for review.<br /><i>Note: (Modified 2/28/03, 6/30/03)</i></DESCRIPTION>

<CODE>M130 </CODE><DESCRIPTION>Missing invoice or statement certifying the actual cost of the lens, less discounts, and/or the type of intraocular lens used.<br /><i>Note: (Modified 2/28/03) Related to N231</i></DESCRIPTION>

<CODE>M131 </CODE><DESCRIPTION>Missing physician financial relationship form.<br /><i>Note: (Modified 2/28/03) Related to N239</i></DESCRIPTION>

<CODE>M132 </CODE><DESCRIPTION>Missing pacemaker registration form.<br /><i>Note: (Modified 2/28/03) Related to N235</i></DESCRIPTION>

<CODE>M133 </CODE><DESCRIPTION>Claim did not identify who performed the purchased diagnostic test or the amount you were charged for the test.</DESCRIPTION>

<CODE>M134 </CODE><DESCRIPTION>Performed by a facility/supplier in which the provider has a financial interest.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>M135 </CODE><DESCRIPTION>Missing/incomplete/invalid plan of treatment.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M136 </CODE><DESCRIPTION>Missing/incomplete/invalid indication that the service was supervised or evaluated by a physician.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>M137 </CODE><DESCRIPTION>Part B coinsurance under a demonstration project.</DESCRIPTION>

<CODE>M138 </CODE><DESCRIPTION>Patient identified as a demonstration participant but the patient was not enrolled in the demonstration at the time services were rendered.  Coverage is limited to demonstration participants.</DESCRIPTION>

<CODE>M139 </CODE><DESCRIPTION>Denied services exceed the coverage limit for the demonstration.</DESCRIPTION>

<CODE>M141 </CODE><DESCRIPTION>Missing physician certified plan of care.<br /><i>Note: (Modified 2/28/03) Related to N238</i></DESCRIPTION>

<CODE>M142 </CODE><DESCRIPTION>Missing American Diabetes Association Certificate of Recognition.<br /><i>Note: (Modified 2/28/03) Related to N226</i></DESCRIPTION>

<CODE>M143 </CODE><DESCRIPTION>The provider must update license information with the payer.<br /><i>Note: (Modified 12/1/06)</i></DESCRIPTION>

<CODE>M144 </CODE><DESCRIPTION>Pre-/post-operative care payment is included in the allowance for the surgery/procedure.</DESCRIPTION>

<CODE>MA01 </CODE><DESCRIPTION>Alert: If you do not agree with what we approved for these services, you may appeal our decision.  To make sure that we are fair to you, we require another individual that did not process your initial claim to conduct the appeal.  However, in order to be eligible for an appeal, you must write to us within 120 days of the date you received this notice, unless you have a good reason for being late.<br /><i>Note: (Modified 10/31/02, 6/30/03, 8/1/05, 4/1/07)</i></DESCRIPTION>

<CODE>MA02 </CODE><DESCRIPTION>Alert: If you do not agree with this determination, you have the right to appeal. You must file a written request for an appeal within 180 days of the date you receive this notice.<br /><i>Note: (Modified 10/31/02, 6/30/03, 8/1/05, 12/29/05, 8/1/06, 4/1/07)</i></DESCRIPTION>

<CODE>MA04 </CODE><DESCRIPTION>Secondary payment cannot be considered without the identity of or payment information from the primary payer.  The information was either not reported or was illegible.</DESCRIPTION>

<CODE>MA07 </CODE><DESCRIPTION>Alert: The claim information has also been forwarded to Medicaid for review.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA08 </CODE><DESCRIPTION>Alert: Claim information was not forwarded because the supplemental coverage is not with a Medigap plan, or you do not participate in Medicare.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA09 </CODE><DESCRIPTION>Claim submitted as unassigned but processed as assigned. You agreed to accept assignment for all claims.</DESCRIPTION>

<CODE>MA10 </CODE><DESCRIPTION>Alert: The patient's payment was in excess of the amount owed.  You must refund the overpayment to the patient.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA12 </CODE><DESCRIPTION>You have not established that you have the right under the law to bill for services furnished by the person(s) that furnished this (these) service(s).</DESCRIPTION>

<CODE>MA13 </CODE><DESCRIPTION>Alert: You may be subject to penalties if you bill the patient for amounts not reported with the PR (patient responsibility) group code.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA14 </CODE><DESCRIPTION>Alert: The patient is a member of an employer-sponsored prepaid health plan. Services from outside that health plan are not covered.  However, as you were not previously notified of this, we are paying this time.  In the future, we will not pay you for non-plan services.<br /><i>Note: (Modified 4/1/07, 8/1/07)</i></DESCRIPTION>

<CODE>MA15 </CODE><DESCRIPTION>Alert: Your claim has been separated to expedite handling. You will receive a separate notice for the other services reported.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA16 </CODE><DESCRIPTION>The patient is covered by the Black Lung Program.  Send this claim to the Department of Labor, Federal Black Lung Program, P.O. Box 828, Lanham-Seabrook MD 20703.</DESCRIPTION>

<CODE>MA17 </CODE><DESCRIPTION>We are the primary payer and have paid at the primary rate.  You must contact the patient's other insurer to refund any excess it may have paid due to its erroneous primary payment.</DESCRIPTION>

<CODE>MA18 </CODE><DESCRIPTION>Alert: The claim information is also being forwarded to the patient's supplemental insurer. Send any questions regarding supplemental benefits to them.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA19 </CODE><DESCRIPTION>Alert:  Information was not sent to the Medigap insurer due to incorrect/invalid information you submitted concerning that insurer. Please verify your information and submit your secondary claim directly to that insurer.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA20 </CODE><DESCRIPTION>Skilled Nursing Facility (SNF) stay not covered when care is primarily related to the use of an urethral catheter for convenience or the control of incontinence.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>MA21 </CODE><DESCRIPTION>SSA records indicate mismatch with name and sex.</DESCRIPTION>

<CODE>MA22 </CODE><DESCRIPTION>Payment of less than $1.00 suppressed.  </DESCRIPTION>

<CODE>MA23 </CODE><DESCRIPTION>Demand bill approved as result of medical review.</DESCRIPTION>

<CODE>MA24 </CODE><DESCRIPTION>Christian Science Sanitarium/ Skilled Nursing Facility (SNF) bill in the same benefit period. <br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>MA25 </CODE><DESCRIPTION>A patient may not elect to change a hospice provider more than once in a benefit period.</DESCRIPTION>

<CODE>MA26 </CODE><DESCRIPTION>Alert: Our records indicate that you were previously informed of this rule.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA27 </CODE><DESCRIPTION>Missing/incomplete/invalid entitlement number or name shown on the claim.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA28 </CODE><DESCRIPTION>Alert: Receipt of this notice by a physician or supplier who did not accept assignment is for information only and does not make the physician or supplier a party to the determination.  No additional rights to appeal this decision, above those rights already provided for by regulation/instruction, are conferred by receipt of this notice.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA30 </CODE><DESCRIPTION>Missing/incomplete/invalid type of bill.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA31 </CODE><DESCRIPTION>Missing/incomplete/invalid beginning and ending dates of the period billed.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA32 </CODE><DESCRIPTION>Missing/incomplete/invalid number of covered days during the billing period.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA33 </CODE><DESCRIPTION>Missing/incomplete/invalid noncovered days during the billing period.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA34 </CODE><DESCRIPTION>Missing/incomplete/invalid number of coinsurance days during the billing period.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA35 </CODE><DESCRIPTION>Missing/incomplete/invalid number of lifetime reserve days.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA36 </CODE><DESCRIPTION>Missing/incomplete/invalid patient name.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA37 </CODE><DESCRIPTION>Missing/incomplete/invalid patient's address.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA39 </CODE><DESCRIPTION>Missing/incomplete/invalid gender.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA40 </CODE><DESCRIPTION>Missing/incomplete/invalid admission date.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA41 </CODE><DESCRIPTION>Missing/incomplete/invalid admission type.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA42 </CODE><DESCRIPTION>Missing/incomplete/invalid admission source.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA43 </CODE><DESCRIPTION>Missing/incomplete/invalid patient status.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA44 </CODE><DESCRIPTION>Alert: No appeal rights. Adjudicative decision based on law.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA45 </CODE><DESCRIPTION>Alert: As previously advised, a portion or all of your payment is being held in a special account.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA46 </CODE><DESCRIPTION>The new information was considered, however, additional payment cannot be issued. Please review the information listed for the explanation.</DESCRIPTION>

<CODE>MA47 </CODE><DESCRIPTION>Our records show you have opted out of Medicare, agreeing with the patient not to bill Medicare for services/tests/supplies furnished.  As result, we cannot pay this claim. The patient is responsible for payment.</DESCRIPTION>

<CODE>MA48 </CODE><DESCRIPTION>Missing/incomplete/invalid name or address of responsible party or primary payer.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA50 </CODE><DESCRIPTION>Missing/incomplete/invalid Investigational Device Exemption number for FDA-approved clinical trial services.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA53 </CODE><DESCRIPTION>Missing/incomplete/invalid Competitive Bidding Demonstration Project identification. <br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>MA54 </CODE><DESCRIPTION>Physician certification or election consent for hospice care not received timely.</DESCRIPTION>

<CODE>MA55 </CODE><DESCRIPTION>Not covered as patient received medical health care services, automatically revoking his/her election to receive religious non-medical health care services.</DESCRIPTION>

<CODE>MA56 </CODE><DESCRIPTION>Our records show you have opted out of Medicare, agreeing with the patient not to bill Medicare for services/tests/supplies furnished.  As result, we cannot pay this claim. The patient is responsible for payment, but under Federal law, you cannot charge the patient more than the limiting charge amount.</DESCRIPTION>

<CODE>MA57 </CODE><DESCRIPTION>Patient submitted written request to revoke his/her election for religious non-medical health care services.</DESCRIPTION>

<CODE>MA58 </CODE><DESCRIPTION>Missing/incomplete/invalid release of information indicator.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA59 </CODE><DESCRIPTION>Alert: The patient overpaid you for these services. You must issue the patient a refund within 30 days for the difference between his/her payment and the total amount shown as patient responsibility on this notice. <br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA60 </CODE><DESCRIPTION>Missing/incomplete/invalid patient relationship to insured.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA61 </CODE><DESCRIPTION>Missing/incomplete/invalid social security number or health insurance claim number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA62 </CODE><DESCRIPTION>Alert: This is a telephone review decision.<br /><i>Note: (Modified 4/1/07, 8/1/07)</i></DESCRIPTION>

<CODE>MA63 </CODE><DESCRIPTION>Missing/incomplete/invalid principal diagnosis.<br /><i>Note: (Modified 2/28/03) </i></DESCRIPTION>

<CODE>MA64 </CODE><DESCRIPTION>Our records indicate that we should be the third payer for this claim.  We cannot process this claim until we have received payment information from the primary and secondary payers.</DESCRIPTION>

<CODE>MA65 </CODE><DESCRIPTION>Missing/incomplete/invalid admitting diagnosis.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA66 </CODE><DESCRIPTION>Missing/incomplete/invalid principal procedure code.<br /><i>Note: (Modified 12/2/04) Related to N303</i></DESCRIPTION>

<CODE>MA67 </CODE><DESCRIPTION>Correction to a prior claim.</DESCRIPTION>

<CODE>MA68 </CODE><DESCRIPTION>Alert: We did not crossover this claim because the secondary insurance information on the claim was incomplete. Please supply complete information or use the PLANID of the insurer to assure correct and timely routing of the claim.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA69 </CODE><DESCRIPTION>Missing/incomplete/invalid remarks.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA70 </CODE><DESCRIPTION>Missing/incomplete/invalid provider representative signature.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA71 </CODE><DESCRIPTION>Missing/incomplete/invalid provider representative signature date.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA72 </CODE><DESCRIPTION>Alert: The patient overpaid you for these assigned services.  You must issue the patient a refund within 30 days for the difference between his/her payment to you and the total of the amount shown as patient responsibility and as paid to the patient on this notice.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA73 </CODE><DESCRIPTION>Informational remittance associated with a Medicare demonstration.  No payment issued under fee-for-service Medicare as patient has elected managed care.</DESCRIPTION>

<CODE>MA74 </CODE><DESCRIPTION>This payment replaces an earlier payment for this claim that was either lost, damaged or returned.</DESCRIPTION>

<CODE>MA75 </CODE><DESCRIPTION>Missing/incomplete/invalid patient or authorized representative signature.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA76 </CODE><DESCRIPTION>Missing/incomplete/invalid provider identifier for home health agency or hospice when physician is performing care plan oversight services.<br /><i>Note: (Modified 2/28/03, 2/1/04)</i></DESCRIPTION>

<CODE>MA77 </CODE><DESCRIPTION>Alert: The patient overpaid you. You must issue the patient a refund within 30 days for the difference between the patient's payment less the total of our and other payer payments and the amount shown as patient responsibility on this notice.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>MA79 </CODE><DESCRIPTION>Billed in excess of interim rate.</DESCRIPTION>

<CODE>MA80 </CODE><DESCRIPTION>Informational notice. No payment issued for this claim with this notice. Payment issued to the hospital by its intermediary for all services for this encounter under a demonstration project.</DESCRIPTION>

<CODE>MA81 </CODE><DESCRIPTION>Missing/incomplete/invalid provider/supplier signature.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA83 </CODE><DESCRIPTION>Did not indicate whether we are the primary or secondary payer.<br /><i>Note: (Modified 8/1/05)</i></DESCRIPTION>

<CODE>MA84 </CODE><DESCRIPTION>Patient identified as participating in the National Emphysema Treatment Trial but our records indicate that this patient is either not a participant, or has not yet been approved for this phase of the study.  Contact Johns Hopkins University, the study coordinator, to resolve if there was a discrepancy.</DESCRIPTION>

<CODE>MA88 </CODE><DESCRIPTION>Missing/incomplete/invalid insured's address and/or telephone number for the primary payer.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA89 </CODE><DESCRIPTION>Missing/incomplete/invalid patient's relationship to the insured for the primary payer.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA90 </CODE><DESCRIPTION>Missing/incomplete/invalid employment status code for the primary insured.<br /><i>Note: (Modified 2/28/03). </i></DESCRIPTION>

<CODE>MA91 </CODE><DESCRIPTION>This determination is the result of the appeal you filed.</DESCRIPTION>

<CODE>MA92 </CODE><DESCRIPTION>Missing plan information for other insurance.<br /><i>Note: (Modified 2/1/04) Related to N245</i></DESCRIPTION>

<CODE>MA93 </CODE><DESCRIPTION>Non-PIP (Periodic Interim Payment) claim.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>MA94 </CODE><DESCRIPTION>Did not enter the statement "Attending physician not hospice employee" on the claim form to certify that the rendering physician is not an employee of the hospice.<br /><i>Note: (Reactivated 4/1/04, Modified 8/1/05)</i></DESCRIPTION>

<CODE>MA95 </CODE><DESCRIPTION>De-activate and refer to M51.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA96 </CODE><DESCRIPTION>Claim rejected. Coded as a Medicare Managed Care Demonstration but patient is not enrolled in a Medicare managed care plan.</DESCRIPTION>

<CODE>MA97 </CODE><DESCRIPTION>Missing/incomplete/invalid Medicare Managed Care Demonstration contract number or clinical trial registry number.<br /><i>Note: (Modified 2/29/08)</i></DESCRIPTION>

<CODE>MA99 </CODE><DESCRIPTION>Missing/incomplete/invalid Medigap information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA100</CODE><DESCRIPTION>Missing/incomplete/invalid date of current illness or symptoms<br /><i>Note: (Modified 2/28/03, 3/30/05)</i></DESCRIPTION>

<CODE>MA101</CODE><DESCRIPTION>A Skilled Nursing Facility (SNF) is responsible for payment of outside providers who furnish these services/supplies to residents.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>MA103</CODE><DESCRIPTION>Hemophilia Add On.</DESCRIPTION>

<CODE>MA106</CODE><DESCRIPTION>PIP (Periodic Interim Payment) claim.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>MA107</CODE><DESCRIPTION>Paper claim contains more than three separate data items in field 19.</DESCRIPTION>

<CODE>MA108</CODE><DESCRIPTION>Paper claim contains more than one data item in field 23.  </DESCRIPTION>

<CODE>MA109</CODE><DESCRIPTION>Claim processed in accordance with ambulatory surgical guidelines.  </DESCRIPTION>

<CODE>MA110</CODE><DESCRIPTION>Missing/incomplete/invalid information on whether the diagnostic test(s) were performed by an outside entity or if no purchased tests are included on the claim.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA111</CODE><DESCRIPTION>Missing/incomplete/invalid purchase price of the test(s) and/or the performing laboratory's name and address.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA112</CODE><DESCRIPTION>Missing/incomplete/invalid group practice information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA113</CODE><DESCRIPTION>Incomplete/invalid taxpayer identification number (TIN) submitted by you per the Internal Revenue Service. Your claims cannot be processed without your correct TIN, and you may not bill the patient pending correction of your TIN.  There are no appeal rights for unprocessable claims, but you may resubmit this claim after you have notified this office of your correct TIN.</DESCRIPTION>

<CODE>MA114</CODE><DESCRIPTION>Missing/incomplete/invalid information on where the services were furnished.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA115</CODE><DESCRIPTION>Missing/incomplete/invalid physical location (name and address, or PIN) where the service(s) were rendered in a Health Professional Shortage Area (HPSA).<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA116</CODE><DESCRIPTION>Did not complete the statement 'Homebound' on the claim to validate whether laboratory services were performed at home or in an institution.<br /><i>Note: (Reactivated 4/1/04)</i></DESCRIPTION>

<CODE>MA117</CODE><DESCRIPTION>This claim has been assessed a $1.00 user fee.</DESCRIPTION>

<CODE>MA118</CODE><DESCRIPTION>Coinsurance and/or deductible amounts apply to a claim for services or supplies furnished to a Medicare-eligible veteran through a facility of the Department of Veterans Affairs.  No Medicare payment issued.</DESCRIPTION>

<CODE>MA120</CODE><DESCRIPTION>Missing/incomplete/invalid CLIA certification number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>MA121</CODE><DESCRIPTION>Missing/incomplete/invalid x-ray date.<br /><i>Note: (Modified 12/2/04)</i></DESCRIPTION>

<CODE>MA122</CODE><DESCRIPTION>Missing/incomplete/invalid initial treatment date.<br /><i>Note: (Modified 12/2/04)</i></DESCRIPTION>

<CODE>MA123</CODE><DESCRIPTION>Your center was not selected to participate in this study, therefore, we cannot pay for these services.</DESCRIPTION>

<CODE>MA125</CODE><DESCRIPTION>Per legislation governing this program, payment constitutes payment in full. </DESCRIPTION>

<CODE>MA126</CODE><DESCRIPTION>Pancreas transplant not covered unless kidney transplant performed.</DESCRIPTION>

<CODE>MA128</CODE><DESCRIPTION>Missing/incomplete/invalid FDA approval number.<br /><i>Note: (Modified 2/28/03, 3/30/05)</i></DESCRIPTION>

<CODE>MA130</CODE><DESCRIPTION>Your claim contains incomplete and/or invalid information, and no appeal rights are afforded because the claim is unprocessable.  Please submit a new claim with the complete/correct information.</DESCRIPTION>

<CODE>MA131</CODE><DESCRIPTION>Physician already paid for services in conjunction with this demonstration claim.  You must have the physician withdraw that claim and refund the payment before we can process your claim.</DESCRIPTION>

<CODE>MA132</CODE><DESCRIPTION>Adjustment to the pre-demonstration rate.</DESCRIPTION>

<CODE>MA133</CODE><DESCRIPTION>Claim overlaps inpatient stay. Rebill only those services rendered outside the inpatient stay.</DESCRIPTION>

<CODE>MA134</CODE><DESCRIPTION>Missing/incomplete/invalid provider number of the facility where the patient resides. </DESCRIPTION>

<CODE>N1   </CODE><DESCRIPTION>Alert: You may appeal this decision in writing within the required time limits following receipt of this notice by following the instructions included in your contract or plan benefit documents.<br /><i>Note: (Modified 2/28/03, 4/1/07)</i></DESCRIPTION>

<CODE>N2   </CODE><DESCRIPTION>This allowance has been made in accordance with the most appropriate course of treatment provision of the plan.</DESCRIPTION>

<CODE>N3   </CODE><DESCRIPTION>Missing consent form.<br /><i>Note: (Modified 2/28/03) Related to N228</i></DESCRIPTION>

<CODE>N4   </CODE><DESCRIPTION>Missing/incomplete/invalid prior insurance carrier EOB.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N5   </CODE><DESCRIPTION>EOB received from previous payer.  Claim not on file.</DESCRIPTION>

<CODE>N6   </CODE><DESCRIPTION>Under FEHB law (U.S.C. 8904(b)), we cannot pay more for covered care than the amount Medicare would have allowed if the patient were enrolled in Medicare Part A and/or Medicare Part B.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N7   </CODE><DESCRIPTION>Processing of this claim/service has included consideration under Major Medical provisions.</DESCRIPTION>

<CODE>N8   </CODE><DESCRIPTION>Crossover claim denied by previous payer and complete claim data not forwarded. Resubmit this claim to this payer to provide adequate data for adjudication.</DESCRIPTION>

<CODE>N9   </CODE><DESCRIPTION>Adjustment represents the estimated amount a previous payer may pay.<br /><i>Note: (Modified 11/18/05)</i></DESCRIPTION>

<CODE>N10  </CODE><DESCRIPTION>Claim/service adjusted based on the findings of a review organization/professional consult/manual adjudication/medical or dental advisor.<br /><i>Note: (Modified 10/31/02)</i></DESCRIPTION>

<CODE>N11  </CODE><DESCRIPTION>Denial reversed because of medical review.</DESCRIPTION>

<CODE>N12  </CODE><DESCRIPTION>Policy provides coverage supplemental to Medicare. As the member does not appear to be enrolled in the applicable part of Medicare, the member is responsible for payment of the portion of the charge that would have been covered by Medicare.<br /><i>Note: (Modified 8/1/07)</i></DESCRIPTION>

<CODE>N13  </CODE><DESCRIPTION>Payment based on professional/technical component modifier(s).</DESCRIPTION>

<CODE>N15  </CODE><DESCRIPTION>Services for a newborn must be billed separately.</DESCRIPTION>

<CODE>N16  </CODE><DESCRIPTION>Family/member Out-of-Pocket maximum has been met. Payment based on a higher percentage.</DESCRIPTION>

<CODE>N19  </CODE><DESCRIPTION>Procedure code incidental to primary procedure.</DESCRIPTION>

<CODE>N20  </CODE><DESCRIPTION>Service not payable with other service rendered on the same date.</DESCRIPTION>

<CODE>N21  </CODE><DESCRIPTION>Alert: Your line item has been separated into multiple lines to expedite handling.<br /><i>Note: (Modified 8/1/05, 4/1/07)</i></DESCRIPTION>

<CODE>N22  </CODE><DESCRIPTION>This procedure code was added/changed because it more accurately describes the services rendered.<br /><i>Note: (Modified 10/31/02, 2/28/03)</i></DESCRIPTION>

<CODE>N23  </CODE><DESCRIPTION>Alert: Patient liability may be affected due to coordination of benefits with other carriers and/or maximum benefit provisions.<br /><i>Note: (Modified 8/13/01, 4/1/07)</i></DESCRIPTION>

<CODE>N24  </CODE><DESCRIPTION>Missing/incomplete/invalid Electronic Funds Transfer (EFT) banking information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N25  </CODE><DESCRIPTION>This company has been contracted by your benefit plan to provide administrative claims payment services only.  This company does not assume financial risk or obligation with respect to claims processed on behalf of your benefit plan.</DESCRIPTION>

<CODE>N26  </CODE><DESCRIPTION>Missing itemized bill.<br /><i>Note: (Modified 2/28/03) Related to N232</i></DESCRIPTION>

<CODE>N27  </CODE><DESCRIPTION>Missing/incomplete/invalid treatment number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N28  </CODE><DESCRIPTION>Consent form requirements not fulfilled.</DESCRIPTION>

<CODE>N29  </CODE><DESCRIPTION>Missing documentation/orders/notes/summary/report/chart.<br /><i>Note: (Modified 2/28/03, 8/1/05) Related to N225</i></DESCRIPTION>

<CODE>N30  </CODE><DESCRIPTION>Patient ineligible for this service.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N31  </CODE><DESCRIPTION>Missing/incomplete/invalid prescribing provider identifier.<br /><i>Note: (Modified 12/2/04)</i></DESCRIPTION>

<CODE>N32  </CODE><DESCRIPTION>Claim must be submitted by the provider who rendered the service.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N33  </CODE><DESCRIPTION>No record of health check prior to initiation of treatment.</DESCRIPTION>

<CODE>N34  </CODE><DESCRIPTION>Incorrect claim form/format for this service.<br /><i>Note: (Modified 11/18/05)</i></DESCRIPTION>

<CODE>N35  </CODE><DESCRIPTION>Program integrity/utilization review decision.</DESCRIPTION>

<CODE>N36  </CODE><DESCRIPTION>Claim must meet primary payer's processing requirements before we can consider payment.</DESCRIPTION>

<CODE>N37  </CODE><DESCRIPTION>Missing/incomplete/invalid tooth number/letter.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N39  </CODE><DESCRIPTION>Procedure code is not compatible with tooth number/letter.</DESCRIPTION>

<CODE>N40  </CODE><DESCRIPTION>Missing x-ray.<br /><i>Note: (Modified 2/1/04) Related to N242</i></DESCRIPTION>

<CODE>N42  </CODE><DESCRIPTION>No record of mental health assessment.</DESCRIPTION>

<CODE>N43  </CODE><DESCRIPTION>Bed hold or leave days exceeded.</DESCRIPTION>

<CODE>N45  </CODE><DESCRIPTION>Payment based on authorized amount.</DESCRIPTION>

<CODE>N46  </CODE><DESCRIPTION>Missing/incomplete/invalid admission hour.</DESCRIPTION>

<CODE>N47  </CODE><DESCRIPTION>Claim conflicts with another inpatient stay.</DESCRIPTION>

<CODE>N48  </CODE><DESCRIPTION>Claim information does not agree with information received from other insurance carrier.</DESCRIPTION>

<CODE>N49  </CODE><DESCRIPTION>Court ordered coverage information needs validation.</DESCRIPTION>

<CODE>N50  </CODE><DESCRIPTION>Missing/incomplete/invalid discharge information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N51  </CODE><DESCRIPTION>Electronic interchange agreement not on file for provider/submitter.</DESCRIPTION>

<CODE>N52  </CODE><DESCRIPTION>Patient not enrolled in the billing provider's managed care plan on the date of service.</DESCRIPTION>

<CODE>N53  </CODE><DESCRIPTION>Missing/incomplete/invalid point of pick-up address.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N54  </CODE><DESCRIPTION>Claim information is inconsistent with pre-certified/authorized services.</DESCRIPTION>

<CODE>N55  </CODE><DESCRIPTION>Procedures for billing with group/referring/performing providers were not followed.</DESCRIPTION>

<CODE>N56  </CODE><DESCRIPTION>Procedure code billed is not correct/valid for the services billed or the date of service billed.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N57  </CODE><DESCRIPTION>Missing/incomplete/invalid prescribing date.<br /><i>Note: (Modified 12/2/04) Related to N304</i></DESCRIPTION>

<CODE>N58  </CODE><DESCRIPTION>Missing/incomplete/invalid patient liability amount.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N59  </CODE><DESCRIPTION>Alert: Please refer to your provider manual for additional program and provider information.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N61  </CODE><DESCRIPTION>Rebill services on separate claims.</DESCRIPTION>

<CODE>N62  </CODE><DESCRIPTION>Inpatient admission spans multiple rate periods.  Resubmit separate claims.</DESCRIPTION>

<CODE>N63  </CODE><DESCRIPTION>Rebill services on separate claim lines.</DESCRIPTION>

<CODE>N64  </CODE><DESCRIPTION>The from and to dates must be different.</DESCRIPTION>

<CODE>N65  </CODE><DESCRIPTION>Procedure code or procedure rate count cannot be determined, or was not on file, for the date of service/provider.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N67  </CODE><DESCRIPTION>Professional provider services not paid separately.  Included in facility payment under a demonstration project.  Apply to that facility for payment, or resubmit your claim if: the facility notifies you the patient was excluded from this demonstration; or if you furnished these services in another location on the date of the patient's admission or discharge from a demonstration hospital. If services were furnished in a facility not involved in the demonstration on the same date the patient was discharged from or admitted to a demonstration facility, you must report the provider ID number for the non-demonstration facility on the new claim.</DESCRIPTION>

<CODE>N68  </CODE><DESCRIPTION>Prior payment being cancelled as we were subsequently notified this patient was covered by a demonstration project in this site of service.  Professional services were included in the payment made to the facility. You must contact the facility for your payment.  Prior payment made to you by the patient or another insurer for this claim must be refunded to the payer within 30 days.</DESCRIPTION>

<CODE>N69  </CODE><DESCRIPTION>PPS (Prospective Payment System) code changed by claims processing system.  Insufficient visits or therapies.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N70  </CODE><DESCRIPTION>Consolidated billing and payment applies.<br /><i>Note: (Modified 2/28/02, 11/5/07)</i></DESCRIPTION>

<CODE>N71  </CODE><DESCRIPTION>Your unassigned claim for a drug or biological, clinical diagnostic laboratory services or ambulance service was processed as an assigned claim. You are required by law to accept assignment for these types of claims.<br /><i>Note: (Modified 2/21/02, 6/30/03)</i></DESCRIPTION>

<CODE>N72  </CODE><DESCRIPTION>PPS (Prospective Payment System)  code changed by medical reviewers.  Not supported by clinical records. <br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N74  </CODE><DESCRIPTION>Resubmit with multiple claims, each claim covering services provided in only one calendar month.</DESCRIPTION>

<CODE>N75  </CODE><DESCRIPTION>Missing/incomplete/invalid tooth surface information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N76  </CODE><DESCRIPTION>Missing/incomplete/invalid number of riders.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N77  </CODE><DESCRIPTION>Missing/incomplete/invalid designated provider number.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N78  </CODE><DESCRIPTION>The necessary components of the child and teen checkup (EPSDT) were not completed.  </DESCRIPTION>

<CODE>N79  </CODE><DESCRIPTION>Service billed is not compatible with patient location information.</DESCRIPTION>

<CODE>N80  </CODE><DESCRIPTION>Missing/incomplete/invalid prenatal screening information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N81  </CODE><DESCRIPTION>Procedure billed is not compatible with tooth surface code.</DESCRIPTION>

<CODE>N82  </CODE><DESCRIPTION>Provider must accept insurance payment as payment in full when a third party payer contract specifies full reimbursement.</DESCRIPTION>

<CODE>N83  </CODE><DESCRIPTION>No appeal rights. Adjudicative decision based on the provisions of a demonstration project.</DESCRIPTION>

<CODE>N84  </CODE><DESCRIPTION>Alert: Further installment payments are forthcoming.<br /><i>Note: (Modified 4/1/07, 8/1/07)</i></DESCRIPTION>

<CODE>N85  </CODE><DESCRIPTION>Alert: This is the final installment payment.<br /><i>Note: (Modified 4/1/07, 8/1/07)</i></DESCRIPTION>

<CODE>N86  </CODE><DESCRIPTION>A failed trial of pelvic muscle exercise training is required in order for biofeedback training for the treatment of urinary incontinence to be covered.</DESCRIPTION>

<CODE>N87  </CODE><DESCRIPTION>Home use of biofeedback therapy is not covered.</DESCRIPTION>

<CODE>N88  </CODE><DESCRIPTION>Alert: This payment is being made conditionally.  An HHA episode of care notice has been filed for this patient. When a patient is treated under a HHA episode of care, consolidated billing requires that certain therapy services and supplies, such as this, be included in the HHA's payment.  This payment will need to be recouped from you if we establish that the patient is concurrently receiving treatment under a HHA episode of care.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N89  </CODE><DESCRIPTION>Alert: Payment information for this claim has been forwarded to more than one other payer, but format limitations permit only one of the secondary payers to be identified in this remittance advice.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N90  </CODE><DESCRIPTION>Covered only when performed by the attending physician.</DESCRIPTION>

<CODE>N91  </CODE><DESCRIPTION>Services not included in the appeal review.</DESCRIPTION>

<CODE>N92  </CODE><DESCRIPTION>This facility is not certified for digital mammography.</DESCRIPTION>

<CODE>N93  </CODE><DESCRIPTION>A separate claim must be submitted for each place of service. Services furnished at multiple sites may not be billed in the same claim.</DESCRIPTION>

<CODE>N94  </CODE><DESCRIPTION>Claim/Service denied because a more specific taxonomy code is required for adjudication.</DESCRIPTION>

<CODE>N95  </CODE><DESCRIPTION>This provider type/provider specialty may not bill this service.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N96  </CODE><DESCRIPTION>Patient must be refractory to conventional therapy (documented behavioral, pharmacologic and/or surgical corrective therapy) and be an appropriate surgical candidate such that implantation with anesthesia can occur.</DESCRIPTION>

<CODE>N97  </CODE><DESCRIPTION>Patients with stress incontinence, urinary obstruction, and specific neurologic diseases (e.g., diabetes with peripheral nerve involvement) which are associated with secondary manifestations of the above three indications are excluded.</DESCRIPTION>

<CODE>N98  </CODE><DESCRIPTION>Patient must have had a successful test stimulation in order to support subsequent implantation. Before a patient is eligible for permanent implantation, he/she must demonstrate a 50 percent or greater improvement through test stimulation. Improvement is measured through voiding diaries.</DESCRIPTION>

<CODE>N99  </CODE><DESCRIPTION>Patient must be able to demonstrate adequate ability to record voiding diary data such that clinical results of the implant procedure can be properly evaluated.</DESCRIPTION>

<CODE>N100 </CODE><DESCRIPTION>PPS (Prospect Payment System) code corrected during adjudication.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N102 </CODE><DESCRIPTION>This claim has been denied without reviewing the medical record because the requested records were not received or were not received timely.</DESCRIPTION>

<CODE>N103 </CODE><DESCRIPTION>Social Security records indicate that this patient was a prisoner when the service was rendered.  This payer does not cover items and services furnished to an  individual while they are in State or local custody under a penal authority, unless under State or local law, the individual  is personally liable for the cost of his or her health care while incarcerated and the State or local government pursues such debt in the same way and with the same vigor as any other debt.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N104 </CODE><DESCRIPTION>This claim/service is not payable under our claims jurisdiction area. You can identify the correct Medicare contractor to process this claim/service through the CMS website at www.cms.hhs.gov.<br /><i>Note: (Modified 10/31/02)</i></DESCRIPTION>

<CODE>N105 </CODE><DESCRIPTION>This is a misdirected claim/service for an RRB beneficiary. Submit paper claims to the RRB carrier: Palmetto GBA, P.O. Box 10066, Augusta, GA 30999. Call 866-749-4301 for RRB EDI information for electronic claims processing.</DESCRIPTION>

<CODE>N106 </CODE><DESCRIPTION>Payment for services furnished to Skilled Nursing Facility (SNF) inpatients (except for excluded services) can only be made to the SNF. You must request payment from the SNF rather than the patient for this service.</DESCRIPTION>

<CODE>N107 </CODE><DESCRIPTION>Services furnished to Skilled Nursing Facility (SNF) inpatients must be billed on the inpatient claim. They cannot be billed separately as outpatient services.</DESCRIPTION>

<CODE>N108 </CODE><DESCRIPTION>Missing/incomplete/invalid upgrade information.<br /><i>Note: (Modified 2/28/03)</i></DESCRIPTION>

<CODE>N109 </CODE><DESCRIPTION>This claim was chosen for complex review and was denied after reviewing the medical records.</DESCRIPTION>

<CODE>N110 </CODE><DESCRIPTION>This facility is not certified for film mammography.</DESCRIPTION>

<CODE>N111 </CODE><DESCRIPTION>No appeal right except duplicate claim/service issue. This service was included in a claim that has been previously billed and adjudicated.</DESCRIPTION>

<CODE>N112 </CODE><DESCRIPTION>This claim is excluded from your electronic remittance advice.</DESCRIPTION>

<CODE>N113 </CODE><DESCRIPTION>Only one initial visit is covered per physician, group practice or provider.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N114 </CODE><DESCRIPTION>During the transition to the Ambulance Fee Schedule, payment is based on the lesser of a blended amount calculated using a percentage of the reasonable charge/cost and fee schedule amounts, or the submitted charge for the service.  You will be notified yearly what the percentages for the blended payment calculation will be.</DESCRIPTION>

<CODE>N115 </CODE><DESCRIPTION>This decision was based on a local medical review policy (LMRP) or Local Coverage Determination (LCD).An LMRP/LCD provides a guide to assist in determining whether a particular item or service is covered.  A copy of this policy is available at http://www.cms.hhs.gov/mcd, or if you do not have web access, you may contact the contractor to request a copy of the LMRP/LCD.<br /><i>Note: (Modified 4/1/04)</i></DESCRIPTION>

<CODE>N116 </CODE><DESCRIPTION>This payment is being made conditionally because the service was provided in the home, and it is possible that the patient is under a home health episode of care.  When a patient is treated under a home health episode of care, consolidated billing requires that certain therapy services and supplies, such as this, be included in the home health agency's (HHA's) payment.  This payment will need to be recouped from you if we establish that the patient is concurrently receiving treatment under an HHA episode of care.</DESCRIPTION>

<CODE>N117 </CODE><DESCRIPTION>This service is paid only once in a patient's lifetime.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N118 </CODE><DESCRIPTION>This service is not paid if billed more than once every 28 days.</DESCRIPTION>

<CODE>N119 </CODE><DESCRIPTION>This service is not paid if billed once every 28 days, and the patient has spent 5 or more consecutive days in any inpatient or Skilled /nursing Facility (SNF) within those 28 days.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N120 </CODE><DESCRIPTION>Payment is subject to home health prospective payment system partial episode payment adjustment. Patient was transferred/discharged/readmitted during payment episode.<br /><i>Note: (Modified 6/30/03)</i></DESCRIPTION>

<CODE>N121 </CODE><DESCRIPTION>Medicare Part B does not pay for items or services provided by this type of practitioner for beneficiaries in a Medicare Part A covered Skilled Nursing Facility (SNF) stay.<br /><i>Note: (Modified 8/1/04, 6/30/03)</i></DESCRIPTION>

<CODE>N122 </CODE><DESCRIPTION>Add-on code cannot be billed by itself.<br /><i>Note: (Modified 8/1/05)</i></DESCRIPTION>

<CODE>N123 </CODE><DESCRIPTION>This is a split service and represents a portion of the units from the originally submitted service.</DESCRIPTION>

<CODE>N124 </CODE><DESCRIPTION>Payment has been denied for the/made only for a less extensive service/item because the information furnished does not substantiate the need for the (more extensive) service/item. The patient is liable for the charges for this service/item as you informed the patient in writing before the service/item was furnished that we would not pay for it, and the patient agreed to pay.</DESCRIPTION>

<CODE>N125 </CODE><DESCRIPTION>Payment has been (denied for the/made only for a less extensive) service/item because the information furnished does not substantiate the need for the (more extensive) service/item. If you have collected any amount from the patient, you must refund that amount to the patient within 30 days of receiving this notice.<br /><br />The requirements for a refund are in section 1834(a)(18) of the Social Security Act (and in sections 1834(j)(4) and 1879(h) by cross-reference to section 1834(a)(18)). Section 1834(a)(18)(B) specifies that suppliers which knowingly and willfully fail to make appropriate refunds may be subject to civil money penalties and/or exclusion from the Medicare program. If you have any questions about this notice, please contact this office.<br /><i>Note: (Modified 8/1/05. Also refer to N356)</i></DESCRIPTION>

<CODE>N126 </CODE><DESCRIPTION>Social Security Records indicate that this individual has been deported. This payer does not cover items and services furnished to individuals who have been deported.</DESCRIPTION>

<CODE>N127 </CODE><DESCRIPTION>This is a misdirected claim/service for a United Mine Workers of America (UMWA) beneficiary. Please submit claims to them.<br /><i>Note: (Modified 8/1/04</i></DESCRIPTION>

<CODE>N128 </CODE><DESCRIPTION>This amount represents the prior to coverage portion of the allowance.</DESCRIPTION>

<CODE>N129 </CODE><DESCRIPTION>Not eligible due to the patient's age.<br /><i>Note: (Modified 8/1/07)</i></DESCRIPTION>

<CODE>N130 </CODE><DESCRIPTION>Alert: Consult plan benefit documents for information about restrictions for this service.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N131 </CODE><DESCRIPTION>Total payments under multiple contracts cannot exceed the allowance for this service.</DESCRIPTION>

<CODE>N132 </CODE><DESCRIPTION>Alert: Payments will cease for services rendered by this US Government debarred or excluded provider after the 30 day grace period as previously notified.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N133 </CODE><DESCRIPTION>Alert: Services for predetermination and services requesting payment are being processed separately.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N134 </CODE><DESCRIPTION>Alert: This represents your scheduled payment for this service. If treatment has been discontinued, please contact Customer Service.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N135 </CODE><DESCRIPTION>Record fees are the patient's responsibility and limited to the specified co-payment.</DESCRIPTION>

<CODE>N136 </CODE><DESCRIPTION>Alert: To obtain information on the process to file an appeal in Arizona, call the Department's Consumer Assistance Office at (602) 912-8444 or (800) 325-2548.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N137 </CODE><DESCRIPTION>Alert: The provider acting on the Member's behalf, may file an appeal with the Payer. The provider, acting on the Member's behalf, may file a complaint with the State Insurance Regulatory Authority without first filing an appeal, if the coverage decision involves an urgent condition for which care has not been rendered. The address may be obtained from the State Insurance Regulatory Authority.<br /><i>Note: (Modified  8/1/04, 2/28/03, 4/1/07)</i></DESCRIPTION>

<CODE>N138 </CODE><DESCRIPTION>Alert: In the event you disagree with the Dental Advisor's opinion and have additional information relative to the case, you may submit radiographs to the Dental Advisor Unit at the subscriber's dental insurance carrier for a second Independent Dental Advisor Review.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N139 </CODE><DESCRIPTION>Alert: Under the Code of Federal Regulations, Chapter 32, Section 199.13 a non-participating provider is not an appropriate appealing party. Therefore, if you disagree with the Dental Advisor's opinion, you may appeal the determination if appointed in writing, by the beneficiary, to act as his/her representative. Should you be appointed as a representative, submit a copy of this letter, a signed statement explaining the matter in which you disagree, and any radiographs and relevant information to the subscriber's Dental insurance carrier within 90 days from the date of this letter.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N140 </CODE><DESCRIPTION>Alert: You have not been designated as an authorized OCONUS provider therefore are not considered an appropriate appealing party. If the beneficiary has appointed you, in writing, to act as his/her representative and you disagree with the Dental Advisor's opinion, you may appeal by submitting a copy of this letter, a signed statement explaining the matter in which you disagree, and any relevant information to the subscriber's Dental insurance carrier within 90 days from the date of this letter.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N141 </CODE><DESCRIPTION>The patient was not residing in a long-term care facility during all or part of the service dates billed.</DESCRIPTION>

<CODE>N142 </CODE><DESCRIPTION>The original claim was denied.  Resubmit a new claim, not a replacement claim.</DESCRIPTION>

<CODE>N143 </CODE><DESCRIPTION>The patient was not in a hospice program during all or part of the service dates billed.</DESCRIPTION>

<CODE>N144 </CODE><DESCRIPTION>The rate changed during the dates of service billed.</DESCRIPTION>

<CODE>N146 </CODE><DESCRIPTION>Missing screening document.<br /><i>Note: (Modified  8/1/04) Related to N243</i></DESCRIPTION>

<CODE>N147 </CODE><DESCRIPTION>Long term care case mix or per diem rate cannot be determined because the patient ID number is missing, incomplete, or invalid on the assignment request.</DESCRIPTION>

<CODE>N148 </CODE><DESCRIPTION>Missing/incomplete/invalid date of last menstrual period.</DESCRIPTION>

<CODE>N149 </CODE><DESCRIPTION>Rebill all applicable services on a single claim.</DESCRIPTION>

<CODE>N150 </CODE><DESCRIPTION>Missing/incomplete/invalid model number.</DESCRIPTION>

<CODE>N151 </CODE><DESCRIPTION>Telephone contact services will not be paid until the face-to-face contact requirement has been met.</DESCRIPTION>

<CODE>N152 </CODE><DESCRIPTION>Missing/incomplete/invalid replacement claim information.</DESCRIPTION>

<CODE>N153 </CODE><DESCRIPTION>Missing/incomplete/invalid room and board rate.</DESCRIPTION>

<CODE>N154 </CODE><DESCRIPTION>Alert: This payment was delayed for correction of provider's mailing address.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N155 </CODE><DESCRIPTION>Alert: Our records do not indicate that other insurance is on file.  Please submit other insurance information for our records.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N156 </CODE><DESCRIPTION>Alert: The patient is responsible for the difference between the approved treatment and the elective treatment.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N157 </CODE><DESCRIPTION>Transportation to/from this destination is not covered.<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>N158 </CODE><DESCRIPTION>Transportation in a vehicle other than an ambulance is not covered.</DESCRIPTION>

<CODE>N159 </CODE><DESCRIPTION>Payment denied/reduced because mileage is not covered when the patient is not in the ambulance.</DESCRIPTION>

<CODE>N160 </CODE><DESCRIPTION>The patient must choose an option before a payment can be made for this procedure/ equipment/ supply/ service.<br /><i>Note: (Modified 2/1/04)</i></DESCRIPTION>

<CODE>N161 </CODE><DESCRIPTION>This drug/service/supply is covered only when the associated service is covered.</DESCRIPTION>

<CODE>N162 </CODE><DESCRIPTION>Alert: Although your claim was paid, you have billed for a test/specialty not included in your Laboratory Certification.  Your failure to correct the laboratory certification information will result in a denial of payment in the near future.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N163 </CODE><DESCRIPTION>Medical record does not support code billed per the code definition.</DESCRIPTION>

<CODE>N167 </CODE><DESCRIPTION>Charges exceed the post-transplant coverage limit.</DESCRIPTION>

<CODE>N170 </CODE><DESCRIPTION>A new/revised/renewed certificate of medical necessity is needed.</DESCRIPTION>

<CODE>N171 </CODE><DESCRIPTION>Payment for repair or replacement is not covered or has exceeded the purchase price.</DESCRIPTION>

<CODE>N172 </CODE><DESCRIPTION>The patient is not liable for the denied/adjusted charge(s) for receiving any updated service/item.</DESCRIPTION>

<CODE>N173 </CODE><DESCRIPTION>No qualifying hospital stay dates were provided for this episode of care.</DESCRIPTION>

<CODE>N174 </CODE><DESCRIPTION>This is not a covered service/procedure/ equipment/bed, however patient liability is limited to amounts shown in the adjustments under group 'PR'.</DESCRIPTION>

<CODE>N175 </CODE><DESCRIPTION>Missing review organization approval.<br /><i>Note: (Modified 8/1/04, 2/29/08) Related to N241</i></DESCRIPTION>

<CODE>N176 </CODE><DESCRIPTION>Services provided aboard a ship are covered only when the ship is of United States registry and is in United States waters. In addition, a doctor licensed to practice in the United States must provide the service.</DESCRIPTION>

<CODE>N177 </CODE><DESCRIPTION>Alert: We did not send this claim to patient's other insurer. They have indicated no additional payment can be made.<br /><i>Note: (Modified 6/30/03, 4/1/07)</i></DESCRIPTION>

<CODE>N178 </CODE><DESCRIPTION>Missing pre-operative photos or visual field results.<br /><i>Note: (Modified 8/1/04) Related to N244</i></DESCRIPTION>

<CODE>N179 </CODE><DESCRIPTION>Additional information has been requested from the member.  The charges will be reconsidered upon receipt of that information.</DESCRIPTION>

<CODE>N180 </CODE><DESCRIPTION>This item or service does not meet the criteria for the category under which it was billed.</DESCRIPTION>

<CODE>N181 </CODE><DESCRIPTION>Additional information is required from another provider involved in this service.<br /><i>Note: (Modified 12/1/06)</i></DESCRIPTION>

<CODE>N182 </CODE><DESCRIPTION>This claim/service must be billed according to the schedule for this plan.</DESCRIPTION>

<CODE>N183 </CODE><DESCRIPTION>Alert: This is a predetermination advisory message, when this service is submitted for payment additional documentation as specified in plan documents will be required to process benefits.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N184 </CODE><DESCRIPTION>Rebill technical and professional components separately.</DESCRIPTION>

<CODE>N185 </CODE><DESCRIPTION>Alert: Do not resubmit this claim/service.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N186 </CODE><DESCRIPTION>Non-Availability Statement (NAS) required for this service. Contact the nearest Military Treatment Facility (MTF) for assistance.</DESCRIPTION>

<CODE>N187 </CODE><DESCRIPTION>Alert: You may request a review in writing within the required time limits following receipt of this notice by following the instructions included in your contract or plan benefit documents.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N188 </CODE><DESCRIPTION>The approved level of care does not match the procedure code submitted.</DESCRIPTION>

<CODE>N189 </CODE><DESCRIPTION>Alert: This service has been paid as a one-time exception to the plan's benefit restrictions.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N190 </CODE><DESCRIPTION>Missing contract indicator.<br /><i>Note: (Modified 8/1/04) Related to N229</i></DESCRIPTION>

<CODE>N191 </CODE><DESCRIPTION>The provider must update insurance information directly with payer.</DESCRIPTION>

<CODE>N192 </CODE><DESCRIPTION>Patient is a Medicaid/Qualified Medicare Beneficiary.</DESCRIPTION>

<CODE>N193 </CODE><DESCRIPTION>Specific federal/state/local program may cover this service through another payer.</DESCRIPTION>

<CODE>N194 </CODE><DESCRIPTION>Technical component not paid if provider does not own the equipment used.</DESCRIPTION>

<CODE>N195 </CODE><DESCRIPTION>The technical component must be billed separately.</DESCRIPTION>

<CODE>N196 </CODE><DESCRIPTION>Alert: Patient eligible to apply for other coverage which may be primary.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N197 </CODE><DESCRIPTION>The subscriber must update insurance information directly with payer.</DESCRIPTION>

<CODE>N198 </CODE><DESCRIPTION>Rendering provider must be affiliated with the pay-to provider.</DESCRIPTION>

<CODE>N199 </CODE><DESCRIPTION>Additional payment/recoupment approved based on payer-initiated review/audit.<br /><i>Note: (Modified 8/1/06)</i></DESCRIPTION>

<CODE>N200 </CODE><DESCRIPTION>The professional component must be billed separately.</DESCRIPTION>

<CODE>N201 </CODE><DESCRIPTION>A mental health facility is responsible for payment of outside providers who furnish these services/supplies to residents.</DESCRIPTION>

<CODE>N202 </CODE><DESCRIPTION>Alert: Additional information/explanation will be sent separately<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N203 </CODE><DESCRIPTION>Missing/incomplete/invalid anesthesia time/units</DESCRIPTION>

<CODE>N204 </CODE><DESCRIPTION>Services under review for possible pre-existing condition. Send medical records for prior 12 months</DESCRIPTION>

<CODE>N205 </CODE><DESCRIPTION>Information provided was illegible</DESCRIPTION>

<CODE>N206 </CODE><DESCRIPTION>The supporting documentation does not match the claim</DESCRIPTION>

<CODE>N207 </CODE><DESCRIPTION>Missing/incomplete/invalid weight.<br /><i>Note: (Modified 11/18/05)</i></DESCRIPTION>

<CODE>N208 </CODE><DESCRIPTION>Missing/incomplete/invalid DRG code</DESCRIPTION>

<CODE>N209 </CODE><DESCRIPTION>Missing/invalid/incomplete taxpayer identification number (TIN)</DESCRIPTION>

<CODE>N210 </CODE><DESCRIPTION>Alert: You may appeal this decision<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N211 </CODE><DESCRIPTION>Alert: You may not appeal this decision<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N212 </CODE><DESCRIPTION>Charges processed under a Point of Service benefit </DESCRIPTION>

<CODE>N213 </CODE><DESCRIPTION>Missing/incomplete/invalid facility/discrete unit DRG/DRG exempt status information</DESCRIPTION>

<CODE>N214 </CODE><DESCRIPTION>Missing/incomplete/invalid history of the related initial surgical procedure(s)</DESCRIPTION>

<CODE>N215 </CODE><DESCRIPTION>Alert: A payer providing supplemental or secondary coverage shall not require a claims determination for this service from a primary payer as a condition of making its own claims determination.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N216 </CODE><DESCRIPTION>Patient is not enrolled in this portion of our benefit package</DESCRIPTION>

<CODE>N217 </CODE><DESCRIPTION>We pay only one site of service per provider per claim</DESCRIPTION>

<CODE>N218 </CODE><DESCRIPTION>You must furnish and service this item for as long as the patient continues to need it.  We can pay for maintenance and/or servicing for the time period specified in the contract or coverage manual.</DESCRIPTION>

<CODE>N219 </CODE><DESCRIPTION>Payment based on previous payer's allowed amount.</DESCRIPTION>

<CODE>N220 </CODE><DESCRIPTION>Alert: See the payer's web site or contact the payer's Customer Service department to obtain forms and instructions for filing a provider dispute.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N221 </CODE><DESCRIPTION>Missing Admitting History and Physical report.</DESCRIPTION>

<CODE>N222 </CODE><DESCRIPTION>Incomplete/invalid Admitting History and Physical report.</DESCRIPTION>

<CODE>N223 </CODE><DESCRIPTION>Missing documentation of benefit to the patient during initial treatment period.</DESCRIPTION>

<CODE>N224 </CODE><DESCRIPTION>Incomplete/invalid documentation of benefit to the patient during initial treatment period.</DESCRIPTION>

<CODE>N225 </CODE><DESCRIPTION>Incomplete/invalid documentation/orders/notes/summary/report/chart.<br /><i>Note: (Modified 8/1/05)</i></DESCRIPTION>

<CODE>N226 </CODE><DESCRIPTION>Incomplete/invalid American Diabetes Association Certificate of Recognition.</DESCRIPTION>

<CODE>N227 </CODE><DESCRIPTION>Incomplete/invalid Certificate of Medical Necessity.</DESCRIPTION>

<CODE>N228 </CODE><DESCRIPTION>Incomplete/invalid consent form.</DESCRIPTION>

<CODE>N229 </CODE><DESCRIPTION>Incomplete/invalid contract indicator.</DESCRIPTION>

<CODE>N230 </CODE><DESCRIPTION>Incomplete/invalid indication of whether the patient owns the equipment that requires the part or supply.</DESCRIPTION>

<CODE>N231 </CODE><DESCRIPTION>Incomplete/invalid invoice or statement certifying the actual cost of the lens, less discounts, and/or the type of intraocular lens used.</DESCRIPTION>

<CODE>N232 </CODE><DESCRIPTION>Incomplete/invalid itemized bill.</DESCRIPTION>

<CODE>N233 </CODE><DESCRIPTION>Incomplete/invalid operative report.</DESCRIPTION>

<CODE>N234 </CODE><DESCRIPTION>Incomplete/invalid oxygen certification/re-certification.</DESCRIPTION>

<CODE>N235 </CODE><DESCRIPTION>Incomplete/invalid pacemaker registration form.</DESCRIPTION>

<CODE>N236 </CODE><DESCRIPTION>Incomplete/invalid pathology report.</DESCRIPTION>

<CODE>N237 </CODE><DESCRIPTION>Incomplete/invalid patient medical record for this service.</DESCRIPTION>

<CODE>N238 </CODE><DESCRIPTION>Incomplete/invalid physician certified plan of care</DESCRIPTION>

<CODE>N239 </CODE><DESCRIPTION>Incomplete/invalid physician financial relationship form.</DESCRIPTION>

<CODE>N240 </CODE><DESCRIPTION>Incomplete/invalid radiology report.</DESCRIPTION>

<CODE>N241 </CODE><DESCRIPTION>Incomplete/invalid review organization approval.<br /><i>Note: (Modified 2/29/08)</i></DESCRIPTION>

<CODE>N242 </CODE><DESCRIPTION>Incomplete/invalid x-ray.</DESCRIPTION>

<CODE>N243 </CODE><DESCRIPTION>Incomplete/invalid/not approved screening document.</DESCRIPTION>

<CODE>N244 </CODE><DESCRIPTION>Incomplete/invalid pre-operative photos/visual field results.</DESCRIPTION>

<CODE>N245 </CODE><DESCRIPTION>Incomplete/invalid plan information for other insurance </DESCRIPTION>

<CODE>N246 </CODE><DESCRIPTION>State regulated patient payment limitations apply to this service.</DESCRIPTION>

<CODE>N247 </CODE><DESCRIPTION>Missing/incomplete/invalid assistant surgeon taxonomy.</DESCRIPTION>

<CODE>N248 </CODE><DESCRIPTION>Missing/incomplete/invalid assistant surgeon name.</DESCRIPTION>

<CODE>N249 </CODE><DESCRIPTION>Missing/incomplete/invalid assistant surgeon primary identifier.</DESCRIPTION>

<CODE>N250 </CODE><DESCRIPTION>Missing/incomplete/invalid assistant surgeon secondary identifier.</DESCRIPTION>

<CODE>N251 </CODE><DESCRIPTION>Missing/incomplete/invalid attending provider taxonomy.</DESCRIPTION>

<CODE>N252 </CODE><DESCRIPTION>Missing/incomplete/invalid attending provider name.</DESCRIPTION>

<CODE>N253 </CODE><DESCRIPTION>Missing/incomplete/invalid attending provider primary identifier.</DESCRIPTION>

<CODE>N254 </CODE><DESCRIPTION>Missing/incomplete/invalid attending provider secondary identifier.</DESCRIPTION>

<CODE>N255 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider taxonomy.</DESCRIPTION>

<CODE>N256 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider/supplier name.</DESCRIPTION>

<CODE>N257 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider/supplier primary identifier.</DESCRIPTION>

<CODE>N258 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider/supplier address.</DESCRIPTION>

<CODE>N259 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider/supplier secondary identifier.</DESCRIPTION>

<CODE>N260 </CODE><DESCRIPTION>Missing/incomplete/invalid billing provider/supplier contact information.</DESCRIPTION>

<CODE>N261 </CODE><DESCRIPTION>Missing/incomplete/invalid operating provider name.</DESCRIPTION>

<CODE>N262 </CODE><DESCRIPTION>Missing/incomplete/invalid operating provider primary identifier.</DESCRIPTION>

<CODE>N263 </CODE><DESCRIPTION>Missing/incomplete/invalid operating provider secondary identifier.</DESCRIPTION>

<CODE>N264 </CODE><DESCRIPTION>Missing/incomplete/invalid ordering provider name.</DESCRIPTION>

<CODE>N265 </CODE><DESCRIPTION>Missing/incomplete/invalid ordering provider primary identifier.</DESCRIPTION>

<CODE>N266 </CODE><DESCRIPTION>Missing/incomplete/invalid ordering provider address.</DESCRIPTION>

<CODE>N267 </CODE><DESCRIPTION>Missing/incomplete/invalid ordering provider secondary identifier.</DESCRIPTION>

<CODE>N268 </CODE><DESCRIPTION>Missing/incomplete/invalid ordering provider contact information.</DESCRIPTION>

<CODE>N269 </CODE><DESCRIPTION>Missing/incomplete/invalid other provider name.</DESCRIPTION>

<CODE>N270 </CODE><DESCRIPTION>Missing/incomplete/invalid other provider primary identifier.</DESCRIPTION>

<CODE>N271 </CODE><DESCRIPTION>Missing/incomplete/invalid other provider secondary identifier.</DESCRIPTION>

<CODE>N272 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer attending provider identifier.</DESCRIPTION>

<CODE>N273 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer operating provider identifier.</DESCRIPTION>

<CODE>N274 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer other provider identifier.</DESCRIPTION>

<CODE>N275 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer purchased service provider identifier.</DESCRIPTION>

<CODE>N276 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer referring provider identifier.</DESCRIPTION>

<CODE>N277 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer rendering provider identifier.</DESCRIPTION>

<CODE>N278 </CODE><DESCRIPTION>Missing/incomplete/invalid other payer service facility provider identifier.</DESCRIPTION>

<CODE>N279 </CODE><DESCRIPTION>Missing/incomplete/invalid pay-to provider name.</DESCRIPTION>

<CODE>N280 </CODE><DESCRIPTION>Missing/incomplete/invalid pay-to provider primary identifier.</DESCRIPTION>

<CODE>N281 </CODE><DESCRIPTION>Missing/incomplete/invalid pay-to provider address.</DESCRIPTION>

<CODE>N282 </CODE><DESCRIPTION>Missing/incomplete/invalid pay-to provider secondary identifier.</DESCRIPTION>

<CODE>N283 </CODE><DESCRIPTION>Missing/incomplete/invalid purchased service provider identifier.</DESCRIPTION>

<CODE>N284 </CODE><DESCRIPTION>Missing/incomplete/invalid referring provider taxonomy.</DESCRIPTION>

<CODE>N285 </CODE><DESCRIPTION>Missing/incomplete/invalid referring provider name.</DESCRIPTION>

<CODE>N286 </CODE><DESCRIPTION>Missing/incomplete/invalid referring provider primary identifier.</DESCRIPTION>

<CODE>N287 </CODE><DESCRIPTION>Missing/incomplete/invalid referring provider secondary identifier.</DESCRIPTION>

<CODE>N288 </CODE><DESCRIPTION>Missing/incomplete/invalid rendering provider taxonomy.</DESCRIPTION>

<CODE>N289 </CODE><DESCRIPTION>Missing/incomplete/invalid rendering provider name.</DESCRIPTION>

<CODE>N290 </CODE><DESCRIPTION>Missing/incomplete/invalid rendering provider primary identifier.</DESCRIPTION>

<CODE>N291 </CODE><DESCRIPTION>Missing/incomplete/invalid rending provider secondary identifier.</DESCRIPTION>

<CODE>N292 </CODE><DESCRIPTION>Missing/incomplete/invalid service facility name.</DESCRIPTION>

<CODE>N293 </CODE><DESCRIPTION>Missing/incomplete/invalid service facility primary identifier.</DESCRIPTION>

<CODE>N294 </CODE><DESCRIPTION>Missing/incomplete/invalid service facility primary address.</DESCRIPTION>

<CODE>N295 </CODE><DESCRIPTION>Missing/incomplete/invalid service facility secondary identifier.</DESCRIPTION>

<CODE>N296 </CODE><DESCRIPTION>Missing/incomplete/invalid supervising provider name.</DESCRIPTION>

<CODE>N297 </CODE><DESCRIPTION>Missing/incomplete/invalid supervising provider primary identifier.</DESCRIPTION>

<CODE>N298 </CODE><DESCRIPTION>Missing/incomplete/invalid supervising provider secondary identifier.</DESCRIPTION>

<CODE>N299 </CODE><DESCRIPTION>Missing/incomplete/invalid occurrence date(s).</DESCRIPTION>

<CODE>N300 </CODE><DESCRIPTION>Missing/incomplete/invalid occurrence span date(s).</DESCRIPTION>

<CODE>N301 </CODE><DESCRIPTION>Missing/incomplete/invalid procedure date(s).</DESCRIPTION>

<CODE>N302 </CODE><DESCRIPTION>Missing/incomplete/invalid other procedure date(s).</DESCRIPTION>

<CODE>N303 </CODE><DESCRIPTION>Missing/incomplete/invalid principal procedure date.</DESCRIPTION>

<CODE>N304 </CODE><DESCRIPTION>Missing/incomplete/invalid dispensed date.</DESCRIPTION>

<CODE>N305 </CODE><DESCRIPTION>Missing/incomplete/invalid accident date.</DESCRIPTION>

<CODE>N306 </CODE><DESCRIPTION>Missing/incomplete/invalid acute manifestation date.</DESCRIPTION>

<CODE>N307 </CODE><DESCRIPTION>Missing/incomplete/invalid adjudication or payment date.</DESCRIPTION>

<CODE>N308 </CODE><DESCRIPTION>Missing/incomplete/invalid appliance placement date.</DESCRIPTION>

<CODE>N309 </CODE><DESCRIPTION>Missing/incomplete/invalid assessment date.</DESCRIPTION>

<CODE>N310 </CODE><DESCRIPTION>Missing/incomplete/invalid assumed or relinquished care date.</DESCRIPTION>

<CODE>N311 </CODE><DESCRIPTION>Missing/incomplete/invalid authorized to return to work date.</DESCRIPTION>

<CODE>N312 </CODE><DESCRIPTION>Missing/incomplete/invalid begin therapy date.</DESCRIPTION>

<CODE>N313 </CODE><DESCRIPTION>Missing/incomplete/invalid certification revision date.</DESCRIPTION>

<CODE>N314 </CODE><DESCRIPTION>Missing/incomplete/invalid diagnosis date.</DESCRIPTION>

<CODE>N315 </CODE><DESCRIPTION>Missing/incomplete/invalid disability from date.</DESCRIPTION>

<CODE>N316 </CODE><DESCRIPTION>Missing/incomplete/invalid disability to date.</DESCRIPTION>

<CODE>N317 </CODE><DESCRIPTION>Missing/incomplete/invalid discharge hour.</DESCRIPTION>

<CODE>N318 </CODE><DESCRIPTION>Missing/incomplete/invalid discharge or end of care date.</DESCRIPTION>

<CODE>N319 </CODE><DESCRIPTION>Missing/incomplete/invalid hearing or vision prescription date.</DESCRIPTION>

<CODE>N320 </CODE><DESCRIPTION>Missing/incomplete/invalid Home Health Certification Period.</DESCRIPTION>

<CODE>N321 </CODE><DESCRIPTION>Missing/incomplete/invalid last admission period.</DESCRIPTION>

<CODE>N322 </CODE><DESCRIPTION>Missing/incomplete/invalid last certification date.</DESCRIPTION>

<CODE>N323 </CODE><DESCRIPTION>Missing/incomplete/invalid last contact date.</DESCRIPTION>

<CODE>N324 </CODE><DESCRIPTION>Missing/incomplete/invalid last seen/visit date.</DESCRIPTION>

<CODE>N325 </CODE><DESCRIPTION>Missing/incomplete/invalid last worked date.</DESCRIPTION>

<CODE>N326 </CODE><DESCRIPTION>Missing/incomplete/invalide last x-ray date.</DESCRIPTION>

<CODE>N327 </CODE><DESCRIPTION>Missing/incomplete/invalid other insured birth date.</DESCRIPTION>

<CODE>N328 </CODE><DESCRIPTION>Missing/incomplete/invalid Oxygen Saturation Test date.</DESCRIPTION>

<CODE>N329 </CODE><DESCRIPTION>Missing/incomplete/invalid patient birth date.</DESCRIPTION>

<CODE>N330 </CODE><DESCRIPTION>Missing/incomplete/invalid patient death date.</DESCRIPTION>

<CODE>N331 </CODE><DESCRIPTION>Missing/incomplete/invalid physician order date.</DESCRIPTION>

<CODE>N332 </CODE><DESCRIPTION>Missing/incomplete/invalid prior hospital discharge date.</DESCRIPTION>

<CODE>N333 </CODE><DESCRIPTION>Missing/incomplete/invalid prior placement date.</DESCRIPTION>

<CODE>N334 </CODE><DESCRIPTION>Missing/incomplete/invalid re-evaluation date</DESCRIPTION>

<CODE>N335 </CODE><DESCRIPTION>Missing/incomplete/invalid referral date.</DESCRIPTION>

<CODE>N336 </CODE><DESCRIPTION>Missing/incomplete/invalid replacement date.</DESCRIPTION>

<CODE>N337 </CODE><DESCRIPTION>Missing/incomplete/invalid secondary diagnosis date.</DESCRIPTION>

<CODE>N338 </CODE><DESCRIPTION>Missing/incomplete/invalid shipped date.</DESCRIPTION>

<CODE>N339 </CODE><DESCRIPTION>Missing/incomplete/invalid similar illness or symptom date.</DESCRIPTION>

<CODE>N340 </CODE><DESCRIPTION>Missing/incomplete/invalid subscriber birth date.</DESCRIPTION>

<CODE>N341 </CODE><DESCRIPTION>Missing/incomplete/invalid surgery date.</DESCRIPTION>

<CODE>N342 </CODE><DESCRIPTION>Missing/incomplete/invalid test performed date.</DESCRIPTION>

<CODE>N343 </CODE><DESCRIPTION>Missing/incomplete/invalid Transcutaneous Electrical Nerve Stimulator (TENS) trial start date.</DESCRIPTION>

<CODE>N344 </CODE><DESCRIPTION>Missing/incomplete/invalid Transcutaneous Electrical Nerve Stimulator (TENS) trial end date.</DESCRIPTION>

<CODE>N345 </CODE><DESCRIPTION>Date range not valid with units submitted. </DESCRIPTION>

<CODE>N346 </CODE><DESCRIPTION>Missing/incomplete/invalid oral cavity designation code.</DESCRIPTION>

<CODE>N347 </CODE><DESCRIPTION>Your claim for a referred or purchased service cannot be paid because payment has already been made for this same service to another provider by a payment contractor representing the payer. </DESCRIPTION>

<CODE>N348 </CODE><DESCRIPTION>You chose that this service/supply/drug would be rendered/supplied and billed by a different practitioner/supplier.</DESCRIPTION>

<CODE>N349 </CODE><DESCRIPTION>The administration method and drug must be reported to adjudicate this service. </DESCRIPTION>

<CODE>N350 </CODE><DESCRIPTION>Missing/incomplete/invalid description of service for a Not Otherwise Classified (NOC) code or an Unlisted procedure.</DESCRIPTION>

<CODE>N351 </CODE><DESCRIPTION>Service date outside of the approved treatment plan service dates.</DESCRIPTION>

<CODE>N352 </CODE><DESCRIPTION>Alert: There are no scheduled payments for this service. Submit a claim for each patient visit.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N353 </CODE><DESCRIPTION>Alert: Benefits have been estimated, when the actual services have been rendered, additional payment will be considered based on the submitted claim.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N354 </CODE><DESCRIPTION>Incomplete/invalid invoice</DESCRIPTION>

<CODE>N355 </CODE><DESCRIPTION>Alert: The law permits exceptions to the refund requirement in two cases: - If you did not know, and could not have reasonably been expected to know, that we would not pay for this service; or - If you notified the patient in writing before providing the service that you believed that we were likely to deny the service, and the patient signed a statement agreeing to pay for the service.<br/><br/>
If you come within either exception, or if you believe the carrier was wrong in its determination that we do not pay for this service, you should request appeal of this determination within 30 days of the date of this notice. Your request for review should include any additional information necessary to support your position.<br/><br/>
If you request an appeal within 30 days of receiving this notice, you may delay refunding the amount to the patient until you receive the results of the review. If the review decision is favorable to you, you do not need to make any refund. If, however, the review is unfavorable, the law specifies that you must make the refund within 15 days of receiving the unfavorable review decision.<br/><br/>
The law also permits you to request an appeal at any time within 120 days of the date you receive this notice. However, an appeal request that is received more than 30 days after the date of this notice, does not permit you to delay making the refund. Regardless of when a review is requested, the patient will be notified that you have requested one, and will receive a copy of the determination.<br/><br/>
The patient has received a separate notice of this denial decision. The notice advises that he/she may be entitled to a refund of any amounts paid, if you should have known that we would not pay and did not tell him/her. It also instructs the patient to contact our office if he/she does not hear anything about a refund within 30 days<br /><i>Note: (Modified 11/18/05, Modified 4/1/07)</i></DESCRIPTION>

<CODE>N356 </CODE><DESCRIPTION>This service is not covered when performed with, or subsequent to, a non-covered service.</DESCRIPTION>

<CODE>N357 </CODE><DESCRIPTION>Time frame requirements between this service/procedure/supply and a related service/procedure/supply have not been met.</DESCRIPTION>

<CODE>N358 </CODE><DESCRIPTION>Alert: This decision may be reviewed if additional documentation as described in the contract or plan benefit documents is submitted.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N359 </CODE><DESCRIPTION>Missing/incomplete/invalid height.</DESCRIPTION>

<CODE>N360 </CODE><DESCRIPTION>Alert: Coordination of benefits has not been calculated when estimating benefits for this pre-determination. Submit payment information from the primary payer with the secondary claim.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N362 </CODE><DESCRIPTION>The number of Days or Units of Service exceeds our acceptable maximum.</DESCRIPTION>

<CODE>N363 </CODE><DESCRIPTION>Alert: in the near future we are implementing new policies/procedures that would affect this determination.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N364 </CODE><DESCRIPTION>Alert: According to our agreement, you must waive the deductible and/or coinsurance amounts.<br /><i>Note: (Modified 4/1/07)</i></DESCRIPTION>

<CODE>N365 </CODE><DESCRIPTION>This procedure code is not payable. It is for reporting/information purposes only.</DESCRIPTION>

<CODE>N366 </CODE><DESCRIPTION>Requested information not provided. The claim will be reopened if the information previously requested is submitted within one year after the date of this denial notice.</DESCRIPTION>

<CODE>N367 </CODE><DESCRIPTION>Alert: The claim information has been forwarded to a Consumer Account Fund processor for review.<br /><i>Note: (Modified 4/1/07, 11/5/07)</i></DESCRIPTION>

<CODE>N368 </CODE><DESCRIPTION>You must appeal the determination of the previously adjudicated claim.</DESCRIPTION>

<CODE>N369 </CODE><DESCRIPTION>Alert: Although this claim has been processed, it is deficient according to state legislation/regulation.</DESCRIPTION>

<CODE>N370 </CODE><DESCRIPTION>Billing exceeds the rental months covered/approved by the payer.</DESCRIPTION>

<CODE>N371 </CODE><DESCRIPTION>Alert: title of this equipment must be transferred to the patient.</DESCRIPTION>

<CODE>N372 </CODE><DESCRIPTION>Only reasonable and necessary maintenance/service charges are covered.</DESCRIPTION>

<CODE>N373 </CODE><DESCRIPTION>It has been determined that another payer paid the services as primary when they were not the primary payer. Therefore, we are refunding to the payer that paid as primary on your behalf.</DESCRIPTION>

<CODE>N374 </CODE><DESCRIPTION>Primary Medicare Part A insurance has been exhausted and a Part B Remittance Advice is required.</DESCRIPTION>

<CODE>N375 </CODE><DESCRIPTION>Missing/incomplete/invalid questionnaire/information required to determine dependent eligibility.</DESCRIPTION>

<CODE>N376 </CODE><DESCRIPTION>Subscriber/patient is assigned to active military duty, therefore primary coverage may be TRICARE.</DESCRIPTION>

<CODE>N377 </CODE><DESCRIPTION>Payment based on a processed replacement claim.<br /><i>Note: (Modified 11/5/07)</i></DESCRIPTION>

<CODE>N378 </CODE><DESCRIPTION>Missing/incomplete/invalid prescription quantity.</DESCRIPTION>

<CODE>N379 </CODE><DESCRIPTION>Claim level information does not match line level information.</DESCRIPTION>

<CODE>N380 </CODE><DESCRIPTION>The original claim  has been processed, submit a corrected claim.</DESCRIPTION>

<CODE>N381 </CODE><DESCRIPTION>Consult our contractual agreement for restrictions/billing/payment information related to these charges.</DESCRIPTION>

<CODE>N382 </CODE><DESCRIPTION>Missing/incomplete/invalid patient identifier.</DESCRIPTION>

<CODE>N383 </CODE><DESCRIPTION>Services deemed cosmetic are not covered</DESCRIPTION>

<CODE>N384 </CODE><DESCRIPTION>Records indicate that the referenced body part/tooth has been removed in a previous procedure. </DESCRIPTION>

<CODE>N385 </CODE><DESCRIPTION>Notification of admission was not timely according to published plan procedures.<br /><i>Note: (Modified 11/5/07)</i></DESCRIPTION>

<CODE>N386 </CODE><DESCRIPTION>This decision was based on a National Coverage Determination (NCD).  An NCD provides a coverage determination as to whether a particular item or service is covered. A copy of this policy is available at http://www.cms.hhs.gov/mcd/search.asp. If you do not have web access, you may contact the contractor to request a copy of the NCD.</DESCRIPTION>

<CODE>N387 </CODE><DESCRIPTION>You should submit this claim to the patient's other insurer for potential payment of supplemental benefits. We did not forward the claim information.</DESCRIPTION>

<CODE>N388 </CODE><DESCRIPTION>Missing/incomplete/invalid prescription number</DESCRIPTION>

<CODE>N389 </CODE><DESCRIPTION>Duplicate prescription number submitted.</DESCRIPTION>

<CODE>N390 </CODE><DESCRIPTION>This service cannot be billed separately.</DESCRIPTION>

<CODE>N391 </CODE><DESCRIPTION>Missing emergency department records.</DESCRIPTION>

<CODE>N392 </CODE><DESCRIPTION>Incomplete/invalid emergency department records.</DESCRIPTION>

<CODE>N393 </CODE><DESCRIPTION>Missing progress notes or report.   </DESCRIPTION>

<CODE>N394 </CODE><DESCRIPTION>Incomplete/invalid progress notes or report.    </DESCRIPTION>

<CODE>N395 </CODE><DESCRIPTION>Missing laboratory report.</DESCRIPTION>

<CODE>N396 </CODE><DESCRIPTION>Incomplete/invalid laboratory report.</DESCRIPTION>

<CODE>N397 </CODE><DESCRIPTION>Benefits are not available for incomplete service(s)/undelivered item(s).</DESCRIPTION>

<CODE>N398 </CODE><DESCRIPTION>Missing elective consent form.</DESCRIPTION>

<CODE>N399 </CODE><DESCRIPTION>Incomplete/invalid elective consent form.</DESCRIPTION>

<CODE>N400 </CODE><DESCRIPTION>Alert: Electronically enabled providers should submit claims electronically.</DESCRIPTION>

<CODE>N401 </CODE><DESCRIPTION>Missing periodontal charting. </DESCRIPTION>

<CODE>N402 </CODE><DESCRIPTION>Incomplete/invalid periodontal charting.</DESCRIPTION>

<CODE>N403 </CODE><DESCRIPTION>Missing facility certification.</DESCRIPTION>

<CODE>N404 </CODE><DESCRIPTION>Incomplete/invalid facility certification.</DESCRIPTION>

<CODE>N405 </CODE><DESCRIPTION>This service is only covered when the donor's insurer(s) do not provide coverage for the service.</DESCRIPTION>

<CODE>N406 </CODE><DESCRIPTION>This service is only covered when the recipient's insurer(s) do not provide coverage for the service.</DESCRIPTION>

<CODE>N407 </CODE><DESCRIPTION>You are not an approved submitter for this transmission format.</DESCRIPTION>

<CODE>N408 </CODE><DESCRIPTION>This payer does not cover deductibles assessed by a previous payer. </DESCRIPTION>

<CODE>N409 </CODE><DESCRIPTION>This service is related to an accidental injury and is not covered unless provided within a specific time frame from the date of the accident. </DESCRIPTION>

<CODE>N410 </CODE><DESCRIPTION>This is not covered unless the prescription changes.</DESCRIPTION>

<CODE>N418 </CODE><DESCRIPTION>Misrouted claim.  See the payer's claim submission instructions.</DESCRIPTION>

<CODE>N419 </CODE><DESCRIPTION>Claim payment was the result of a payer's retroactive adjustment due to a retroactive rate change.</DESCRIPTION>

<CODE>N420 </CODE><DESCRIPTION>Claim payment was the result of a payer's retroactive adjustment due to a Coordination of Benefits or Third Party Liability Recovery.</DESCRIPTION>

<CODE>N421 </CODE><DESCRIPTION>Claim payment was the result of a payer's retrocative adjustment due to a review organization decision.<br /><i>Note: (Modified 2/29/08)</i></DESCRIPTION>

<CODE>N422 </CODE><DESCRIPTION>Claim payment was the result of a payer's retrocative adjustment due to a payer's contract incentive program.</DESCRIPTION>

<CODE>N423 </CODE><DESCRIPTION>Claim payment was the result of a payer's retroactive adjustment due to a non standard program.</DESCRIPTION>

<CODE>N424 </CODE><DESCRIPTION>Patient does not reside in the geographic area required for this type of payment.</DESCRIPTION>

<CODE>N425 </CODE><DESCRIPTION>Statutorily excluded service(s).</DESCRIPTION>

<CODE>N426 </CODE><DESCRIPTION>No coverage when self-administered.</DESCRIPTION>

<CODE>N427 </CODE><DESCRIPTION>Payment for eyeglasses or contact lenses can be made only after cataract surgery.</DESCRIPTION>

<CODE>N428 </CODE><DESCRIPTION>Service/procedure not covered when performed in this place of service.</DESCRIPTION>

<CODE>N429 </CODE><DESCRIPTION>This is not covered since it is considered routine.</DESCRIPTION>

<CODE>N430 </CODE><DESCRIPTION>Procedure code is inconsistent with the units billed.</DESCRIPTION>

<CODE>N431 </CODE><DESCRIPTION>Service is not covered with this procedure.</DESCRIPTION>

<CODE>N432 </CODE><DESCRIPTION>Adjustment based on a Recovery Audit.</DESCRIPTION>

<CODE>N433 </CODE><DESCRIPTION>Resubmit this claim using only your National Provider Identifier (NPI)</DESCRIPTION>
</remarks>
"""

__remarks = __get_remarks()

__car2str_map = { 
      "1" : "Deductible Amount",
      "2" : "Coinsurance Amount",
      "3" : "Co-payment Amount",
      "4" : "The procedure code is inconsistent with the modifier used or a required modifier is missing.",
      "5" : "The procedure code/bill type is inconsistent with the place of service.",
      "6" : "The procedure/revenue code is inconsistent with the patient's age.",
      "7" : "The procedure/revenue code is inconsistent with the patient's gender.",
      "8" : "The procedure code is inconsistent with the provider type/specialty (taxonomy).",
      "9" : "The diagnosis is inconsistent with the patient's age.",
      "10" : "The diagnosis is inconsistent with the patient's gender.",
      "11" : "The diagnosis is inconsistent with the procedure.",
      "12" : "The diagnosis is inconsistent with the provider type.",
      "13" : "The date of death precedes the date of service.",
      "14" : "The date of birth follows the date of service.",
      "15" : "Payment adjusted because the submitted authorization number is missing, invalid, or does not apply to the billed services or provider.",
      "16" : "Claim/service lacks information which is needed for adjudication. Additional information is supplied using remittance advice remarks codes whenever appropriate",
      "17" : "Payment adjusted because requested information was not provided or was insufficient/incomplete. Additional information is supplied using the remittance advice remarks codes whenever appropriate.",
      "18" : "Duplicate claim/service.",
      "19" : "Claim denied because this is a work-related injury/illness and thus the liability of the Worker's Compensation Carrier.",
      "20" : "Claim denied because this injury/illness is covered by the liability carrier.",
      "21" : "Claim denied because this injury/illness is the liability of the no-fault carrier.",
      "22" : "Payment adjusted because this care may be covered by another payer per coordination of benefits.",
      "23" : "Payment adjusted because charges have been paid by another payer.",
      "24" : "Payment for charges adjusted. Charges are covered under a capitation agreement/managed care plan.",
      "25" : "Payment denied. Your Stop loss deductible has not been met.",
      "26" : "Expenses incurred prior to coverage.",
      "27" : "Expenses incurred after coverage terminated.",
      "28" : "Coverage not in effect at the time the service was provided.",
      "29" : "The time limit for filing has expired.",
      "30" : "Payment adjusted because the patient has not met the required eligibility, spend down, waiting, or residency requirements.",
      "31" : "Claim denied as patient cannot be identified as our insured.",
      "32" : "Our records indicate that this dependent is not an eligible dependent as defined.",
      "33" : "Claim denied. Insured has no dependent coverage.",
      "34" : "Claim denied. Insured has no coverage for newborns.",
      "35" : "Lifetime benefit maximum has been reached.",
      "36" : "Balance does not exceed co-payment amount.",
      "37" : "Balance does not exceed deductible.",
      "38" : "Services not provided or authorized by designated (network/primary care) providers.",
      "39" : "Services denied at the time authorization/pre-certification was requested.",
      "40" : "Charges do not meet qualifications for emergent/urgent care.",
      "41" : "Discount agreed to in Preferred Provider contract.",
      "42" : "Charges exceed our fee schedule or maximum allowable amount.",
      "43" : "Gramm-Rudman reduction.",
      "44" : "Prompt-pay discount.",
      "45" : "Charges exceed your contracted/ legislated fee arrangement.",
      "46" : "This (these) service(s) is (are) not covered.",
      "47" : "This (these) diagnosis(es) is (are) not covered, missing, or are invalid.",
      "48" : "This (these) procedure(s) is (are) not covered.",
      "49" : "These are non-covered services because this is a routine exam or screening procedure done in conjunction with a routine exam.",
      "50" : "These are non-covered services because this is not deemed a `medical necessity' by the payer.",
      "51" : "These are non-covered services because this is a pre-existing condition",
      "52" : "The referring/prescribing/rendering provider is not eligible to refer/prescribe/order/perform the service billed.",
      "53" : "Services by an immediate relative or a member of the same household are not covered.",
      "54" : "Multiple physicians/assistants are not covered in this case .",
      "55" : "Claim/service denied because procedure/treatment is deemed experimental/investigational by the payer.",
      "56" : "Claim/service denied because procedure/treatment has not been deemed `proven to be effective' by the payer.",
      "57" : "Payment denied/reduced because the payer deems the information submitted does not support this level of service, this many services, this length of service, this dosage, or this day's supply.",
      "58" : "Payment adjusted because treatment was deemed by the payer to have been rendered in an inappropriate or invalid place of service.",
      "59" : "Charges are adjusted based on multiple surgery rules or concurrent anesthesia rules.",
      "60" : "Charges for outpatient services with this proximity to inpatient services are not covered.",
      "61" : "Charges adjusted as penalty for failure to obtain second surgical opinion.",
      "62" : "Payment denied/reduced for absence of, or exceeded, pre-certification/authorization.",
      "63" : "Correction to a prior claim.",
      "64" : "Denial reversed per Medical Review.",
      "65" : "Procedure code was incorrect. This payment reflects the correct code.",
      "66" : "Blood Deductible.",
      "67" : "Lifetime reserve days. (Handled in QTY, QTY01=LA)",
      "68" : "DRG weight. (Handled in CLP12)",
      "69" : "Day outlier amount.",
      "70" : "Cost outlier - Adjustment to compensate for additonal costs.",
      "71" : "Primary Payer amount.",
      "72" : "Coinsurance day. (Handled in QTY, QTY01=CD)",
      "73" : "Administrative days.",
      "74" : "Indirect Medical Education Adjustment.",
      "75" : "Direct Medical Education Adjustment.",
      "76" : "Disproportionate Share Adjustment.",
      "77" : "Covered days. (Handled in QTY, QTY01=CA)",
      "78" : "Non-Covered days/Room charge adjustment.",
      "79" : "Cost Report days. (Handled in MIA15)",
      "80" : "Outlier days. (Handled in QTY, QTY01=OU)",
      "81" : "Discharges.",
      "82" : "PIP days.",
      "83" : "Total visits.",
      "84" : "Capital Adjustment. (Handled in MIA)",
      "85" : "Interest amount.",
      "86" : "Statutory Adjustment.",
      "87" : "Transfer amount.",
      "88" : "Adjustment amount represents collection against receivable created in prior overpayment.",
      "89" : "Professional fees removed from charges.",
      "90" : "Ingredient cost adjustment.",
      "91" : "Dispensing fee adjustment.",
      "92" : "Claim Paid in full.",
      "93" : "No Claim level Adjustments.",
      "94" : "Processed in Excess of charges.",
      "95" : "Benefits adjusted. Plan procedures not followed.",
      "96" : "Non-covered charge(s).",
      "97" : "Payment is included in the allowance for another service/procedure.",
      "98" : "The hospital must file the Medicare claim for this inpatient non-physician service.",
      "99" : "Medicare Secondary Payer Adjustment Amount.",
      "100" : "Payment made to patient/insured/responsible party.",
      "101" : "Predetermination: anticipated payment upon completion of services or claim adjudication.",
      "102" : "Major Medical Adjustment.",
      "103" : "Provider promotional discount (e.g., Senior citizen discount).",
      "104" : "Managed care withholding.",
      "105" : "Tax withholding.",
      "106" : "Patient payment option/election not in effect.",
      "107" : "Claim/service denied because the related or qualifying claim/service was not previously paid or identified on this claim.",
      "108" : "Payment adjusted because rent/purchase guidelines were not met.",
      "109" : "Claim not covered by this payer/contractor. You must send the claim to the correct payer/contractor.",
      "110" : "Billing date predates service date.",
      "111" : "Not covered unless the provider accepts assignment.",
      "112" : "Payment adjusted as not furnished directly to the patient and/or not documented.",
      "113" : "Payment denied because service/procedure was provided outside the United States or as a result of war.",
      "114" : "Procedure/product not approved by the Food and Drug Administration.",
      "115" : "Payment adjusted as procedure postponed or canceled.",
      "116" : "Payment denied. The advance indemnification notice signed by the patient did not comply with requirements.",
      "117" : "Payment adjusted because transportation is only covered to the closest facility that can provide the necessary care.",
      "118" : "Charges reduced for ESRD network support.",
      "119" : "Benefit maximum for this time period has been reached.",
      "120" : "Patient is covered by a managed care plan.",
      "121" : "Indemnification adjustment.",
      "122" : "Psychiatric reduction.",
      "123" : "Payer refund due to overpayment.",
      "124" : "Payer refund amount - not our patient.",
      "125" : "Payment adjusted due to a submission/billing error(s). Additional information is supplied using the remittance advice remarks codes whenever appropriate.",
      "126" : "Deductible -- Major Medical",
      "127" : "Coinsurance -- Major Medical",
      "128" : "Newborn's services are covered in the mother's Allowance.",
      "129" : "Payment denied - Prior processing information appears incorrect.",
      "130" : "Claim submission fee.",
      "131" : "Claim specific negotiated discount.",
      "132" : "Prearranged demonstration project adjustment.",
      "133" : "The disposition of this claim/service is pending further review.",
      "134" : "Technical fees removed from charges.",
      "135" : "Claim denied. Interim bills cannot be processed.",
      "136" : "Claim Adjusted. Plan procedures of a prior payer were not followed.",
      "137" : "Payment/Reduction for Regulatory Surcharges, Assessments, Allowances or Health Related Taxes.",
      "138" : "Claim/service denied. Appeal procedures not followed or time limits not met.",
      "139" : "Contracted funding agreement - Subscriber is employed by the provider of services.",
      "140" : "Patient/Insured health identification number and name do not match.",
      "141" : "Claim adjustment because the claim spans eligible and ineligible periods of coverage.",
      "142" : "Claim adjusted by the monthly Medicaid patient liability amount.",
      "143" : "Portion of payment deferred.",
      "144" : "Incentive adjustment, e.g. preferred product/service.",
      "145" : "Premium payment withholding",
      "146" : "Payment denied because the diagnosis was invalid for the date(s) of service reported.",
      "147" : "Provider contracted/negotiated rate expired or not on file.",
      "148" : "Claim/service rejected at this time because information from another provider was not provided or was insufficient/incomplete.",
      "149" : "Lifetime benefit maximum has been reached for this service/benefit category.",
      "150" : "Payment adjusted because the payer deems the information submitted does not support this level of service.",
      "151" : "Payment adjusted because the payer deems the information submitted does not support this many services.",
      "152" : "Payment adjusted because the payer deems the information submitted does not support this length of service.",
      "153" : "Payment adjusted because the payer deems the information submitted does not support this dosage.",
      "154" : "Payment adjusted because the payer deems the information submitted does not support this day's supply.",
      "155" : "This claim is denied because the patient refused the service/procedure.",
      "156" : "Flexible spending account payments",
      "157" : "Payment denied/reduced because service/procedure was provided as a result of an act of war.",
      "158" : "Payment denied/reduced because the service/procedure was provided outside of the United States.",
      "159" : "Payment denied/reduced because the service/procedure was provided as a result of terrorism.",
      "160" : "Payment denied/reduced because injury/illness was the result of an activity that is a benefit exclusion.",
      "A0" : "Patient refund amount.",
      "A1" : "Claim denied charges.",
      "A2" : "Contractual adjustment.",
      "A3" : "Medicare Secondary Payer liability met.",
      "A4" : "Medicare Claim PPS Capital Day Outlier Amount.",
      "A5" : "Medicare Claim PPS Capital Cost Outlier Amount.",
      "A6" : "Prior hospitalization or 30 day transfer requirement not met.",
      "A7" : "Presumptive Payment Adjustment",
      "A8" : "Claim denied; ungroupable DRG",
      "B1" : "Non-covered visits.",
      "B2" : "Covered visits.",
      "B3" : "Covered charges.",
      "B4" : "Late filing penalty.",
      "B5" : "Payment adjusted because coverage/program guidelines were not met or were exceeded.",
      "B6" : "This payment is adjusted when performed/billed by this type of provider, by this type of provider in this type of facility, or by a provider of this specialty.",
      "B7" : "This provider was not certified/eligible to be paid for this procedure/service on this date of service.",
      "B8" : "Claim/service not covered/reduced because alternative services were available, and should have been utilized.",
      "B9" : "Services not covered because the patient is enrolled in a Hospice.",
      "B10" : "Allowed amount has been reduced because a component of the basic procedure/test was paid. The beneficiary is not liable for more than the charge limit for the basic procedure/test.",
      "B11" : "The claim/service has been transferred to the proper payer/processor for processing. Claim/service not covered by this payer/processor.",
      "B12" : "Services not documented in patients' medical records.",
      "B13" : "Previously paid. Payment for this claim/service may have been provided in a previous payment.",
      "B14" : "Payment denied because only one visit or consultation per physician per day is covered.",
      "B15" : "Payment adjusted because this procedure/service is not paid separately.",
      "B16" : "Payment adjusted because `New Patient' qualifications were not met.",
      "B17" : "Payment adjusted because this service was not prescribed by a physician, not prescribed prior to delivery, the prescription is incomplete, or the prescription is not current.",
      "B18" : "Payment denied because this procedure code/modifier was invalid on the date of service or claim submission.",
      "B19" : "Claim/service adjusted because of the finding of a Review Organization.",
      "B20" : "Payment adjusted because procedure/service was partially or fully furnished by another provider.",
      "B21" : "The charges were reduced because the service/care was partially furnished by another physician.",
      "B22" : "This payment is adjused based on the diagnosis.",
      "B23" : "Payment denied because this provider has failed an aspect of a proficiency testing program.",
      "D1" : "Claim/service denied. Level of subluxation is missing or inadequate.",
      "D2" : "Claim lacks the name, strength, or dosage of the drug furnished.",
      "D3" : "Claim/service denied because information to indicate if the patient owns the equipment that requires the part or supply was missing.",
      "D4" : "Claim/service does not indicate the period of time for which this will be needed.",
      "D5" : "Claim/service denied. Claim lacks individual lab codes included in the test.",
      "D6" : "Claim/service denied. Claim did not include patient's medical record for the service.",
      "D7" : "Claim/service denied. Claim lacks date of patient's most recent physician visit.",
      "D8" : "Claim/service denied. Claim lacks indicator that `x-ray is available for review.'",
      "D9" : "Claim/service denied. Claim lacks invoice or statement certifying the actual cost of the lens, less discounts or the type of intraocular lens used.",
      "D10" : "Claim/service denied. Completed physician financial relationship form not on file.",
      "D11" : "Claim lacks completed pacemaker registration form.",
      "D12" : "Claim/service denied. Claim does not identify who performed the purchased diagnostic test or the amount you were charged for the test.",
      "D13" : "Claim/service denied. Performed by a facility/supplier in which the ordering/referring physician has a financial interest.",
      "D14" : "Claim lacks indication that plan of treatment is on file.",
      "D15" : "Claim lacks indication that service was supervised or evaluated by a physician.",
      "W1" : "Workers Compensation State Fee Schedule Adjustment" }

def ClaimAdjustmentReasonToStr(code):
    try:
        return __car2str_map[code]
    except KeyError:
        return "UNKNOWN CODE!"

def RemarkCodeToStr(code_list, code):
    try:
        return __remarks[code]
    except KeyError:
        return "UNKNOWN CODE!"

__claim_status_map = { "0": "UNDEFINED",
              "1" : "Processed as Primary",
              "2" : "Processed as Secondary",
              "3" : "Processed as Tertiary",
              "4" : "Denied",
              "5" : "Pended",
              "10" : "Received, but not in process",
              "13" : "Suspended",
              "15" : "Suspended, investigation with field",
              "16" : "Suspended, return with material",
              "17" : "Suspended, review pending",
              "19" : "Procesed as Primary, Forwarded to Additional Payers",
              "20" : "Procesed as Secondary, Forwarded to Additional Payers",
              "21" : "Processed as Tertiary, Forwarded to Additional Payers",
              "22" : "Reversal of Previous Payment",
              "23" : "Not Our Claim, Forwarded to Additional Payer(s)",
              "25" : "Predetermination Pricing Only - No Payment",
              "27" : "something bad"
              }
def CLPStatusCodeToStr(code):
    return __claim_status_map[code]

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        if sys.argv[1] == "--todbf":
            import dbf
            fname = sys.argv[2]

            db = dbf.create( fname, 
                     [ ( "CODE",     "C", 5,  0, False ),
                       ( "DESC",     "C", 254,  0, False ),
                       ] )

            for code, description in __remarks.items():
                db.append_blank()
                db["CODE"] = code
                db["DESC"] = description[:254]

    else:
        print remarks

