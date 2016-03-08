# downloaded on Mar 7, 2016
# http://www.wpc-edi.com/reference/codelists/healthcare/remittance-advice-remark-codes/
REMITTANCE_ADVICE_REMARK_CODES_RAW = """
<remarks>
<tr class="prod_set current"><td class="code">M1</td><td class="description">X-ray not taken within the past 12 months or near enough to the start of treatment.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M2</td><td class="description">Not paid separately when the patient is an inpatient.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M3</td><td class="description">Equipment is the same or similar to equipment already being used.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M4</td><td class="description">Alert: This is the last monthly installment payment for this durable medical equipment.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M5</td><td class="description">Monthly rental payments can continue until the earlier of the 15th month from the first rental month, or the month when the equipment is no longer needed.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M6</td><td class="description">Alert: You must furnish and service this item for any period of medical need for the remainder of the reasonable useful lifetime of the equipment.<br />Start: 01/01/1997 | Last Modified: 03/01/2009<br />Notes: (Modified 4/1/07, 3/1/2009)</td></tr>

<tr class="prod_set current"><td class="code">M7</td><td class="description">No rental payments after the item is purchased, or after the total of issued rental payments equals the purchase price.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M8</td><td class="description">We do not accept blood gas tests results when the test was conducted by a medical supplier or taken while the patient is on oxygen.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M9</td><td class="description">Alert: This is the tenth rental month. You must offer the patient the choice of changing the rental to a purchase agreement.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M10</td><td class="description">Equipment purchases are limited to the first or the tenth month of medical necessity.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M11</td><td class="description">DME, orthotics and prosthetics must be billed to the DME carrier who services the patient's zip code.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M12</td><td class="description">Diagnostic tests performed by a physician must indicate whether purchased services are included on the claim.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M13</td><td class="description">Only one initial visit is covered per specialty per medical group.<br />Start: 01/01/1997 | Last Modified: 06/30/2007<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">M14</td><td class="description">No separate payment for an injection administered during an office visit, and no payment for a full office visit if the patient only received an injection.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M15</td><td class="description">Separately billed services/tests have been bundled as they are considered components of the same procedure. Separate payment is not allowed.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M16</td><td class="description">Alert: Please see our web site, mailings, or bulletins for more details concerning this policy/procedure/decision.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Reactivated 4/1/04, Modified 11/18/05, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M17</td><td class="description">Alert: Payment approved as you did not know, and could not reasonably have been expected to know, that this would not normally have been covered for this patient.  In the future, you will be liable for charges for the same service(s) under the same or similar conditions.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M18</td><td class="description">Certain services may be approved for home use.  Neither a hospital nor a Skilled Nursing Facility (SNF) is considered to be a patient's home.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">M19</td><td class="description">Missing oxygen certification/re-certification.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N234</td></tr>

<tr class="prod_set current"><td class="code">M20</td><td class="description">Missing/incomplete/invalid HCPCS.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M21</td><td class="description">Missing/incomplete/invalid place of residence for this service/item provided in a home.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M22</td><td class="description">Missing/incomplete/invalid number of miles traveled.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M23</td><td class="description">Missing invoice.<br />Start: 01/01/1997 | Last Modified: 08/01/2005<br />Notes: (Modified 8/1/05)</td></tr>

<tr class="prod_set current"><td class="code">M24</td><td class="description">Missing/incomplete/invalid number of doses per vial.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M25</td><td class="description">The information furnished does not substantiate the need for this level of service. If you believe the service should have been fully covered as billed, or if you did not know and could not reasonably have been expected to know that we would not pay for this level of service, or if you notified the patient in writing in advance that we would not pay for this level of service and he/she agreed in writing to pay, ask us to review your claim within 120 days of the date of this notice.  If you do not request an appeal, we will, upon application from the patient, reimburse him/her for the amount you have collected from him/her in excess of any deductible and coinsurance amounts. We will recover the reimbursement from you as an overpayment.<br />Start: 01/01/1997 | Last Modified: 11/01/2010<br />Notes: (Modified 10/1/02, 6/30/03, 8/1/05, 11/5/07, 11/1/10)</td></tr>

<tr class="prod_set current"><td class="code">M26</td><td class="description">The information furnished does not substantiate the need for this level of service. If you have collected any amount from the patient for this level of service /any amount that exceeds the limiting charge for the less extensive service, the law requires you to refund that amount to the patient within 30 days of receiving this notice. <br /><br />The requirements for refund are in 1824(I) of the Social Security Act and 42CFR411.408. The section specifies that physicians who knowingly and willfully fail to make appropriate refunds may be subject to civil monetary penalties and/or exclusion from the program. If you have any questions about this notice, please contact this office.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 10/1/02, 6/30/03, 8/1/05, 11/5/07. Also refer to N356)</td></tr>

<tr class="prod_set current"><td class="code">M27</td><td class="description">Alert: The patient has been relieved of liability of payment of these items and services under the limitation of liability provision of the law. The provider is ultimately liable for the patient's waived charges, including any charges for coinsurance, since the items or services were not reasonable and necessary or constituted custodial care, and you knew or could reasonably have been expected to know, that they were not covered. You may appeal this determination. You may ask for an appeal regarding both the coverage determination and the issue of whether you exercised due care. The appeal request must be filed within 120 days of the date you receive this notice. You must make the request through this office.<br />Start: 01/01/1997 | Last Modified: 08/01/2007<br />Notes: (Modified 10/1/02, 8/1/05, 4/1/07, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M28</td><td class="description">This does not qualify for payment under Part B when Part A coverage is exhausted or not otherwise available.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M29</td><td class="description">Missing operative note/report.<br />Start: 01/01/1997 | Last Modified: 07/01/2008<br />Notes: (Modified 2/28/03, 7/1/2008) Related to N233</td></tr>

<tr class="prod_set current"><td class="code">M30</td><td class="description">Missing pathology report.<br />Start: 01/01/1997 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04, 2/28/03) Related to N236</td></tr>

<tr class="prod_set current"><td class="code">M31</td><td class="description">Missing radiology report.<br />Start: 01/01/1997 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04, 2/28/03) Related to N240</td></tr>

<tr class="prod_set current"><td class="code">M32</td><td class="description">Alert: This is a conditional payment made pending a decision on this service by the patient's primary payer. This payment may be subject to refund upon your receipt of any additional payment for this service from another payer. You must contact this office immediately upon receipt of an additional payment for this service.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">M33</td><td class="description">Missing/incomplete/invalid UPIN for the ordering/referring/performing provider.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using M68</td></tr>

<tr class="prod_set deactivated"><td class="code">M34</td><td class="description">Claim lacks the CLIA certification number.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA120</td></tr>

<tr class="prod_set deactivated"><td class="code">M35</td><td class="description">Missing/incomplete/invalid pre-operative photos or visual field results.<br />Start: 01/01/1997 | Stop: 02/05/2005<br />Notes: Consider using N178</td></tr>

<tr class="prod_set current"><td class="code">M36</td><td class="description">This is the 11th rental month.  We cannot pay for this until you indicate that the patient has been given the option of changing the rental to a purchase.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M37</td><td class="description">Not covered when the patient is under age 35.<br />Start: 01/01/1997 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">M38</td><td class="description">Alert: The patient is liable for the charges for this service as they were informed in writing before the service was furnished that we would not pay for it and the patient agreed to be responsible for the charges.<br />Start: 01/01/1997 | Last Modified: 07/01/2015<br />Notes: (Modified 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">M39</td><td class="description">Alert: The patient is not liable for payment of this service as the advance notice of non-coverage you provided the patient did not comply with program requirements.<br />Start: 01/01/1997 | Last Modified: 07/01/2015<br />Notes: (Modified 2/1/04, 4/1/07, 11/1/09, 11/1/12, 7/1/15) Related to N563</td></tr>

<tr class="prod_set current"><td class="code">M40</td><td class="description">Claim must be assigned and must be filed by the practitioner's employer.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M41</td><td class="description">We do not pay for this as the patient has no legal obligation to pay for this.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M42</td><td class="description">The medical necessity form must be personally signed by the attending physician.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M43</td><td class="description">Payment for this service previously issued to you or another provider by another carrier/intermediary.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using Reason Code 23</td></tr>

<tr class="prod_set current"><td class="code">M44</td><td class="description">Missing/incomplete/invalid condition code.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M45</td><td class="description">Missing/incomplete/invalid occurrence code(s).<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N299</td></tr>

<tr class="prod_set current"><td class="code">M46</td><td class="description">Missing/incomplete/invalid occurrence span code(s).<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N300</td></tr>

<tr class="prod_set current"><td class="code">M47</td><td class="description">Missing/incomplete/invalid Payer Claim Control Number. Other terms exist for this element including, but not limited to, Internal Control Number (ICN), Claim Control Number (CCN), Document Control Number (DCN).<br />Start: 01/01/1997 | Last Modified: 07/01/2015<br />Notes: (Modified 2/28/03, 7/1/15)</td></tr>

<tr class="prod_set deactivated"><td class="code">M48</td><td class="description">Payment for services furnished to hospital inpatients (other than professional services of physicians) can only be made to the hospital.  You must request payment from the hospital rather than the patient for this service.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M97</td></tr>

<tr class="prod_set current"><td class="code">M49</td><td class="description">Missing/incomplete/invalid value code(s) or amount(s).<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M50</td><td class="description">Missing/incomplete/invalid revenue code(s).<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M51</td><td class="description">Missing/incomplete/invalid procedure code(s).<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N301</td></tr>

<tr class="prod_set current"><td class="code">M52</td><td class="description">Missing/incomplete/invalid "from" date(s) of service.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M53</td><td class="description">Missing/incomplete/invalid days or units of service.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M54</td><td class="description">Missing/incomplete/invalid total charges.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M55</td><td class="description">We do not pay for self-administered anti-emetic drugs that are not administered with a covered oral anti-cancer drug.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M56</td><td class="description">Missing/incomplete/invalid payer identifier.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">M57</td><td class="description">Missing/incomplete/invalid provider identifier.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set deactivated"><td class="code">M58</td><td class="description">Missing/incomplete/invalid claim information.  Resubmit claim after corrections.<br />Start: 01/01/1997 | Stop: 02/05/2005</td></tr>

<tr class="prod_set current"><td class="code">M59</td><td class="description">Missing/incomplete/invalid "to" date(s) of service.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M60</td><td class="description">Missing Certificate of Medical Necessity.<br />Start: 01/01/1997 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04, 6/30/03) Related to N227</td></tr>

<tr class="prod_set current"><td class="code">M61</td><td class="description">We cannot pay for this as the approval period for the FDA clinical trial has expired.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M62</td><td class="description">Missing/incomplete/invalid treatment authorization code.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">M63</td><td class="description">We do not pay for more than one of these on the same day.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M86</td></tr>

<tr class="prod_set current"><td class="code">M64</td><td class="description">Missing/incomplete/invalid other diagnosis.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M65</td><td class="description">One interpreting physician charge can be submitted per claim when a purchased diagnostic test is indicated. Please submit a separate claim for each interpreting physician.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M66</td><td class="description">Our records indicate that you billed diagnostic tests subject to price limitations and the procedure code submitted includes a professional component. Only the technical component is subject to price limitations.  Please submit the technical and professional components of this service as separate line items.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M67</td><td class="description">Missing/incomplete/invalid other procedure code(s).<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N302</td></tr>

<tr class="prod_set deactivated"><td class="code">M68</td><td class="description">Missing/incomplete/invalid attending, ordering, rendering, supervising or referring physician identification.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">M69</td><td class="description">Paid at the regular rate as you did not submit documentation to justify the modified procedure code.<br />Start: 01/01/1997 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">M70</td><td class="description">Alert: The NDC code submitted for this service was translated to a HCPCS code for processing, but please continue to submit the NDC on future claims for this item.<br />Start: 01/01/1997 | Last Modified: 08/01/2007<br />Notes: (Modified 4/1/2007, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">M71</td><td class="description">Total payment reduced due to overlap of tests billed.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M72</td><td class="description">Did not enter full 8-digit date (MM/DD/CCYY).<br />Start: 01/01/1997 | Stop: 10/16/2003<br />Notes: Consider using MA52</td></tr>

<tr class="prod_set current"><td class="code">M73</td><td class="description">The HPSA/Physician Scarcity bonus can only be paid on the professional component of this service. Rebill as separate professional and technical components.<br />Start: 01/01/1997 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04)</td></tr>

<tr class="prod_set current"><td class="code">M74</td><td class="description">This service does not qualify for a HPSA/Physician Scarcity bonus payment.<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04)</td></tr>

<tr class="prod_set current"><td class="code">M75</td><td class="description">Multiple automated multichannel tests performed on the same day combined for payment.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">M76</td><td class="description">Missing/incomplete/invalid diagnosis or condition.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M77</td><td class="description">Missing/incomplete/invalid/inappropriate place of service.<br />Start: 01/01/1997 | Last Modified: 03/14/2014<br />Notes: (Modified 2/28/03, 3/1/2014, 3/14/2014)</td></tr>

<tr class="prod_set deactivated"><td class="code">M78</td><td class="description">Missing/incomplete/invalid HCPCS modifier.<br />Start: 01/01/1997 | Stop: 05/18/2006 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03,) Consider using Reason Code 4</td></tr>

<tr class="prod_set current"><td class="code">M79</td><td class="description">Missing/incomplete/invalid charge.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M80</td><td class="description">Not covered when performed during the same session/date as a previously processed service for the patient.<br />Start: 01/01/1997 | Last Modified: 10/31/2002<br />Notes: (Modified 10/31/02)</td></tr>

<tr class="prod_set current"><td class="code">M81</td><td class="description">You are required to code to the highest level of specificity.<br />Start: 01/01/1997 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">M82</td><td class="description">Service is not covered when patient is under age 50.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M83</td><td class="description">Service is not covered unless the patient is classified as at high risk.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M84</td><td class="description">Medical code sets used must be the codes in effect at the time of service.<br />Start: 01/01/1997 | Last Modified: 03/14/2014<br />Notes: (Modified 2/1/04, 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">M85</td><td class="description">Subjected to review of physician evaluation and management services.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M86</td><td class="description">Service denied because payment already made for same/similar procedure within set time frame.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">M87</td><td class="description">Claim/service(s) subjected to CFO-CAP prepayment review.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M88</td><td class="description">We cannot pay for laboratory tests unless billed by the laboratory that did the work.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using Reason Code B20</td></tr>

<tr class="prod_set current"><td class="code">M89</td><td class="description">Not covered more than once under age 40.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M90</td><td class="description">Not covered more than once in a 12 month period.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M91</td><td class="description">Lab procedures with different CLIA certification numbers must be billed on separate claims.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M92</td><td class="description">Services subjected to review under the Home Health Medical Review Initiative.<br />Start: 01/01/1997 | Stop: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">M93</td><td class="description">Information supplied supports a break in therapy.  A new capped rental period began with delivery of this equipment.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M94</td><td class="description">Information supplied does not support a break in therapy.  A new capped rental period will not begin.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M95</td><td class="description">Services subjected to Home Health Initiative medical review/cost report audit.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M96</td><td class="description">The technical component of a service furnished to an inpatient may only be billed by that inpatient facility. You must contact the inpatient facility for technical component reimbursement.  If not already billed, you should bill us for the professional component only.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M97</td><td class="description">Not paid to practitioner when provided to patient in this place of service.  Payment included in the reimbursement issued the facility.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M98</td><td class="description">Begin to report the Universal Product Number on claims for items of this type. We will soon begin to deny payment for items of this type if billed without the correct UPN.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M99</td></tr>

<tr class="prod_set current"><td class="code">M99</td><td class="description">Missing/incomplete/invalid Universal Product Number/Serial Number.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M100</td><td class="description">We do not pay for an oral anti-emetic drug that is not administered for use immediately before, at, or within 48 hours of administration of a covered chemotherapy drug.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M101</td><td class="description">Begin to report a G1-G5 modifier with this HCPCS.  We will soon begin to deny payment for this service if billed without a G1-G5 modifier.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M78</td></tr>

<tr class="prod_set current"><td class="code">M102</td><td class="description">Service not performed on equipment approved by the FDA for this purpose.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M103</td><td class="description">Information supplied supports a break in therapy.  However, the medical information we have for this patient does not support the need for this item as billed.  We have approved payment for this item at a reduced level, and a new capped rental period will begin with the delivery of this equipment.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M104</td><td class="description">Information supplied supports a break in therapy.  A new capped rental period will begin with delivery of the equipment.  This is the maximum approved under the fee schedule for this item or service.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M105</td><td class="description">Information supplied does not support a break in therapy.  The medical information we have for this patient does not support the need for this item as billed. We have approved payment for this item at a reduced level, and a new capped rental period will not begin.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M106</td><td class="description">Information supplied does not support a break in therapy.  A new capped rental period will not begin. This is the maximum approved under the fee schedule for this item or service.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using MA 31</td></tr>

<tr class="prod_set current"><td class="code">M107</td><td class="description">Payment reduced as 90-day rolling average hematocrit for ESRD patient exceeded 36.5%.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M108</td><td class="description">Missing/incomplete/invalid provider identifier for the provider who interpreted the diagnostic test.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">M109</td><td class="description">We have provided you with a bundled payment for a teleconsultation. You must send 25 percent of the teleconsultation payment to the referring practitioner.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M110</td><td class="description">Missing/incomplete/invalid provider identifier for the provider from whom you purchased interpretation services.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">M111</td><td class="description">We do not pay for chiropractic manipulative treatment when the patient refuses to have an x-ray taken.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M112</td><td class="description">Reimbursement for this item is based on the single payment amount required under the DMEPOS Competitive Bidding Program for the area where the patient resides.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">M113</td><td class="description">Our records indicate that this patient began using this item/service prior to the current contract period for the DMEPOS Competitive Bidding Program.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">M114</td><td class="description">This service was processed in accordance with rules and guidelines under the DMEPOS Competitive Bidding Program or a Demonstration Project.  For more information regarding these projects, contact your local contractor.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 8/1/06, 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">M115</td><td class="description">This item is denied when provided to this patient by a non-contract or non-demonstration supplier.<br />Start: 01/01/1997 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/2007)</td></tr>

<tr class="prod_set current"><td class="code">M116</td><td class="description">Processed under a demonstration project or program. Project or program is ending and additional services may not be paid under this project or program.<br />Start: 01/01/1997 | Last Modified: 03/08/2011<br />Notes: (Modified 2/1/04, 3/15/11)</td></tr>

<tr class="prod_set current"><td class="code">M117</td><td class="description">Not covered unless submitted via electronic claim.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">M118</td><td class="description">Letter to follow containing further information.<br />Start: 01/01/1997 | Stop: 01/01/2011 | Last Modified: 11/01/2009<br />Notes: Consider using N202</td></tr>

<tr class="prod_set current"><td class="code">M119</td><td class="description">Missing/incomplete/invalid/ deactivated/withdrawn National Drug Code (NDC).<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 2/28/03, 4/1/04)</td></tr>

<tr class="prod_set deactivated"><td class="code">M120</td><td class="description">Missing/incomplete/invalid provider identifier for the substituting physician who furnished the service(s) under a reciprocal billing or locum tenens arrangement.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">M121</td><td class="description">We pay for this service only when performed with a covered cryosurgical ablation.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M122</td><td class="description">Missing/incomplete/invalid level of subluxation.<br />Start: 01/01/1997 | Last Modified: 02/28/2006<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M123</td><td class="description">Missing/incomplete/invalid name, strength, or dosage of the drug furnished.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M124</td><td class="description">Missing indication of whether the patient owns the equipment that requires the part or supply.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N230</td></tr>

<tr class="prod_set current"><td class="code">M125</td><td class="description">Missing/incomplete/invalid information on the period of time for which the service/supply/equipment will be needed.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M126</td><td class="description">Missing/incomplete/invalid individual lab codes included in the test.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M127</td><td class="description">Missing patient medical record for this service.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N237</td></tr>

<tr class="prod_set deactivated"><td class="code">M128</td><td class="description">Missing/incomplete/invalid date of the patient's last physician visit.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">M129</td><td class="description">Missing/incomplete/invalid indicator of x-ray availability for review.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 2/28/03, 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">M130</td><td class="description">Missing invoice or statement certifying the actual cost of the lens, less discounts, and/or the type of intraocular lens used.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N231</td></tr>

<tr class="prod_set current"><td class="code">M131</td><td class="description">Missing physician financial relationship form.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N239</td></tr>

<tr class="prod_set current"><td class="code">M132</td><td class="description">Missing pacemaker registration form.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N235</td></tr>

<tr class="prod_set current"><td class="code">M133</td><td class="description">Claim did not identify who performed the purchased diagnostic test or the amount you were charged for the test.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M134</td><td class="description">Performed by a facility/supplier in which the provider has a financial interest.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">M135</td><td class="description">Missing/incomplete/invalid plan of treatment.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M136</td><td class="description">Missing/incomplete/invalid indication that the service was supervised or evaluated by a physician.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">M137</td><td class="description">Part B coinsurance under a demonstration project or pilot program.<br />Start: 01/01/1997 | Last Modified: 11/01/2012<br />Notes: (Modified 11/1/12)</td></tr>

<tr class="prod_set current"><td class="code">M138</td><td class="description">Patient identified as a demonstration participant but the patient was not enrolled in the demonstration at the time services were rendered.  Coverage is limited to demonstration participants.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">M139</td><td class="description">Denied services exceed the coverage limit for the demonstration.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">M140</td><td class="description">Service not covered until after the patient's 50th birthday, i.e., no coverage prior to the day after the 50th birthday<br />Start: 01/01/1997 | Stop: 01/30/2004<br />Notes: Consider using M82</td></tr>

<tr class="prod_set current"><td class="code">M141</td><td class="description">Missing physician certified plan of care.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N238</td></tr>

<tr class="prod_set current"><td class="code">M142</td><td class="description">Missing American Diabetes Association Certificate of Recognition.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N226</td></tr>

<tr class="prod_set current"><td class="code">M143</td><td class="description">The provider must update license information with the payer.<br />Start: 01/01/1997 | Last Modified: 12/01/2006<br />Notes: (Modified 12/1/06)</td></tr>

<tr class="prod_set current"><td class="code">M144</td><td class="description">Pre-/post-operative care payment is included in the allowance for the surgery/procedure.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA01</td><td class="description">Alert: If you do not agree with what we approved for these services, you may appeal our decision.  To make sure that we are fair to you, we require another individual that did not process your initial claim to conduct the appeal.  However, in order to be eligible for an appeal, you must write to us within 120 days of the date you received this notice, unless you have a good reason for being late.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 10/31/02, 6/30/03, 8/1/05, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA02</td><td class="description">Alert: If you do not agree with this determination, you have the right to appeal. You must file a written request for an appeal within 180 days of the date you receive this notice.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 10/31/02, 6/30/03, 8/1/05, 12/29/05, 8/1/06, 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA03</td><td class="description">If you do not agree with the approved amounts and $100 or more is in dispute (less deductible and coinsurance), you may ask for a hearing within six months of the date of this notice. To meet the $100, you may combine amounts on other claims that have been denied, including reopened appeals if you received a revised decision. You must appeal each claim on time.<br />Start: 01/01/1997 | Stop: 10/01/2006 | Last Modified: 11/18/2005<br />Notes: Consider using MA02 (Modified 10/31/02, 6/30/03, 8/1/05, 11/18/05)</td></tr>

<tr class="prod_set current"><td class="code">MA04</td><td class="description">Secondary payment cannot be considered without the identity of or payment information from the primary payer.  The information was either not reported or was illegible.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">MA05</td><td class="description">Incorrect admission date patient status or type of bill entry on claim.<br />Start: 01/01/1997 | Stop: 10/16/2003<br />Notes: Consider using MA30, MA40 or MA43</td></tr>

<tr class="prod_set deactivated"><td class="code">MA06</td><td class="description">Missing/incomplete/invalid beginning and/or ending date(s).<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA31</td></tr>

<tr class="prod_set current"><td class="code">MA07</td><td class="description">Alert: The claim information has also been forwarded to Medicaid for review.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA08</td><td class="description">Alert: Claim information was not forwarded because the supplemental coverage is not with a Medigap plan, or you do not participate in Medicare.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA09</td><td class="description">Alert: Claim submitted as unassigned but processed as assigned in accordance with our current assignment/participation agreement.<br />Start: 01/01/1997 | Last Modified: 11/01/2015<br />Notes: (Modified 11/1/2014, 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">MA10</td><td class="description">Alert: The patient's payment was in excess of the amount owed.  You must refund the overpayment to the patient.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA11</td><td class="description">Payment is being issued on a conditional basis.  If no-fault insurance, liability insurance, Workers' Compensation, Department of Veterans Affairs, or a group health plan for employees and dependents also covers this claim, a refund may be due us.  Please contact us if the patient is covered by any of these sources.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M32</td></tr>

<tr class="prod_set current"><td class="code">MA12</td><td class="description">You have not established that you have the right under the law to bill for services furnished by the person(s) that furnished this (these) service(s).<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA13</td><td class="description">Alert: You may be subject to penalties if you bill the patient for amounts not reported with the PR (patient responsibility) group code.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA14</td><td class="description">Alert: The patient is a member of an employer-sponsored prepaid health plan. Services from outside that health plan are not covered.  However, as you were not previously notified of this, we are paying this time.  In the future, we will not pay you for non-plan services.<br />Start: 01/01/1997 | Last Modified: 08/01/2007<br />Notes: (Modified 4/1/07, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA15</td><td class="description">Alert: Your claim has been separated to expedite handling. You will receive a separate notice for the other services reported.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA16</td><td class="description">The patient is covered by the Black Lung Program.  Send this claim to the Department of Labor, Federal Black Lung Program, P.O. Box 828, Lanham-Seabrook MD 20703.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA17</td><td class="description">We are the primary payer and have paid at the primary rate.  You must contact the patient's other insurer to refund any excess it may have paid due to its erroneous primary payment.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA18</td><td class="description">Alert: The claim information is also being forwarded to the patient's supplemental insurer. Send any questions regarding supplemental benefits to them.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA19</td><td class="description">Alert:  Information was not sent to the Medigap insurer due to incorrect/invalid information you submitted concerning that insurer. Please verify your information and submit your secondary claim directly to that insurer.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA20</td><td class="description">Skilled Nursing Facility (SNF) stay not covered when care is primarily related to the use of an urethral catheter for convenience or the control of incontinence.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">MA21</td><td class="description">SSA records indicate mismatch with name and sex.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA22</td><td class="description">Payment of less than $1.00 suppressed.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA23</td><td class="description">Demand bill approved as result of medical review.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA24</td><td class="description">Christian Science Sanitarium/ Skilled Nursing Facility (SNF) bill in the same benefit period.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">MA25</td><td class="description">A patient may not elect to change a hospice provider more than once in a benefit period.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA26</td><td class="description">Alert: Our records indicate that you were previously informed of this rule.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA27</td><td class="description">Missing/incomplete/invalid entitlement number or name shown on the claim.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA28</td><td class="description">Alert: Receipt of this notice by a physician or supplier who did not accept assignment is for information only and does not make the physician or supplier a party to the determination.  No additional rights to appeal this decision, above those rights already provided for by regulation/instruction, are conferred by receipt of this notice.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA29</td><td class="description">Missing/incomplete/invalid provider name, city, state, or zip code.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA30</td><td class="description">Missing/incomplete/invalid type of bill.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA31</td><td class="description">Missing/incomplete/invalid beginning and ending dates of the period billed.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA32</td><td class="description">Missing/incomplete/invalid number of covered days during the billing period.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA33</td><td class="description">Missing/incomplete/invalid noncovered days during the billing period.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA34</td><td class="description">Missing/incomplete/invalid number of coinsurance days during the billing period.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA35</td><td class="description">Missing/incomplete/invalid number of lifetime reserve days.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA36</td><td class="description">Missing/incomplete/invalid patient name.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA37</td><td class="description">Missing/incomplete/invalid patient's address.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA38</td><td class="description">Missing/incomplete/invalid birth date.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA39</td><td class="description">Missing/incomplete/invalid gender.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA40</td><td class="description">Missing/incomplete/invalid admission date.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA41</td><td class="description">Missing/incomplete/invalid admission type.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA42</td><td class="description">Missing/incomplete/invalid admission source.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA43</td><td class="description">Missing/incomplete/invalid patient status.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA44</td><td class="description">Alert: No appeal rights. Adjudicative decision based on law.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA45</td><td class="description">Alert: As previously advised, a portion or all of your payment is being held in a special account.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA46</td><td class="description">Alert: The new information was considered but additional payment will not be issued.<br />Start: 01/01/1997 | Last Modified: 11/01/2015<br />Notes: (Modified 3/1/2009, 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">MA47</td><td class="description">Our records show you have opted out of Medicare, agreeing with the patient not to bill Medicare for services/tests/supplies furnished.  As result, we cannot pay this claim. The patient is responsible for payment.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA48</td><td class="description">Missing/incomplete/invalid name or address of responsible party or primary payer.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA49</td><td class="description">Missing/incomplete/invalid six-digit provider identifier for home health agency or hospice for physician(s) performing care plan oversight services.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA76</td></tr>

<tr class="prod_set current"><td class="code">MA50</td><td class="description">Missing/incomplete/invalid Investigational Device Exemption number or Clinical Trial number.<br />Start: 01/01/1997 | Last Modified: 03/01/2014<br />Notes: (Modified  2/28/03, 3/1/2014)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA51</td><td class="description">Missing/incomplete/invalid CLIA certification number for laboratory services billed by physician office laboratory.<br />Start: 01/01/1997 | Stop: 02/05/2005<br />Notes: Consider using MA120</td></tr>

<tr class="prod_set deactivated"><td class="code">MA52</td><td class="description">Missing/incomplete/invalid date.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA53</td><td class="description">Missing/incomplete/invalid Competitive Bidding Demonstration Project identification.<br />Start: 01/01/1997 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">MA54</td><td class="description">Physician certification or election consent for hospice care not received timely.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA55</td><td class="description">Not covered as patient received medical health care services, automatically revoking his/her election to receive religious non-medical health care services.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA56</td><td class="description">Our records show you have opted out of Medicare, agreeing with the patient not to bill Medicare for services/tests/supplies furnished.  As result, we cannot pay this claim. The patient is responsible for payment, but under Federal law, you cannot charge the patient more than the limiting charge amount.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA57</td><td class="description">Patient submitted written request to revoke his/her election for religious non-medical health care services.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA58</td><td class="description">Missing/incomplete/invalid release of information indicator.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA59</td><td class="description">Alert: The patient overpaid you for these services. You must issue the patient a refund within 30 days for the difference between his/her payment and the total amount shown as patient responsibility on this notice.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA60</td><td class="description">Missing/incomplete/invalid patient relationship to insured.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA61</td><td class="description">Missing/incomplete/invalid social security number or health insurance claim number.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA62</td><td class="description">Alert: This is a telephone review decision.<br />Start: 01/01/1997 | Last Modified: 08/01/2007<br />Notes: (Modified 4/1/07, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA63</td><td class="description">Missing/incomplete/invalid principal diagnosis.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA64</td><td class="description">Our records indicate that we should be the third payer for this claim.  We cannot process this claim until we have received payment information from the primary and secondary payers.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA65</td><td class="description">Missing/incomplete/invalid admitting diagnosis.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA66</td><td class="description">Missing/incomplete/invalid principal procedure code.<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N303</td></tr>

<tr class="prod_set current"><td class="code">MA67</td><td class="description">Alert: Correction to a prior claim.<br />Start: 01/01/1997 | Last Modified: 11/01/2015<br />Notes: (Modified 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">MA68</td><td class="description">Alert: We did not crossover this claim because the secondary insurance information on the claim was incomplete. Please supply complete information or use the PLANID of the insurer to assure correct and timely routing of the claim.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA69</td><td class="description">Missing/incomplete/invalid remarks.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA70</td><td class="description">Missing/incomplete/invalid provider representative signature.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA71</td><td class="description">Missing/incomplete/invalid provider representative signature date.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA72</td><td class="description">Alert: The patient overpaid you for these assigned services.  You must issue the patient a refund within 30 days for the difference between his/her payment to you and the total of the amount shown as patient responsibility and as paid to the patient on this notice.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">MA73</td><td class="description">Informational remittance associated with a Medicare demonstration.  No payment issued under fee-for-service Medicare as patient has elected managed care.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA74</td><td class="description">Alert: This payment replaces an earlier payment for this claim that was either lost, damaged or returned.<br />Start: 01/01/1997 | Last Modified: 07/01/2015<br />Notes: (Modified 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">MA75</td><td class="description">Missing/incomplete/invalid patient or authorized representative signature.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA76</td><td class="description">Missing/incomplete/invalid provider identifier for home health agency or hospice when physician is performing care plan oversight services.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03, 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">MA77</td><td class="description">Alert: The patient overpaid you. You must issue the patient a refund within 30 days for the difference between the patient's payment less the total of our and other payer payments and the amount shown as patient responsibility on this notice.<br />Start: 01/01/1997 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA78</td><td class="description">The patient overpaid you.  You must issue the patient a refund within 30 days for the difference between our allowed amount total and the amount paid by the patient.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using MA59</td></tr>

<tr class="prod_set current"><td class="code">MA79</td><td class="description">Billed in excess of interim rate.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA80</td><td class="description">Informational notice. No payment issued for this claim with this notice. Payment issued to the hospital by its intermediary for all services for this encounter under a demonstration project.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA81</td><td class="description">Missing/incomplete/invalid provider/supplier signature.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA82</td><td class="description">Missing/incomplete/invalid provider/supplier billing number/identifier or billing name, address, city, state, zip code, or phone number.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA83</td><td class="description">Did not indicate whether we are the primary or secondary payer.<br />Start: 01/01/1997 | Last Modified: 08/01/2005<br />Notes: (Modified 8/1/05)</td></tr>

<tr class="prod_set current"><td class="code">MA84</td><td class="description">Patient identified as participating in the National Emphysema Treatment Trial but our records indicate that this patient is either not a participant, or has not yet been approved for this phase of the study.  Contact Johns Hopkins University, the study coordinator, to resolve if there was a discrepancy.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">MA85</td><td class="description">Our records indicate that a primary payer exists (other than ourselves); however, you did not complete or enter accurately the insurance plan/group/program name or identification number.  Enter the PlanID when effective.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA92</td></tr>

<tr class="prod_set deactivated"><td class="code">MA86</td><td class="description">Missing/incomplete/invalid group or policy number of the insured for the primary coverage.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA92</td></tr>

<tr class="prod_set deactivated"><td class="code">MA87</td><td class="description">Missing/incomplete/invalid insured's name for the primary payer.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using MA92</td></tr>

<tr class="prod_set current"><td class="code">MA88</td><td class="description">Missing/incomplete/invalid insured's address and/or telephone number for the primary payer.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA89</td><td class="description">Missing/incomplete/invalid patient's relationship to the insured for the primary payer.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA90</td><td class="description">Missing/incomplete/invalid employment status code for the primary insured.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03).</td></tr>

<tr class="prod_set current"><td class="code">MA91</td><td class="description">Alert: This determination is the result of the appeal you filed.<br />Start: 01/01/1997 | Last Modified: 07/01/2015<br />Notes: (Modified 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">MA92</td><td class="description">Missing plan information for other insurance.<br />Start: 01/01/1997 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04) Related to N245</td></tr>

<tr class="prod_set current"><td class="code">MA93</td><td class="description">Non-PIP (Periodic Interim Payment) claim.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">MA94</td><td class="description">Did not enter the statement "Attending physician not hospice employee" on the claim form to certify that the rendering physician is not an employee of the hospice.<br />Start: 01/01/1997 | Last Modified: 08/01/2005<br />Notes: (Reactivated 4/1/04, Modified 8/1/05)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA95</td><td class="description">A not otherwise classified or unlisted procedure code(s) was billed but a narrative description of the procedure was not entered on the claim.  Refer to item 19 on the HCFA-1500.<br />Start: 01/01/1997 | Stop: 01/01/2004 | Last Modified: 02/28/2003<br />Notes: (Deactivated 2/28/2003) (Erroneous description corrected 9/2/2008) Consider using M51</td></tr>

<tr class="prod_set current"><td class="code">MA96</td><td class="description">Claim rejected. Coded as a Medicare Managed Care Demonstration but patient is not enrolled in a Medicare managed care plan.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA97</td><td class="description">Missing/incomplete/invalid Medicare Managed Care Demonstration contract number or clinical trial registry number.<br />Start: 01/01/1997 | Last Modified: 02/29/2008<br />Notes: (Modified 2/29/08)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA98</td><td class="description">Claim Rejected. Does not contain the correct Medicare Managed Care Demonstration contract number for this beneficiary.<br />Start: 01/01/1997 | Stop: 10/16/2003<br />Notes: Consider using MA97</td></tr>

<tr class="prod_set current"><td class="code">MA99</td><td class="description">Missing/incomplete/invalid Medigap information.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA100</td><td class="description">Missing/incomplete/invalid date of current illness or symptoms.<br />Start: 01/01/1997 | Last Modified: 03/14/2014<br />Notes: (Modified 2/28/03, 3/30/05, 3/14/2014)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA101</td><td class="description">A Skilled Nursing Facility (SNF) is responsible for payment of outside providers who furnish these services/supplies to residents.<br />Start: 01/01/1997 | Stop: 01/01/2011 | Last Modified: 06/30/2003<br />Notes: Consider using N538</td></tr>

<tr class="prod_set deactivated"><td class="code">MA102</td><td class="description">Missing/incomplete/invalid name or provider identifier for the rendering/referring/ ordering/ supervising provider.<br />Start: 01/01/1997 | Stop: 08/01/2004<br />Notes: Consider using M68</td></tr>

<tr class="prod_set current"><td class="code">MA103</td><td class="description">Hemophilia Add On.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">MA104</td><td class="description">Missing/incomplete/invalid date the patient was last seen or the provider identifier of the attending physician.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using M128 or M57</td></tr>

<tr class="prod_set deactivated"><td class="code">MA105</td><td class="description">Missing/incomplete/invalid provider number for this place of service.<br />Start: 01/01/1997 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA106</td><td class="description">PIP (Periodic Interim Payment) claim.<br />Start: 01/01/1997 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">MA107</td><td class="description">Paper claim contains more than three separate data items in field 19.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA108</td><td class="description">Paper claim contains more than one data item in field 23.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA109</td><td class="description">Claim processed in accordance with ambulatory surgical guidelines.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA110</td><td class="description">Missing/incomplete/invalid information on whether the diagnostic test(s) were performed by an outside entity or if no purchased tests are included on the claim.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA111</td><td class="description">Missing/incomplete/invalid purchase price of the test(s) and/or the performing laboratory's name and address.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA112</td><td class="description">Missing/incomplete/invalid group practice information.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA113</td><td class="description">Incomplete/invalid taxpayer identification number (TIN) submitted by you per the Internal Revenue Service. Your claims cannot be processed without your correct TIN, and you may not bill the patient pending correction of your TIN.  There are no appeal rights for unprocessable claims, but you may resubmit this claim after you have notified this office of your correct TIN.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA114</td><td class="description">Missing/incomplete/invalid information on where the services were furnished.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA115</td><td class="description">Missing/incomplete/invalid physical location (name and address, or PIN) where the service(s) were rendered in a Health Professional Shortage Area (HPSA).<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA116</td><td class="description">Did not complete the statement 'Homebound' on the claim to validate whether laboratory services were performed at home or in an institution.<br />Start: 01/01/1997<br />Notes: (Reactivated 4/1/04)</td></tr>

<tr class="prod_set current"><td class="code">MA117</td><td class="description">This claim has been assessed a $1.00 user fee.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA118</td><td class="description">Alert: No Medicare payment issued for this claim for services or supplies furnished to a Medicare-eligible veteran through a facility of the Department of Veterans Affairs. Coinsurance and/or deductible are applicable.<br />Start: 01/01/1997 | Last Modified: 11/01/2014</td></tr>

<tr class="prod_set deactivated"><td class="code">MA119</td><td class="description">Provider level adjustment for late claim filing applies to this claim.<br />Start: 01/01/1997 | Stop: 05/01/2008 | Last Modified: 11/05/2007<br />Notes: Consider using Reason Code B4</td></tr>

<tr class="prod_set current"><td class="code">MA120</td><td class="description">Missing/incomplete/invalid CLIA certification number.<br />Start: 01/01/1997 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">MA121</td><td class="description">Missing/incomplete/invalid x-ray date.<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04)</td></tr>

<tr class="prod_set current"><td class="code">MA122</td><td class="description">Missing/incomplete/invalid initial treatment date.<br />Start: 01/01/1997 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04)</td></tr>

<tr class="prod_set current"><td class="code">MA123</td><td class="description">Your center was not selected to participate in this study, therefore, we cannot pay for these services.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set deactivated"><td class="code">MA124</td><td class="description">Processed for IME only.<br />Start: 01/01/1997 | Stop: 01/31/2004<br />Notes: Consider using Reason Code 74</td></tr>

<tr class="prod_set current"><td class="code">MA125</td><td class="description">Per legislation governing this program, payment constitutes payment in full.<br />Start: 01/01/1997</td></tr>

<tr class="prod_set current"><td class="code">MA126</td><td class="description">Pancreas transplant not covered unless kidney transplant performed.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set deactivated"><td class="code">MA127</td><td class="description">Reserved for future use.<br />Start: 10/12/2001 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">MA128</td><td class="description">Missing/incomplete/invalid FDA approval number.<br />Start: 10/12/2001 | Last Modified: 03/30/2005<br />Notes: (Modified 2/28/03, 3/30/05)</td></tr>

<tr class="prod_set deactivated"><td class="code">MA129</td><td class="description">This provider was not certified for this procedure on this date of service.<br />Start: 10/12/2001 | Stop: 01/31/2004 | Last Modified: 01/31/2004<br />Notes: Consider using MA120 and Reason Code B7</td></tr>

<tr class="prod_set current"><td class="code">MA130</td><td class="description">Your claim contains incomplete and/or invalid information, and no appeal rights are afforded because the claim is unprocessable.  Please submit a new claim with the complete/correct information.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set current"><td class="code">MA131</td><td class="description">Physician already paid for services in conjunction with this demonstration claim.  You must have the physician withdraw that claim and refund the payment before we can process your claim.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set current"><td class="code">MA132</td><td class="description">Adjustment to the pre-demonstration rate.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set current"><td class="code">MA133</td><td class="description">Claim overlaps inpatient stay. Rebill only those services rendered outside the inpatient stay.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set current"><td class="code">MA134</td><td class="description">Missing/incomplete/invalid provider number of the facility where the patient resides.<br />Start: 10/12/2001</td></tr>

<tr class="prod_set current"><td class="code">N1</td><td class="description">Alert: You may appeal this decision in writing within the required time limits following receipt of this notice by following the instructions included in your contract, plan benefit documents or jurisdiction statutes.<br />Start: 01/01/2000 | Last Modified: 07/15/2013<br />Notes: (Modified 2/28/03, 4/1/07, 7/15/13)</td></tr>

<tr class="prod_set current"><td class="code">N2</td><td class="description">This allowance has been made in accordance with the most appropriate course of treatment provision of the plan.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N3</td><td class="description">Missing consent form.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03) Related to N228</td></tr>

<tr class="prod_set current"><td class="code">N4</td><td class="description">Missing/Incomplete/Invalid prior Insurance Carrier(s) EOB.<br />Start: 01/01/2000 | Last Modified: 03/06/2012<br />Notes: (Modified 2/28/03, 3/6/2012)</td></tr>

<tr class="prod_set current"><td class="code">N5</td><td class="description">EOB received from previous payer.  Claim not on file.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N6</td><td class="description">Under FEHB law (U.S.C. 8904(b)), we cannot pay more for covered care than the amount Medicare would have allowed if the patient were enrolled in Medicare Part A and/or Medicare Part B.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N7</td><td class="description">Alert: Processing of this claim/service has included consideration under Major Medical provisions.<br />Start: 01/01/2000 | Last Modified: 07/15/2013<br />Notes: (Modified 7/15/13)</td></tr>

<tr class="prod_set current"><td class="code">N8</td><td class="description">Crossover claim denied by previous payer and complete claim data not forwarded. Resubmit this claim to this payer to provide adequate data for adjudication.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N9</td><td class="description">Adjustment represents the estimated amount a previous payer may pay.<br />Start: 01/01/2000 | Last Modified: 11/18/2005<br />Notes: (Modified 11/18/05)</td></tr>

<tr class="prod_set current"><td class="code">N10</td><td class="description">Adjustment based on the findings of a review organization/professional consult/manual adjudication/medical advisor/dental advisor/peer review.<br />Start: 01/01/2000 | Last Modified: 03/01/2015<br />Notes: (Modified 10/31/02, 7/1/08, 7/15/13, 3/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N11</td><td class="description">Denial reversed because of medical review.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N12</td><td class="description">Policy provides coverage supplemental to Medicare. As the member does not appear to be enrolled in the applicable part of Medicare, the member is responsible for payment of the portion of the charge that would have been covered by Medicare.<br />Start: 01/01/2000 | Last Modified: 08/01/2007<br />Notes: (Modified 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N13</td><td class="description">Payment based on professional/technical component modifier(s).<br />Start: 01/01/2000</td></tr>

<tr class="prod_set deactivated"><td class="code">N14</td><td class="description">Payment based on a contractual amount or agreement, fee schedule, or maximum allowable amount.<br />Start: 01/01/2000 | Stop: 10/01/2007<br />Notes: Consider using Reason Code 45</td></tr>

<tr class="prod_set current"><td class="code">N15</td><td class="description">Services for a newborn must be billed separately.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N16</td><td class="description">Family/member Out-of-Pocket maximum has been met. Payment based on a higher percentage.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set deactivated"><td class="code">N17</td><td class="description">Per admission deductible.<br />Start: 01/01/2000 | Stop: 08/01/2004<br />Notes: Consider using Reason Code 1</td></tr>

<tr class="prod_set deactivated"><td class="code">N18</td><td class="description">Payment based on the Medicare allowed amount.<br />Start: 01/01/2000 | Stop: 01/31/2004<br />Notes: Consider using N14</td></tr>

<tr class="prod_set current"><td class="code">N19</td><td class="description">Procedure code incidental to primary procedure.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N20</td><td class="description">Service not payable with other service rendered on the same date.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N21</td><td class="description">Alert: Your line item has been separated into multiple lines to expedite handling.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 8/1/05, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N22</td><td class="description">Alert: This procedure code was added/changed because it more accurately describes the services rendered.<br />Start: 01/01/2000 | Last Modified: 07/01/2015<br />Notes: (Modified 10/31/02, 2/28/03, 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">N23</td><td class="description">Alert: Patient liability may be affected due to coordination of benefits with other carriers and/or maximum benefit provisions.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 8/13/01, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N24</td><td class="description">Missing/incomplete/invalid Electronic Funds Transfer (EFT) banking information.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N25</td><td class="description">This company has been contracted by your benefit plan to provide administrative claims payment services only.  This company does not assume financial risk or obligation with respect to claims processed on behalf of your benefit plan.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N26</td><td class="description">Missing itemized bill/statement.<br />Start: 01/01/2000 | Last Modified: 07/01/2008<br />Notes: (Modified 2/28/03, 7/1/2008) Related to N232</td></tr>

<tr class="prod_set current"><td class="code">N27</td><td class="description">Missing/incomplete/invalid treatment number.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N28</td><td class="description">Consent form requirements not fulfilled.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set deactivated"><td class="code">N29</td><td class="description">Missing documentation/orders/notes/summary/report/chart.<br />Start: 01/01/2000 | Stop: 03/01/2016 | Last Modified: 03/01/2014<br />Notes: (Modified 2/28/03, 8/1/05, 3/1/2014) Related to N225, Explicit RARCs have been approved, this non-specific RARC will be deactivated in March 2016.</td></tr>

<tr class="prod_set current"><td class="code">N30</td><td class="description">Patient ineligible for this service.<br />Start: 01/01/2000 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N31</td><td class="description">Missing/incomplete/invalid prescribing provider identifier.<br />Start: 01/01/2000 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04)</td></tr>

<tr class="prod_set current"><td class="code">N32</td><td class="description">Claim must be submitted by the provider who rendered the service.<br />Start: 01/01/2000 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N33</td><td class="description">No record of health check prior to initiation of treatment.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N34</td><td class="description">Incorrect claim form/format for this service.<br />Start: 01/01/2000 | Last Modified: 11/18/2005<br />Notes: (Modified 11/18/05)</td></tr>

<tr class="prod_set current"><td class="code">N35</td><td class="description">Program integrity/utilization review decision.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N36</td><td class="description">Claim must meet primary payer's processing requirements before we can consider payment.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N37</td><td class="description">Missing/incomplete/invalid tooth number/letter.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">N38</td><td class="description">Missing/incomplete/invalid place of service.<br />Start: 01/01/2000 | Stop: 02/05/2005<br />Notes: Consider using M77</td></tr>

<tr class="prod_set current"><td class="code">N39</td><td class="description">Procedure code is not compatible with tooth number/letter.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N40</td><td class="description">Missing radiology film(s)/image(s).<br />Start: 01/01/2000 | Last Modified: 07/01/2008<br />Notes: (Modified 2/1/04, 7/1/08) Related to N242</td></tr>

<tr class="prod_set deactivated"><td class="code">N41</td><td class="description">Authorization request denied.<br />Start: 01/01/2000 | Stop: 10/16/2003<br />Notes: Consider using Reason Code 39</td></tr>

<tr class="prod_set current"><td class="code">N42</td><td class="description">Missing mental health assessment.<br />Start: 01/01/2000 | Last Modified: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N43</td><td class="description">Bed hold or leave days exceeded.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set deactivated"><td class="code">N44</td><td class="description">Payer's share of regulatory surcharges, assessments, allowances or health care-related taxes paid directly to the regulatory authority.<br />Start: 01/01/2000 | Stop: 10/16/2003<br />Notes: Consider using Reason Code 137</td></tr>

<tr class="prod_set current"><td class="code">N45</td><td class="description">Payment based on authorized amount.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N46</td><td class="description">Missing/incomplete/invalid admission hour.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N47</td><td class="description">Claim conflicts with another inpatient stay.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N48</td><td class="description">Claim information does not agree with information received from other insurance carrier.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N49</td><td class="description">Court ordered coverage information needs validation.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N50</td><td class="description">Missing/incomplete/invalid discharge information.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N51</td><td class="description">Electronic interchange agreement not on file for provider/submitter.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N52</td><td class="description">Patient not enrolled in the billing provider's managed care plan on the date of service.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N53</td><td class="description">Missing/incomplete/invalid point of pick-up address.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N54</td><td class="description">Claim information is inconsistent with pre-certified/authorized services.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N55</td><td class="description">Procedures for billing with group/referring/performing providers were not followed.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N56</td><td class="description">Procedure code billed is not correct/valid for the services billed or the date of service billed.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N57</td><td class="description">Missing/incomplete/invalid prescribing date.<br />Start: 01/01/2000 | Last Modified: 12/02/2004<br />Notes: (Modified 12/2/04) Related to N304</td></tr>

<tr class="prod_set current"><td class="code">N58</td><td class="description">Missing/incomplete/invalid patient liability amount.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N59</td><td class="description">Alert: Please refer to your provider manual for additional program and provider information.<br />Start: 01/01/2000 | Last Modified: 11/01/2015<br />Notes: (Modified 4/1/07, 11/1/09, 11/1/2015)</td></tr>

<tr class="prod_set deactivated"><td class="code">N60</td><td class="description">A valid NDC is required for payment of drug claims effective October 02.<br />Start: 01/01/2000 | Stop: 01/31/2004<br />Notes: Consider using M119</td></tr>

<tr class="prod_set current"><td class="code">N61</td><td class="description">Rebill services on separate claims.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N62</td><td class="description">Dates of service span multiple rate periods. Resubmit separate claims.<br />Start: 01/01/2000 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N63</td><td class="description">Rebill services on separate claim lines.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N64</td><td class="description">The "from" and "to" dates must be different.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N65</td><td class="description">Procedure code or procedure rate count cannot be determined, or was not on file, for the date of service/provider.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">N66</td><td class="description">Missing/incomplete/invalid documentation.<br />Start: 01/01/2000 | Stop: 02/05/2005<br />Notes: Consider using N29 or N225.</td></tr>

<tr class="prod_set current"><td class="code">N67</td><td class="description">Professional provider services not paid separately.  Included in facility payment under a demonstration project.  Apply to that facility for payment, or resubmit your claim if: the facility notifies you the patient was excluded from this demonstration; or if you furnished these services in another location on the date of the patient's admission or discharge from a demonstration hospital. If services were furnished in a facility not involved in the demonstration on the same date the patient was discharged from or admitted to a demonstration facility, you must report the provider ID number for the non-demonstration facility on the new claim.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N68</td><td class="description">Prior payment being cancelled as we were subsequently notified this patient was covered by a demonstration project in this site of service.  Professional services were included in the payment made to the facility. You must contact the facility for your payment.  Prior payment made to you by the patient or another insurer for this claim must be refunded to the payer within 30 days.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N69</td><td class="description">Alert: PPS (Prospective Payment System) code changed by claims processing system.<br />Start: 01/01/2000 | Last Modified: 11/01/2015<br />Notes: (Modified 6/30/03, 7/1/12, 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N70</td><td class="description">Consolidated billing and payment applies.<br />Start: 01/01/2000 | Last Modified: 11/05/2007<br />Notes: (Modified 2/28/02, 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">N71</td><td class="description">Your unassigned claim for a drug or biological, clinical diagnostic laboratory services or ambulance service was processed as an assigned claim. You are required by law to accept assignment for these types of claims.<br />Start: 01/01/2000 | Last Modified: 06/30/2003<br />Notes: (Modified 2/21/02, 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N72</td><td class="description">PPS (Prospective Payment System)  code changed by medical reviewers.  Not supported by clinical records.<br />Start: 01/01/2000 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set deactivated"><td class="code">N73</td><td class="description">A Skilled Nursing Facility is responsible for payment of outside providers who furnish these services/supplies under arrangement to its residents.<br />Start: 01/01/2000 | Stop: 01/31/2004<br />Notes: Consider using MA101 or N200</td></tr>

<tr class="prod_set current"><td class="code">N74</td><td class="description">Resubmit with multiple claims, each claim covering services provided in only one calendar month.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N75</td><td class="description">Missing/incomplete/invalid tooth surface information.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N76</td><td class="description">Missing/incomplete/invalid number of riders.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N77</td><td class="description">Missing/incomplete/invalid designated provider number.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N78</td><td class="description">The necessary components of the child and teen checkup (EPSDT) were not completed.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N79</td><td class="description">Service billed is not compatible with patient location information.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N80</td><td class="description">Missing/incomplete/invalid prenatal screening information.<br />Start: 01/01/2000 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N81</td><td class="description">Procedure billed is not compatible with tooth surface code.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N82</td><td class="description">Provider must accept insurance payment as payment in full when a third party payer contract specifies full reimbursement.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N83</td><td class="description">No appeal rights. Adjudicative decision based on the provisions of a demonstration project.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N84</td><td class="description">Alert: Further installment payments are forthcoming.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N85</td><td class="description">Alert: This is the final installment payment.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07, 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N86</td><td class="description">A failed trial of pelvic muscle exercise training is required in order for biofeedback training for the treatment of urinary incontinence to be covered.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N87</td><td class="description">Home use of biofeedback therapy is not covered.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N88</td><td class="description">Alert: This payment is being made conditionally.  An HHA episode of care notice has been filed for this patient. When a patient is treated under a HHA episode of care, consolidated billing requires that certain therapy services and supplies, such as this, be included in the HHA's payment.  This payment will need to be recouped from you if we establish that the patient is concurrently receiving treatment under a HHA episode of care.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N89</td><td class="description">Alert: Payment information for this claim has been forwarded to more than one other payer, but format limitations permit only one of the secondary payers to be identified in this remittance advice.<br />Start: 01/01/2000 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N90</td><td class="description">Covered only when performed by the attending physician.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N91</td><td class="description">Services not included in the appeal review.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N92</td><td class="description">This facility is not certified for digital mammography.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N93</td><td class="description">A separate claim must be submitted for each place of service. Services furnished at multiple sites may not be billed in the same claim.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N94</td><td class="description">Claim/Service denied because a more specific taxonomy code is required for adjudication.<br />Start: 01/01/2000</td></tr>

<tr class="prod_set current"><td class="code">N95</td><td class="description">This provider type/provider specialty may not bill this service.<br />Start: 07/31/2001 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N96</td><td class="description">Patient must be refractory to conventional therapy (documented behavioral, pharmacologic and/or surgical corrective therapy) and be an appropriate surgical candidate such that implantation with anesthesia can occur.<br />Start: 08/24/2001</td></tr>

<tr class="prod_set current"><td class="code">N97</td><td class="description">Patients with stress incontinence, urinary obstruction, and specific neurologic diseases (e.g., diabetes with peripheral nerve involvement) which are associated with secondary manifestations of the above three indications are excluded.<br />Start: 08/24/2001</td></tr>

<tr class="prod_set current"><td class="code">N98</td><td class="description">Patient must have had a successful test stimulation in order to support subsequent implantation. Before a patient is eligible for permanent implantation, he/she must demonstrate a 50 percent or greater improvement through test stimulation. Improvement is measured through voiding diaries.<br />Start: 08/24/2001</td></tr>

<tr class="prod_set current"><td class="code">N99</td><td class="description">Patient must be able to demonstrate adequate ability to record voiding diary data such that clinical results of the implant procedure can be properly evaluated.<br />Start: 08/24/2001</td></tr>

<tr class="prod_set current tobe"><td class="code">N100</td><td class="description">PPS (Prospect Payment System) code corrected during adjudication.<br />Start: 09/14/2001 | Stop: 11/01/2016 | Last Modified: 11/01/2015<br />Notes: (Modified 6/30/03, 11/1/2015)</td></tr>

<tr class="prod_set deactivated"><td class="code">N101</td><td class="description">Additional information is needed in order to process this claim. Please resubmit the claim with the identification number of the provider where this service took place. The Medicare number of the site of service provider should be preceded with the letters 'HSP' and entered into item #32 on the claim form. You may bill only one site of service provider number per claim.<br />Start: 10/31/2001 | Stop: 01/31/2004 | Last Modified: 03/14/2014<br />Notes: Consider using MA105 (Modified 3/14/2014)</td></tr>

<tr class="prod_set current tobe"><td class="code">N102</td><td class="description">This claim has been denied without reviewing the medical/dental record because the requested records were not received or were not received timely.<br />Start: 10/31/2001 | Stop: 07/01/2016 | Last Modified: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N103</td><td class="description">Records indicate this patient was a prisoner or in custody of a Federal, State, or local authority when the service was rendered. This  payer does not cover items and services furnished to an individual while he or she is in custody under a penal statute or rule, unless under State or local law, the individual is personally liable for the cost of his or her health care while in custody and the State or local government pursues the collection of such debt in the same way and with the same vigor as the collection of its other debts. The provider can collect from the Federal/State/ Local Authority as appropriate.<br />Start: 10/31/2001 | Last Modified: 11/01/2013<br />Notes: (Modified 6/30/03, 7/1/12, 11/1/13)</td></tr>

<tr class="prod_set current"><td class="code">N104</td><td class="description">This claim/service is not payable under our claims jurisdiction area. You can identify the correct Medicare contractor to process this claim/service through the CMS website at www.cms.gov.<br />Start: 01/29/2002 | Last Modified: 07/01/2010<br />Notes: (Modified 10/31/02, 7/1/10)</td></tr>

<tr class="prod_set current"><td class="code">N105</td><td class="description">This is a misdirected claim/service for an RRB beneficiary. Submit paper claims to the RRB carrier: Palmetto GBA, P.O. Box 10066, Augusta, GA 30999. Call 866-749-4301 for RRB EDI information for electronic claims processing.<br />Start: 01/29/2002</td></tr>

<tr class="prod_set current"><td class="code">N106</td><td class="description">Payment for services furnished to Skilled Nursing Facility (SNF) inpatients (except for excluded services) can only be made to the SNF. You must request payment from the SNF rather than the patient for this service.<br />Start: 01/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N107</td><td class="description">Services furnished to Skilled Nursing Facility (SNF) inpatients must be billed on the inpatient claim. They cannot be billed separately as outpatient services.<br />Start: 01/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N108</td><td class="description">Missing/incomplete/invalid upgrade information.<br />Start: 01/31/2002 | Last Modified: 02/28/2003<br />Notes: (Modified 2/28/03)</td></tr>

<tr class="prod_set current"><td class="code">N109</td><td class="description">Alert: This claim/service was chosen for complex review.<br />Start: 02/28/2002 | Last Modified: 07/01/2015<br />Notes: (Modified 3/1/2009, 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">N110</td><td class="description">This facility is not certified for film mammography.<br />Start: 02/28/2002</td></tr>

<tr class="prod_set current"><td class="code">N111</td><td class="description">No appeal right except duplicate claim/service issue. This service was included in a claim that has been previously billed and adjudicated.<br />Start: 02/28/2002</td></tr>

<tr class="prod_set current"><td class="code">N112</td><td class="description">This claim is excluded from your electronic remittance advice.<br />Start: 02/28/2002</td></tr>

<tr class="prod_set current"><td class="code">N113</td><td class="description">Only one initial visit is covered per physician, group practice or provider.<br />Start: 04/16/2002 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N114</td><td class="description">During the transition to the Ambulance Fee Schedule, payment is based on the lesser of a blended amount calculated using a percentage of the reasonable charge/cost and fee schedule amounts, or the submitted charge for the service.  You will be notified yearly what the percentages for the blended payment calculation will be.<br />Start: 05/30/2002</td></tr>

<tr class="prod_set current"><td class="code">N115</td><td class="description">This decision was based on a Local Coverage Determination (LCD).  An LCD provides a guide to assist in determining whether a particular item or service is covered. A copy of this policy is available at www.cms.gov/mcd, or if you do not have web access, you may contact the contractor to request a copy of the LCD.<br />Start: 05/30/2002 | Last Modified: 07/01/2010<br />Notes: (Modified 4/1/04, 7/1/10)</td></tr>

<tr class="prod_set current"><td class="code">N116</td><td class="description">This payment is being made conditionally because the service was provided in the home, and it is possible that the patient is under a home health episode of care.  When a patient is treated under a home health episode of care, consolidated billing requires that certain therapy services and supplies, such as this, be included in the home health agency's (HHA's) payment.  This payment will need to be recouped from you if we establish that the patient is concurrently receiving treatment under an HHA episode of care.<br />Start: 06/30/2002</td></tr>

<tr class="prod_set current"><td class="code">N117</td><td class="description">This service is paid only once in a patient's lifetime.<br />Start: 07/30/2002 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N118</td><td class="description">This service is not paid if billed more than once every 28 days.<br />Start: 07/30/2002</td></tr>

<tr class="prod_set current"><td class="code">N119</td><td class="description">This service is not paid if billed once every 28 days, and the patient has spent 5 or more consecutive days in any inpatient or Skilled /nursing Facility (SNF) within those 28 days.<br />Start: 07/30/2002 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N120</td><td class="description">Payment is subject to home health prospective payment system partial episode payment adjustment. Patient was transferred/discharged/readmitted during payment episode.<br />Start: 08/09/2002 | Last Modified: 06/30/2003<br />Notes: (Modified 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N121</td><td class="description">Medicare Part B does not pay for items or services provided by this type of practitioner for beneficiaries in a Medicare Part A covered Skilled Nursing Facility (SNF) stay.<br />Start: 09/09/2002 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04, 6/30/03)</td></tr>

<tr class="prod_set current"><td class="code">N122</td><td class="description">Add-on code cannot be billed by itself.<br />Start: 09/12/2002 | Last Modified: 08/01/2005<br />Notes: (Modified 8/1/05)</td></tr>

<tr class="prod_set current"><td class="code">N123</td><td class="description">Alert: This is a split service and represents a portion of the units from the originally submitted service.<br />Start: 09/24/2002 | Last Modified: 03/01/2016<br />Notes: (Modified 3/1/2016)</td></tr>

<tr class="prod_set current"><td class="code">N124</td><td class="description">Payment has been denied for the/made only for a less extensive service/item because the information furnished does not substantiate the need for the (more extensive) service/item. The patient is liable for the charges for this service/item as you informed the patient in writing before the service/item was furnished that we would not pay for it, and the patient agreed to pay.<br />Start: 09/26/2002</td></tr>

<tr class="prod_set current"><td class="code">N125</td><td class="description">Payment has been (denied for the/made only for a less extensive) service/item because the information furnished does not substantiate the need for the (more extensive) service/item. If you have collected any amount from the patient, you must refund that amount to the patient within 30 days of receiving this notice.<br /><br />The requirements for a refund are in S1834(a)(18) of the Social Security Act (and in SS1834(j)(4) and 1879(h) by cross-reference to S1834(a)(18)). Section 1834(a)(18)(B) specifies that suppliers which knowingly and willfully fail to make appropriate refunds may be subject to civil money penalties and/or exclusion from the Medicare program. If you have any questions about this notice, please contact this office.<br />Start: 09/26/2002 | Last Modified: 08/01/2005<br />Notes: (Modified 8/1/05. Also refer to N356)</td></tr>

<tr class="prod_set current"><td class="code">N126</td><td class="description">Social Security Records indicate that this individual has been deported. This payer does not cover items and services furnished to individuals who have been deported.<br />Start: 10/17/2002</td></tr>

<tr class="prod_set current"><td class="code">N127</td><td class="description">This is a misdirected claim/service for a United Mine Workers of America (UMWA) beneficiary. Please submit claims to them.<br />Start: 10/31/2007 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04</td></tr>

<tr class="prod_set current"><td class="code">N128</td><td class="description">This amount represents the prior to coverage portion of the allowance.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N129</td><td class="description">Not eligible due to the patient's age.<br />Start: 10/31/2002 | Last Modified: 08/01/2007<br />Notes: (Modified 8/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N130</td><td class="description">Consult plan benefit documents/guidelines for information about restrictions for this service.<br />Start: 10/31/2002 | Last Modified: 11/01/2009<br />Notes: (Modified 4/1/07, 7/1/08, 11/1/09)</td></tr>

<tr class="prod_set current"><td class="code">N131</td><td class="description">Total payments under multiple contracts cannot exceed the allowance for this service.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N132</td><td class="description">Alert: Payments will cease for services rendered by this US Government debarred or excluded provider after the 30 day grace period as previously notified.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N133</td><td class="description">Alert: Services for predetermination and services requesting payment are being processed separately.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N134</td><td class="description">Alert: This represents your scheduled payment for this service. If treatment has been discontinued, please contact Customer Service.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N135</td><td class="description">Record fees are the patient's responsibility and limited to the specified co-payment.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N136</td><td class="description">Alert: To obtain information on the process to file an appeal in Arizona, call the Department's Consumer Assistance Office at (602) 912-8444 or (800) 325-2548.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N137</td><td class="description">Alert: The provider acting on the Member's behalf, may file an appeal with the Payer. The provider, acting on the Member's behalf, may file a complaint with the State Insurance Regulatory Authority without first filing an appeal, if the coverage decision involves an urgent condition for which care has not been rendered. The address may be obtained from the State Insurance Regulatory Authority.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified  8/1/04, 2/28/03, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N138</td><td class="description">Alert: In the event you disagree with the Dental Advisor's opinion and have additional information relative to the case, you may submit radiographs to the Dental Advisor Unit at the subscriber's dental insurance carrier for a second Independent Dental Advisor Review.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N139</td><td class="description">Alert: Under the Code of Federal Regulations, Chapter 32, Section 199.13 a non-participating provider is not an appropriate appealing party. Therefore, if you disagree with the Dental Advisor's opinion, you may appeal the determination if appointed in writing, by the beneficiary, to act as his/her representative. Should you be appointed as a representative, submit a copy of this letter, a signed statement explaining the matter in which you disagree, and any radiographs and relevant information to the subscriber's Dental insurance carrier within 90 days from the date of this letter.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N140</td><td class="description">Alert: You have not been designated as an authorized OCONUS provider therefore are not considered an appropriate appealing party. If the beneficiary has appointed you, in writing, to act as his/her representative and you disagree with the Dental Advisor's opinion, you may appeal by submitting a copy of this letter, a signed statement explaining the matter in which you disagree, and any relevant information to the subscriber's Dental insurance carrier within 90 days from the date of this letter.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N141</td><td class="description">The patient was not residing in a long-term care facility during all or part of the service dates billed.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N142</td><td class="description">The original claim was denied.  Resubmit a new claim, not a replacement claim.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N143</td><td class="description">The patient was not in a hospice program during all or part of the service dates billed.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N144</td><td class="description">The rate changed during the dates of service billed.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set deactivated"><td class="code">N145</td><td class="description">Missing/incomplete/invalid provider identifier for this place of service.<br />Start: 10/31/2002 | Stop: 06/02/2005</td></tr>

<tr class="prod_set current"><td class="code">N146</td><td class="description">Missing screening document.<br />Start: 10/31/2002 | Last Modified: 08/01/2004<br />Notes: (Modified  8/1/04) Related to N243</td></tr>

<tr class="prod_set current"><td class="code">N147</td><td class="description">Long term care case mix or per diem rate cannot be determined because the patient ID number is missing, incomplete, or invalid on the assignment request.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N148</td><td class="description">Missing/incomplete/invalid date of last menstrual period.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N149</td><td class="description">Rebill all applicable services on a single claim.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N150</td><td class="description">Missing/incomplete/invalid model number.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N151</td><td class="description">Telephone contact services will not be paid until the face-to-face contact requirement has been met.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N152</td><td class="description">Missing/incomplete/invalid replacement claim information.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N153</td><td class="description">Missing/incomplete/invalid room and board rate.<br />Start: 10/31/2002</td></tr>

<tr class="prod_set current"><td class="code">N154</td><td class="description">Alert: This payment was delayed for correction of provider's mailing address.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N155</td><td class="description">Alert: Our records do not indicate that other insurance is on file.  Please submit other insurance information for our records.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N156</td><td class="description">Alert: The patient is responsible for the difference between the approved treatment and the elective treatment.<br />Start: 10/31/2002 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N157</td><td class="description">Transportation to/from this destination is not covered.<br />Start: 02/28/2003 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">N158</td><td class="description">Transportation in a vehicle other than an ambulance is not covered.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N159</td><td class="description">Payment denied/reduced because mileage is not covered when the patient is not in the ambulance.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N160</td><td class="description">The patient must choose an option before a payment can be made for this procedure/ equipment/ supply/ service.<br />Start: 02/28/2003 | Last Modified: 02/01/2004<br />Notes: (Modified 2/1/04)</td></tr>

<tr class="prod_set current"><td class="code">N161</td><td class="description">This drug/service/supply is covered only when the associated service is covered.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N162</td><td class="description">Alert: Although your claim was paid, you have billed for a test/specialty not included in your Laboratory Certification.  Your failure to correct the laboratory certification information will result in a denial of payment in the near future.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N163</td><td class="description">Medical record does not support code billed per the code definition.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set deactivated"><td class="code">N164</td><td class="description">Transportation to/from this destination is not covered.<br />Start: 02/28/2003 | Stop: 01/31/2004<br />Notes: Consider using N157</td></tr>

<tr class="prod_set deactivated"><td class="code">N165</td><td class="description">Transportation in a vehicle other than an ambulance is not covered.<br />Start: 02/28/2003 | Stop: 01/31/2004<br />Notes: Consider using N158)</td></tr>

<tr class="prod_set deactivated"><td class="code">N166</td><td class="description">Payment denied/reduced because mileage is not covered when the patient is not in the ambulance.<br />Start: 02/28/2003 | Stop: 01/31/2004<br />Notes: Consider using N159</td></tr>

<tr class="prod_set current"><td class="code">N167</td><td class="description">Charges exceed the post-transplant coverage limit.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set deactivated"><td class="code">N168</td><td class="description">The patient must choose an option before a payment can be made for this procedure/ equipment/ supply/ service.<br />Start: 02/28/2003 | Stop: 01/31/2004<br />Notes: Consider using N160</td></tr>

<tr class="prod_set deactivated"><td class="code">N169</td><td class="description">This drug/service/supply is covered only when the associated service is covered.<br />Start: 02/28/2003 | Stop: 01/31/2004<br />Notes: Consider using N161</td></tr>

<tr class="prod_set current"><td class="code">N170</td><td class="description">A new/revised/renewed certificate of medical necessity is needed.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N171</td><td class="description">Payment for repair or replacement is not covered or has exceeded the purchase price.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N172</td><td class="description">The patient is not liable for the denied/adjusted charge(s) for receiving any updated service/item.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N173</td><td class="description">No qualifying hospital stay dates were provided for this episode of care.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N174</td><td class="description">This is not a covered service/procedure/ equipment/bed, however patient liability is limited to amounts shown in the adjustments under group 'PR'.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N175</td><td class="description">Missing review organization approval.<br />Start: 02/28/2003 | Last Modified: 02/29/2008<br />Notes: (Modified 8/1/04, 2/29/08) Related to N241</td></tr>

<tr class="prod_set current"><td class="code">N176</td><td class="description">Services provided aboard a ship are covered only when the ship is of United States registry and is in United States waters. In addition, a doctor licensed to practice in the United States must provide the service.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N177</td><td class="description">Alert: We did not send this claim to patient's other insurer. They have indicated no additional payment can be made.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 6/30/03, 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N178</td><td class="description">Missing pre-operative images/visual field results.<br />Start: 02/28/2003 | Last Modified: 11/01/2013<br />Notes: (Modified 8/1/04, 11/1/13) Related to N244</td></tr>

<tr class="prod_set current"><td class="code">N179</td><td class="description">Additional information has been requested from the member.  The charges will be reconsidered upon receipt of that information.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N180</td><td class="description">This item or service does not meet the criteria for the category under which it was billed.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N181</td><td class="description">Additional information is required from another provider involved in this service.<br />Start: 02/28/2003 | Last Modified: 12/01/2006<br />Notes: (Modified 12/1/06)</td></tr>

<tr class="prod_set current"><td class="code">N182</td><td class="description">This claim/service must be billed according to the schedule for this plan.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N183</td><td class="description">Alert: This is a predetermination advisory message, when this service is submitted for payment additional documentation as specified in plan documents will be required to process benefits.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N184</td><td class="description">Rebill technical and professional components separately.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N185</td><td class="description">Alert: Do not resubmit this claim/service.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N186</td><td class="description">Non-Availability Statement (NAS) required for this service. Contact the nearest Military Treatment Facility (MTF) for assistance.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N187</td><td class="description">Alert: You may request a review in writing within the required time limits following receipt of this notice by following the instructions included in your contract or plan benefit documents.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N188</td><td class="description">The approved level of care does not match the procedure code submitted.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N189</td><td class="description">Alert: This service has been paid as a one-time exception to the plan's benefit restrictions.<br />Start: 02/28/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N190</td><td class="description">Missing contract indicator.<br />Start: 02/28/2003 | Last Modified: 08/01/2004<br />Notes: (Modified 8/1/04) Related to N229</td></tr>

<tr class="prod_set current"><td class="code">N191</td><td class="description">The provider must update insurance information directly with payer.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N192</td><td class="description">Patient is a Medicaid/Qualified Medicare Beneficiary.<br />Start: 02/28/2003</td></tr>

<tr class="prod_set current"><td class="code">N193</td><td class="description">Alert: Specific federal/state/local program may cover this service through another payer.<br />Start: 02/28/2003 | Last Modified: 11/01/2015<br />Notes: (Modified 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N194</td><td class="description">Technical component not paid if provider does not own the equipment used.<br />Start: 02/25/2003</td></tr>

<tr class="prod_set current"><td class="code">N195</td><td class="description">The technical component must be billed separately.<br />Start: 02/25/2003</td></tr>

<tr class="prod_set current"><td class="code">N196</td><td class="description">Alert: Patient eligible to apply for other coverage which may be primary.<br />Start: 02/25/2003 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N197</td><td class="description">The subscriber must update insurance information directly with payer.<br />Start: 02/25/2003</td></tr>

<tr class="prod_set current"><td class="code">N198</td><td class="description">Rendering provider must be affiliated with the pay-to provider.<br />Start: 02/25/2003</td></tr>

<tr class="prod_set current"><td class="code">N199</td><td class="description">Additional payment/recoupment approved based on payer-initiated review/audit.<br />Start: 02/25/2003 | Last Modified: 08/01/2006<br />Notes: (Modified 8/1/06)</td></tr>

<tr class="prod_set current"><td class="code">N200</td><td class="description">The professional component must be billed separately.<br />Start: 02/25/2003</td></tr>

<tr class="prod_set deactivated"><td class="code">N201</td><td class="description">A mental health facility is responsible for payment of outside providers who furnish these services/supplies to residents.<br />Start: 02/25/2003 | Stop: 01/01/2011<br />Notes: Consider using N538</td></tr>

<tr class="prod_set current"><td class="code">N202</td><td class="description">Alert: Additional information/explanation will be sent separately.<br />Start: 06/30/2003 | Last Modified: 11/01/2015<br />Notes: (Modified 4/1/07, 11/1/09, 3/14/2014, 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N203</td><td class="description">Missing/incomplete/invalid anesthesia time/units.<br />Start: 06/30/2003 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N204</td><td class="description">Services under review for possible pre-existing condition. Send medical records for prior 12 months<br />Start: 06/30/2003</td></tr>

<tr class="prod_set current"><td class="code">N205</td><td class="description">Information provided was illegible.<br />Start: 06/30/2003 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N206</td><td class="description">The supporting documentation does not match the information sent on the claim.<br />Start: 06/30/2003 | Last Modified: 03/06/2012<br />Notes: (Modified 3/6/12)</td></tr>

<tr class="prod_set current"><td class="code">N207</td><td class="description">Missing/incomplete/invalid weight.<br />Start: 06/30/2003 | Last Modified: 11/18/2005<br />Notes: (Modified 11/18/05)</td></tr>

<tr class="prod_set current"><td class="code">N208</td><td class="description">Missing/incomplete/invalid DRG code.<br />Start: 06/30/2003 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N209</td><td class="description">Missing/incomplete/invalid taxpayer identification number (TIN).<br />Start: 06/30/2003 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N210</td><td class="description">Alert: You may appeal this decision.<br />Start: 06/30/2003 | Last Modified: 03/14/2014<br />Notes: (Modified 4/1/07, 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N211</td><td class="description">Alert: You may not appeal this decision.<br />Start: 06/30/2003 | Last Modified: 03/14/2014<br />Notes: (Modified 4/1/07, 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N212</td><td class="description">Charges processed under a Point of Service benefit .<br />Start: 02/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N213</td><td class="description">Missing/incomplete/invalid facility/discrete unit DRG/DRG exempt status information.<br />Start: 04/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N214</td><td class="description">Missing/incomplete/invalid history of the related initial surgical procedure(s).<br />Start: 04/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N215</td><td class="description">Alert: A payer providing supplemental or secondary coverage shall not require a claims determination for this service from a primary payer as a condition of making its own claims determination.<br />Start: 04/01/2004 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N216</td><td class="description">We do not offer coverage for this type of service or the patient is not enrolled in this portion of our benefit package.<br />Start: 04/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/1/2010, 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N217</td><td class="description">We pay only one site of service per provider per claim.<br />Start: 08/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N218</td><td class="description">You must furnish and service this item for as long as the patient continues to need it.  We can pay for maintenance and/or servicing for the time period specified in the contract or coverage manual.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N219</td><td class="description">Payment based on previous payer's allowed amount.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N220</td><td class="description">Alert: See the payer's web site or contact the payer's Customer Service department to obtain forms and instructions for filing a provider dispute.<br />Start: 08/01/2004 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N221</td><td class="description">Missing Admitting History and Physical report.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N222</td><td class="description">Incomplete/invalid Admitting History and Physical report.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N223</td><td class="description">Missing documentation of benefit to the patient during initial treatment period.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N224</td><td class="description">Incomplete/invalid documentation of benefit to the patient during initial treatment period.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set deactivated"><td class="code">N225</td><td class="description">Incomplete/invalid documentation/orders/notes/summary/report/chart.<br />Start: 08/01/2004 | Stop: 03/01/2016 | Last Modified: 03/01/2014<br />Notes: (Modified 8/1/05, 3/1/2014) Explicit RARCs have been approved, this non-specific RARC will be deactivated in March 2016.</td></tr>

<tr class="prod_set current"><td class="code">N226</td><td class="description">Incomplete/invalid American Diabetes Association Certificate of Recognition.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N227</td><td class="description">Incomplete/invalid Certificate of Medical Necessity.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N228</td><td class="description">Incomplete/invalid consent form.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N229</td><td class="description">Incomplete/invalid contract indicator.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N230</td><td class="description">Incomplete/invalid indication of whether the patient owns the equipment that requires the part or supply.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N231</td><td class="description">Incomplete/invalid invoice or statement certifying the actual cost of the lens, less discounts, and/or the type of intraocular lens used.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N232</td><td class="description">Incomplete/invalid itemized bill/statement.<br />Start: 08/01/2004 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N233</td><td class="description">Incomplete/invalid operative note/report.<br />Start: 08/01/2004 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N234</td><td class="description">Incomplete/invalid oxygen certification/re-certification.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N235</td><td class="description">Incomplete/invalid pacemaker registration form.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N236</td><td class="description">Incomplete/invalid pathology report.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N237</td><td class="description">Incomplete/invalid patient medical record for this service.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N238</td><td class="description">Incomplete/invalid physician certified plan of care.<br />Start: 08/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N239</td><td class="description">Incomplete/invalid physician financial relationship form.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N240</td><td class="description">Incomplete/invalid radiology report.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N241</td><td class="description">Incomplete/invalid review organization approval.<br />Start: 08/01/2004 | Last Modified: 02/29/2008<br />Notes: (Modified 2/29/08)</td></tr>

<tr class="prod_set current"><td class="code">N242</td><td class="description">Incomplete/invalid radiology film(s)/image(s).<br />Start: 08/01/2004 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N243</td><td class="description">Incomplete/invalid/not approved screening document.<br />Start: 08/01/2004</td></tr>

<tr class="prod_set current"><td class="code">N244</td><td class="description">Incomplete/Invalid pre-operative  images/visual field results.<br />Start: 08/01/2004 | Last Modified: 11/01/2013<br />Notes: (Modified 11/1/2013)</td></tr>

<tr class="prod_set current"><td class="code">N245</td><td class="description">Incomplete/invalid plan information for other insurance .<br />Start: 08/01/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N246</td><td class="description">State regulated patient payment limitations apply to this service.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N247</td><td class="description">Missing/incomplete/invalid assistant surgeon taxonomy.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N248</td><td class="description">Missing/incomplete/invalid assistant surgeon name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N249</td><td class="description">Missing/incomplete/invalid assistant surgeon primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N250</td><td class="description">Missing/incomplete/invalid assistant surgeon secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N251</td><td class="description">Missing/incomplete/invalid attending provider taxonomy.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N252</td><td class="description">Missing/incomplete/invalid attending provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N253</td><td class="description">Missing/incomplete/invalid attending provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N254</td><td class="description">Missing/incomplete/invalid attending provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N255</td><td class="description">Missing/incomplete/invalid billing provider taxonomy.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N256</td><td class="description">Missing/incomplete/invalid billing provider/supplier name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N257</td><td class="description">Missing/incomplete/invalid billing provider/supplier primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N258</td><td class="description">Missing/incomplete/invalid billing provider/supplier address.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N259</td><td class="description">Missing/incomplete/invalid billing provider/supplier secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N260</td><td class="description">Missing/incomplete/invalid billing provider/supplier contact information.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N261</td><td class="description">Missing/incomplete/invalid operating provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N262</td><td class="description">Missing/incomplete/invalid operating provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N263</td><td class="description">Missing/incomplete/invalid operating provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N264</td><td class="description">Missing/incomplete/invalid ordering provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N265</td><td class="description">Missing/incomplete/invalid ordering provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N266</td><td class="description">Missing/incomplete/invalid ordering provider address.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N267</td><td class="description">Missing/incomplete/invalid ordering provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N268</td><td class="description">Missing/incomplete/invalid ordering provider contact information.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N269</td><td class="description">Missing/incomplete/invalid other provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N270</td><td class="description">Missing/incomplete/invalid other provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N271</td><td class="description">Missing/incomplete/invalid other provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N272</td><td class="description">Missing/incomplete/invalid other payer attending provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N273</td><td class="description">Missing/incomplete/invalid other payer operating provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N274</td><td class="description">Missing/incomplete/invalid other payer other provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N275</td><td class="description">Missing/incomplete/invalid other payer purchased service provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N276</td><td class="description">Missing/incomplete/invalid other payer referring provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N277</td><td class="description">Missing/incomplete/invalid other payer rendering provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N278</td><td class="description">Missing/incomplete/invalid other payer service facility provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N279</td><td class="description">Missing/incomplete/invalid pay-to provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N280</td><td class="description">Missing/incomplete/invalid pay-to provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N281</td><td class="description">Missing/incomplete/invalid pay-to provider address.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N282</td><td class="description">Missing/incomplete/invalid pay-to provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N283</td><td class="description">Missing/incomplete/invalid purchased service provider identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N284</td><td class="description">Missing/incomplete/invalid referring provider taxonomy.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N285</td><td class="description">Missing/incomplete/invalid referring provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N286</td><td class="description">Missing/incomplete/invalid referring provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N287</td><td class="description">Missing/incomplete/invalid referring provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N288</td><td class="description">Missing/incomplete/invalid rendering provider taxonomy.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N289</td><td class="description">Missing/incomplete/invalid rendering provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N290</td><td class="description">Missing/incomplete/invalid rendering provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N291</td><td class="description">Missing/incomplete/invalid rendering provider secondary identifier.<br />Start: 12/02/2004 | Last Modified: 11/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N292</td><td class="description">Missing/incomplete/invalid service facility name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N293</td><td class="description">Missing/incomplete/invalid service facility primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N294</td><td class="description">Missing/incomplete/invalid service facility primary address.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N295</td><td class="description">Missing/incomplete/invalid service facility secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N296</td><td class="description">Missing/incomplete/invalid supervising provider name.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N297</td><td class="description">Missing/incomplete/invalid supervising provider primary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N298</td><td class="description">Missing/incomplete/invalid supervising provider secondary identifier.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N299</td><td class="description">Missing/incomplete/invalid occurrence date(s).<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N300</td><td class="description">Missing/incomplete/invalid occurrence span date(s).<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N301</td><td class="description">Missing/incomplete/invalid procedure date(s).<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N302</td><td class="description">Missing/incomplete/invalid other procedure date(s).<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N303</td><td class="description">Missing/incomplete/invalid principal procedure date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N304</td><td class="description">Missing/incomplete/invalid dispensed date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N305</td><td class="description">Missing/incomplete/invalid accident date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N306</td><td class="description">Missing/incomplete/invalid acute manifestation date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N307</td><td class="description">Missing/incomplete/invalid adjudication or payment date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N308</td><td class="description">Missing/incomplete/invalid appliance placement date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N309</td><td class="description">Missing/incomplete/invalid assessment date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N310</td><td class="description">Missing/incomplete/invalid assumed or relinquished care date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N311</td><td class="description">Missing/incomplete/invalid authorized to return to work date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N312</td><td class="description">Missing/incomplete/invalid begin therapy date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N313</td><td class="description">Missing/incomplete/invalid certification revision date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N314</td><td class="description">Missing/incomplete/invalid diagnosis date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N315</td><td class="description">Missing/incomplete/invalid disability from date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N316</td><td class="description">Missing/incomplete/invalid disability to date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N317</td><td class="description">Missing/incomplete/invalid discharge hour.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N318</td><td class="description">Missing/incomplete/invalid discharge or end of care date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N319</td><td class="description">Missing/incomplete/invalid hearing or vision prescription date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N320</td><td class="description">Missing/incomplete/invalid Home Health Certification Period.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N321</td><td class="description">Missing/incomplete/invalid last admission period.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N322</td><td class="description">Missing/incomplete/invalid last certification date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N323</td><td class="description">Missing/incomplete/invalid last contact date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N324</td><td class="description">Missing/incomplete/invalid last seen/visit date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N325</td><td class="description">Missing/incomplete/invalid last worked date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N326</td><td class="description">Missing/incomplete/invalid last x-ray date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N327</td><td class="description">Missing/incomplete/invalid other insured birth date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N328</td><td class="description">Missing/incomplete/invalid Oxygen Saturation Test date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N329</td><td class="description">Missing/incomplete/invalid patient birth date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N330</td><td class="description">Missing/incomplete/invalid patient death date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N331</td><td class="description">Missing/incomplete/invalid physician order date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N332</td><td class="description">Missing/incomplete/invalid prior hospital discharge date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N333</td><td class="description">Missing/incomplete/invalid prior placement date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N334</td><td class="description">Missing/incomplete/invalid re-evaluation date.<br />Start: 12/02/2004 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N335</td><td class="description">Missing/incomplete/invalid referral date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N336</td><td class="description">Missing/incomplete/invalid replacement date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N337</td><td class="description">Missing/incomplete/invalid secondary diagnosis date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N338</td><td class="description">Missing/incomplete/invalid shipped date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N339</td><td class="description">Missing/incomplete/invalid similar illness or symptom date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N340</td><td class="description">Missing/incomplete/invalid subscriber birth date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N341</td><td class="description">Missing/incomplete/invalid surgery date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N342</td><td class="description">Missing/incomplete/invalid test performed date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N343</td><td class="description">Missing/incomplete/invalid Transcutaneous Electrical Nerve Stimulator (TENS) trial start date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N344</td><td class="description">Missing/incomplete/invalid Transcutaneous Electrical Nerve Stimulator (TENS) trial end date.<br />Start: 12/02/2004</td></tr>

<tr class="prod_set current"><td class="code">N345</td><td class="description">Date range not valid with units submitted.<br />Start: 03/30/2005</td></tr>

<tr class="prod_set current"><td class="code">N346</td><td class="description">Missing/incomplete/invalid oral cavity designation code.<br />Start: 03/30/2005</td></tr>

<tr class="prod_set current"><td class="code">N347</td><td class="description">Your claim for a referred or purchased service cannot be paid because payment has already been made for this same service to another provider by a payment contractor representing the payer.<br />Start: 03/30/2005</td></tr>

<tr class="prod_set current"><td class="code">N348</td><td class="description">You chose that this service/supply/drug would be rendered/supplied and billed by a different practitioner/supplier.<br />Start: 08/01/2005</td></tr>

<tr class="prod_set current"><td class="code">N349</td><td class="description">The administration method and drug must be reported to adjudicate this service.<br />Start: 08/01/2005</td></tr>

<tr class="prod_set current"><td class="code">N350</td><td class="description">Missing/incomplete/invalid description of service for a Not Otherwise Classified (NOC) code or for an Unlisted/By Report procedure.<br />Start: 08/01/2005 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N351</td><td class="description">Service date outside of the approved treatment plan service dates.<br />Start: 08/01/2005</td></tr>

<tr class="prod_set current"><td class="code">N352</td><td class="description">Alert: There are no scheduled payments for this service. Submit a claim for each patient visit.<br />Start: 08/01/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N353</td><td class="description">Alert: Benefits have been estimated, when the actual services have been rendered, additional payment will be considered based on the submitted claim.<br />Start: 08/01/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N354</td><td class="description">Incomplete/invalid invoice.<br />Start: 08/01/2005 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N355</td><td class="description">Alert: The law permits exceptions to the refund requirement in two cases: - If you did not know, and could not have reasonably been expected to know, that we would not pay for this service; or - If you notified the patient in writing before providing the service that you believed that we were likely to deny the service, and the patient signed a statement agreeing to pay for the service.

If you come within either exception, or if you believe the carrier was wrong in its determination that we do not pay for this service, you should request appeal of this determination within 30 days of the date of this notice. Your request for review should include any additional information necessary to support your position.

If you request an appeal within 30 days of receiving this notice, you may delay refunding the amount to the patient until you receive the results of the review. If the review decision is favorable to you, you do not need to make any refund. If, however, the review is unfavorable, the law specifies that you must make the refund within 15 days of receiving the unfavorable review decision.

The law also permits you to request an appeal at any time within 120 days of the date you receive this notice. However, an appeal request that is received more than 30 days after the date of this notice, does not permit you to delay making the refund. Regardless of when a review is requested, the patient will be notified that you have requested one, and will receive a copy of the determination.

The patient has received a separate notice of this denial decision. The notice advises that he/she may be entitled to a refund of any amounts paid, if you should have known that we would not pay and did not tell him/her. It also instructs the patient to contact our office if he/she does not hear anything about a refund within 30 days<br />Start: 08/01/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 11/18/05, Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N356</td><td class="description">Not covered when performed with, or subsequent to, a non-covered service.<br />Start: 08/01/2005 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N357</td><td class="description">Time frame requirements between this service/procedure/supply and a related service/procedure/supply have not been met.<br />Start: 11/18/2005</td></tr>

<tr class="prod_set current"><td class="code">N358</td><td class="description">Alert: This decision may be reviewed if additional documentation as described in the contract or plan benefit documents is submitted.<br />Start: 11/18/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N359</td><td class="description">Missing/incomplete/invalid height.<br />Start: 11/18/2005</td></tr>

<tr class="prod_set current"><td class="code">N360</td><td class="description">Alert: Coordination of benefits has not been calculated when estimating benefits for this pre-determination. Submit payment information from the primary payer with the secondary claim.<br />Start: 11/18/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">N361</td><td class="description">Payment adjusted based on multiple diagnostic imaging procedure rules<br />Start: 11/18/2005 | Stop: 10/01/2007 | Last Modified: 12/01/2006<br />Notes: (Modified 12/1/06) Consider using Reason Code 59</td></tr>

<tr class="prod_set current"><td class="code">N362</td><td class="description">The number of Days or Units of Service exceeds our acceptable maximum.<br />Start: 11/18/2005</td></tr>

<tr class="prod_set current"><td class="code">N363</td><td class="description">Alert: in the near future we are implementing new policies/procedures that would affect this determination.<br />Start: 11/18/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set current"><td class="code">N364</td><td class="description">Alert: According to our agreement, you must waive the deductible and/or coinsurance amounts.<br />Start: 11/18/2005 | Last Modified: 04/01/2007<br />Notes: (Modified 4/1/07)</td></tr>

<tr class="prod_set deactivated"><td class="code">N365</td><td class="description">This procedure code is not payable. It is for reporting/information purposes only.<br />Start: 04/01/2006 | Stop: 07/01/2014<br />Notes: Consider Using CARC 246 or N620</td></tr>

<tr class="prod_set current"><td class="code">N366</td><td class="description">Requested information not provided. The claim will be reopened if the information previously requested is submitted within one year after the date of this denial notice.<br />Start: 04/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N367</td><td class="description">Alert: The claim information has been forwarded to a Consumer Spending Account processor for review; for example, flexible spending account or health savings account.<br />Start: 04/01/2006 | Last Modified: 07/01/2008<br />Notes: (Modified 4/1/07, 11/5/07, 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N368</td><td class="description">You must appeal the determination of the previously adjudicated claim.<br />Start: 04/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N369</td><td class="description">Alert: Although this claim has been processed, it is deficient according to state legislation/regulation.<br />Start: 04/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N370</td><td class="description">Billing exceeds the rental months covered/approved by the payer.<br />Start: 08/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N371</td><td class="description">Alert: title of this equipment must be transferred to the patient.<br />Start: 08/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N372</td><td class="description">Only reasonable and necessary maintenance/service charges are covered.<br />Start: 08/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N373</td><td class="description">It has been determined that another payer paid the services as primary when they were not the primary payer. Therefore, we are refunding to the payer that paid as primary on your behalf.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N374</td><td class="description">Primary Medicare Part A insurance has been exhausted and a Part B Remittance Advice is required.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N375</td><td class="description">Missing/incomplete/invalid questionnaire/information required to determine dependent eligibility.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N376</td><td class="description">Subscriber/patient is assigned to active military duty, therefore primary coverage may be TRICARE.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N377</td><td class="description">Payment based on a processed replacement claim.<br />Start: 12/01/2006 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">N378</td><td class="description">Missing/incomplete/invalid prescription quantity.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N379</td><td class="description">Claim level information does not match line level information.<br />Start: 12/01/2006</td></tr>

<tr class="prod_set current"><td class="code">N380</td><td class="description">The original claim  has been processed, submit a corrected claim.<br />Start: 04/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N381</td><td class="description">Alert: Consult our contractual agreement for restrictions/billing/payment information related to these charges.<br />Start: 04/01/2007 | Last Modified: 07/01/2015<br />Notes: (Modified 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">N382</td><td class="description">Missing/incomplete/invalid patient identifier.<br />Start: 04/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N383</td><td class="description">Not covered when deemed cosmetic.<br />Start: 04/01/2007 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N384</td><td class="description">Records indicate that the referenced body part/tooth has been removed in a previous procedure.<br />Start: 04/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N385</td><td class="description">Notification of admission was not timely according to published plan procedures.<br />Start: 04/01/2007 | Last Modified: 11/05/2007<br />Notes: (Modified 11/5/07)</td></tr>

<tr class="prod_set current"><td class="code">N386</td><td class="description">This decision was based on a National Coverage Determination (NCD). An NCD provides a coverage determination as to whether a particular item or service is covered. A copy of this policy is available at www.cms.gov/mcd/search.asp. If you do not have web access, you may contact the contractor to request a copy of the NCD.<br />Start: 04/01/2007 | Last Modified: 07/01/2010<br />Notes: (Modified 7/1/2010)</td></tr>

<tr class="prod_set current"><td class="code">N387</td><td class="description">Alert: Submit this claim to the patient's other insurer for potential payment of supplemental benefits. We did not forward the claim information.<br />Start: 04/01/2007 | Last Modified: 03/01/2009<br />Notes: (Modified 3/1/2009)</td></tr>

<tr class="prod_set current"><td class="code">N388</td><td class="description">Missing/incomplete/invalid prescription number.<br />Start: 08/01/2007 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N389</td><td class="description">Duplicate prescription number submitted.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N390</td><td class="description">This service/report cannot be billed separately.<br />Start: 08/01/2007 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N391</td><td class="description">Missing emergency department records.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N392</td><td class="description">Incomplete/invalid emergency department records.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N393</td><td class="description">Missing progress notes/report.<br />Start: 08/01/2007 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N394</td><td class="description">Incomplete/invalid progress notes/report.<br />Start: 08/01/2007 | Last Modified: 07/01/2008<br />Notes: (Modified 7/1/08)</td></tr>

<tr class="prod_set current"><td class="code">N395</td><td class="description">Missing laboratory report.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N396</td><td class="description">Incomplete/invalid laboratory report.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N397</td><td class="description">Benefits are not available for incomplete service(s)/undelivered item(s).<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N398</td><td class="description">Missing elective consent form.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N399</td><td class="description">Incomplete/invalid elective consent form.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N400</td><td class="description">Alert: Electronically enabled providers should submit claims electronically.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N401</td><td class="description">Missing periodontal charting.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N402</td><td class="description">Incomplete/invalid periodontal charting.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N403</td><td class="description">Missing facility certification.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N404</td><td class="description">Incomplete/invalid facility certification.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N405</td><td class="description">This service is only covered when the donor's insurer(s) do not provide coverage for the service.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N406</td><td class="description">This service is only covered when the recipient's insurer(s) do not provide coverage for the service.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N407</td><td class="description">You are not an approved submitter for this transmission format.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N408</td><td class="description">This payer does not cover deductibles assessed by a previous payer.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N409</td><td class="description">This service is related to an accidental injury and is not covered unless provided within a specific time frame from the date of the accident.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N410</td><td class="description">Not covered unless the prescription changes.<br />Start: 08/01/2007 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set deactivated"><td class="code">N411</td><td class="description">This service is allowed one time in a 6-month period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N412</td><td class="description">This service is allowed 2 times in a 12-month period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N413</td><td class="description">This service is allowed 2 times in a benefit year. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N414</td><td class="description">This service is allowed 4 times in a 12-month period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N415</td><td class="description">This service is allowed 1 time in an 18-month period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N416</td><td class="description">This service is allowed 1 time in a 3-year period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set deactivated"><td class="code">N417</td><td class="description">This service is allowed 1 time in a 5-year period. (This temporary code will be deactivated on 2/1/09.  Must be used with Reason Code 119.)<br />Start: 08/01/2007 | Stop: 02/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N418</td><td class="description">Misrouted claim.  See the payer's claim submission instructions.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N419</td><td class="description">Claim payment was the result of a payer's retroactive adjustment due to a retroactive rate change.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N420</td><td class="description">Claim payment was the result of a payer's retroactive adjustment due to a Coordination of Benefits or Third Party Liability Recovery.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N421</td><td class="description">Claim payment was the result of a payer's retroactive adjustment due to a review organization decision.<br />Start: 08/01/2007 | Last Modified: 05/08/2008<br />Notes: (Modified 2/29/08, typo fixed 5/8/08)</td></tr>

<tr class="prod_set current"><td class="code">N422</td><td class="description">Claim payment was the result of a payer's retroactive adjustment due to a payer's contract incentive program.<br />Start: 08/01/2007 | Last Modified: 05/08/2008<br />Notes: (Typo fixed 5/8/08)</td></tr>

<tr class="prod_set current"><td class="code">N423</td><td class="description">Claim payment was the result of a payer's retroactive adjustment due to a non standard program.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N424</td><td class="description">Patient does not reside in the geographic area required for this type of payment.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N425</td><td class="description">Statutorily excluded service(s).<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N426</td><td class="description">No coverage when self-administered.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N427</td><td class="description">Payment for eyeglasses or contact lenses can be made only after cataract surgery.<br />Start: 08/01/2007</td></tr>

<tr class="prod_set current"><td class="code">N428</td><td class="description">Not covered when performed in this place of service.<br />Start: 08/01/2007 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N429</td><td class="description">Not covered when considered routine.<br />Start: 08/01/2007 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N430</td><td class="description">Procedure code is inconsistent with the units billed.<br />Start: 11/05/2007</td></tr>

<tr class="prod_set current"><td class="code">N431</td><td class="description">Not covered with this procedure.<br />Start: 11/05/2007 | Last Modified: 03/08/2011<br />Notes: (Modified 3/8/11)</td></tr>

<tr class="prod_set current"><td class="code">N432</td><td class="description">Alert: Adjustment based on a Recovery Audit.<br />Start: 11/05/2007 | Last Modified: 07/01/2015<br />Notes: (Modified 7/1/15)</td></tr>

<tr class="prod_set current"><td class="code">N433</td><td class="description">Resubmit this claim using only your National Provider Identifier (NPI).<br />Start: 02/29/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N434</td><td class="description">Missing/Incomplete/Invalid Present on Admission indicator.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N435</td><td class="description">Exceeds number/frequency approved /allowed within time period without support documentation.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N436</td><td class="description">The injury claim has not been accepted and a mandatory medical reimbursement has been made.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N437</td><td class="description">Alert: If the injury claim is accepted, these charges will be reconsidered.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N438</td><td class="description">This jurisdiction only accepts paper claims.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N439</td><td class="description">Missing anesthesia physical status report/indicators.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N440</td><td class="description">Incomplete/invalid anesthesia physical status report/indicators.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N441</td><td class="description">This missed/cancelled appointment is not covered.<br />Start: 07/01/2008 | Last Modified: 07/15/2013<br />Notes: (Modified 7/15/2013)</td></tr>

<tr class="prod_set current"><td class="code">N442</td><td class="description">Payment based on an alternate fee schedule.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N443</td><td class="description">Missing/incomplete/invalid total time or begin/end time.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N444</td><td class="description">Alert: This facility has not filed the Election for High Cost Outlier form with the Division of Workers' Compensation.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N445</td><td class="description">Missing document for actual cost or paid amount.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N446</td><td class="description">Incomplete/invalid document for actual cost or paid amount.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N447</td><td class="description">Payment is based on a generic equivalent as required documentation was not provided.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N448</td><td class="description">This drug/service/supply is not included in the fee schedule or contracted/legislated fee arrangement.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N449</td><td class="description">Payment based on a comparable drug/service/supply.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N450</td><td class="description">Covered only when performed by the primary treating physician or the designee.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N451</td><td class="description">Missing Admission Summary Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N452</td><td class="description">Incomplete/invalid Admission Summary Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N453</td><td class="description">Missing Consultation Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N454</td><td class="description">Incomplete/invalid Consultation Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N455</td><td class="description">Missing Physician Order.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N456</td><td class="description">Incomplete/invalid Physician Order.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N457</td><td class="description">Missing Diagnostic Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N458</td><td class="description">Incomplete/invalid Diagnostic Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N459</td><td class="description">Missing Discharge Summary.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N460</td><td class="description">Incomplete/invalid Discharge Summary.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N461</td><td class="description">Missing Nursing Notes.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N462</td><td class="description">Incomplete/invalid Nursing Notes.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N463</td><td class="description">Missing support data for claim.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N464</td><td class="description">Incomplete/invalid support data for claim.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N465</td><td class="description">Missing Physical Therapy Notes/Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N466</td><td class="description">Incomplete/invalid Physical Therapy Notes/Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N467</td><td class="description">Missing Tests and Analysis Report.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N468</td><td class="description">Incomplete/invalid Report of Tests and Analysis Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N469</td><td class="description">Alert: Claim/Service(s) subject to appeal process, see section 935 of Medicare Prescription Drug, Improvement, and Modernization Act of 2003 (MMA).<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N470</td><td class="description">This payment will complete the mandatory medical reimbursement limit.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N471</td><td class="description">Missing/incomplete/invalid HIPPS Rate Code.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N472</td><td class="description">Payment for this service has been issued to another provider.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N473</td><td class="description">Missing certification.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N474</td><td class="description">Incomplete/invalid certification.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N475</td><td class="description">Missing completed referral form.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N476</td><td class="description">Incomplete/invalid completed referral form.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N477</td><td class="description">Missing Dental Models.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N478</td><td class="description">Incomplete/invalid Dental Models.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N479</td><td class="description">Missing Explanation of Benefits (Coordination of Benefits or Medicare Secondary Payer).<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N480</td><td class="description">Incomplete/invalid Explanation of Benefits (Coordination of Benefits or Medicare Secondary Payer).<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N481</td><td class="description">Missing Models.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N482</td><td class="description">Incomplete/invalid Models.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set deactivated"><td class="code">N483</td><td class="description">Missing Periodontal Charts.<br />Start: 07/01/2008 | Stop: 05/01/2015 | Last Modified: 11/01/2014<br />Notes: (Modified 11/1/2014)</td></tr>

<tr class="prod_set deactivated"><td class="code">N484</td><td class="description">Incomplete/invalid Periodontal Charts.<br />Start: 07/01/2008 | Stop: 05/01/2015 | Last Modified: 11/01/2014<br />Notes: (Modified 3/14/2014, 11/1/2014)</td></tr>

<tr class="prod_set current"><td class="code">N485</td><td class="description">Missing Physical Therapy Certification.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N486</td><td class="description">Incomplete/invalid Physical Therapy Certification.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N487</td><td class="description">Missing Prosthetics or Orthotics Certification.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N488</td><td class="description">Incomplete/invalid Prosthetics or Orthotics Certification.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N489</td><td class="description">Missing referral form.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N490</td><td class="description">Incomplete/invalid referral form.<br />Start: 07/01/2008 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N491</td><td class="description">Missing/Incomplete/Invalid Exclusionary Rider Condition.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N492</td><td class="description">Alert: A network provider may bill the member for this service if the member requested the service and agreed in writing, prior to receiving the service, to be financially responsible for the billed charge.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N493</td><td class="description">Missing Doctor First Report of Injury.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N494</td><td class="description">Incomplete/invalid Doctor First Report of Injury.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N495</td><td class="description">Missing Supplemental Medical Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N496</td><td class="description">Incomplete/invalid Supplemental Medical Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N497</td><td class="description">Missing Medical Permanent Impairment or Disability Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N498</td><td class="description">Incomplete/invalid Medical Permanent Impairment or Disability Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N499</td><td class="description">Missing Medical Legal Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N500</td><td class="description">Incomplete/invalid Medical Legal Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N501</td><td class="description">Missing Vocational Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N502</td><td class="description">Incomplete/invalid Vocational Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N503</td><td class="description">Missing Work Status Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N504</td><td class="description">Incomplete/invalid Work Status Report.<br />Start: 07/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N505</td><td class="description">Alert: This response includes only services that could be estimated in real time. No estimate will be provided for the services that could not be estimated in real time.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N506</td><td class="description">Alert: This is an estimate of the member's liability based on the information available at the time the estimate was processed. Actual coverage and member liability amounts will be determined when the claim is processed. This is not a pre-authorization or a guarantee of payment.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N507</td><td class="description">Plan distance requirements have not been met.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N508</td><td class="description">Alert: This real time claim adjudication response represents the member responsibility to the provider for services reported. The member will receive an Explanation of Benefits electronically or in the mail.  Contact the insurer if there are any questions.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N509</td><td class="description">Alert: A current inquiry shows the member's Consumer Spending Account contains sufficient funds to cover the member liability for this claim/service.  Actual payment from the Consumer Spending Account will depend on the availability of funds and determination of eligible services at the time of payment processing.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N510</td><td class="description">Alert: A current inquiry shows the member's Consumer Spending Account does not contain sufficient funds to cover the member's liability for this claim/service. Actual payment from the Consumer Spending Account will depend on the availability of funds and determination of eligible services at the time of payment processing.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N511</td><td class="description">Alert: Information on the availability of Consumer Spending Account funds to cover the member liability on this claim/service is not available at this time.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N512</td><td class="description">Alert: This is the initial remit of a non-NCPDP claim originally submitted real-time without change to the adjudication.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set current"><td class="code">N513</td><td class="description">Alert: This is the initial remit of a non-NCPDP claim originally submitted real-time with a change to the adjudication.<br />Start: 11/01/2008</td></tr>

<tr class="prod_set deactivated"><td class="code">N514</td><td class="description">Consult plan benefit documents/guidelines for information about restrictions for this service.<br />Start: 11/01/2008 | Stop: 01/01/2011<br />Notes: Consider using N130</td></tr>

<tr class="prod_set deactivated"><td class="code">N515</td><td class="description">Alert: Submit this claim to the patient's other insurer for potential payment of supplemental benefits. We did not forward the claim information. (use N387 instead)<br />Start: 11/01/2008 | Stop: 10/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N516</td><td class="description">Records indicate a mismatch between the submitted NPI and EIN.<br />Start: 03/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N517</td><td class="description">Resubmit a new claim with the requested information.<br />Start: 03/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N518</td><td class="description">No separate payment for accessories when furnished for use with oxygen equipment.<br />Start: 03/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N519</td><td class="description">Invalid combination of HCPCS modifiers.<br />Start: 07/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N520</td><td class="description">Alert: Payment made from a Consumer Spending Account.<br />Start: 07/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N521</td><td class="description">Mismatch between the submitted provider information and the provider information stored in our system.<br />Start: 11/01/2009</td></tr>

<tr class="prod_set current"><td class="code">N522</td><td class="description">Duplicate of a claim processed, or to be processed, as a crossover claim.<br />Start: 11/01/2009 | Last Modified: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N523</td><td class="description">The limitation on outlier payments defined by this payer for this service period has been met. The outlier payment otherwise applicable to this claim has not been paid.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N524</td><td class="description">Based on policy this payment constitutes payment in full.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N525</td><td class="description">These services are not covered when performed within the global period of another service.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N526</td><td class="description">Not qualified for recovery based on employer size.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N527</td><td class="description">We processed this claim as the primary payer prior to receiving the recovery demand.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N528</td><td class="description">Patient is entitled to benefits for Institutional Services only.<br />Start: 03/01/2010 | Last Modified: 07/01/2010<br />Notes: (Modified 7/1/10)</td></tr>

<tr class="prod_set current"><td class="code">N529</td><td class="description">Patient is entitled to benefits for Professional Services only.<br />Start: 03/01/2010 | Last Modified: 07/01/2010<br />Notes: (Modified 7/1/10)</td></tr>

<tr class="prod_set current"><td class="code">N530</td><td class="description">Not Qualified for Recovery based on enrollment information.<br />Start: 03/01/2010 | Last Modified: 07/01/2010<br />Notes: (Modified 7/1/10)</td></tr>

<tr class="prod_set current"><td class="code">N531</td><td class="description">Not qualified for recovery based on direct payment of premium.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N532</td><td class="description">Not qualified for recovery based on disability and working status.<br />Start: 03/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N533</td><td class="description">Services performed in an Indian Health Services facility under a self-insured tribal Group Health Plan.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N534</td><td class="description">This is an individual policy, the employer does not participate in plan sponsorship.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N535</td><td class="description">Payment is adjusted when procedure is performed in this place of service based on the submitted procedure code and place of service.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N536</td><td class="description">We are not changing the prior payer's determination of patient responsibility, which you may collect, as this service is not covered by us.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N537</td><td class="description">We have examined claims history and no records of the services have been found.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N538</td><td class="description">A facility is responsible for payment to outside providers who furnish these services/supplies/drugs to its patients/residents.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N539</td><td class="description">Alert: We processed appeals/waiver requests on your behalf and that request has been denied.<br />Start: 07/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N540</td><td class="description">Payment adjusted based on the interrupted stay policy.<br />Start: 11/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N541</td><td class="description">Mismatch between the submitted insurance type code and the information stored in our system.<br />Start: 11/01/2010</td></tr>

<tr class="prod_set current"><td class="code">N542</td><td class="description">Missing income verification.<br />Start: 03/08/2011</td></tr>

<tr class="prod_set current"><td class="code">N543</td><td class="description">Incomplete/invalid income verification.<br />Start: 03/08/2011 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N544</td><td class="description">Alert: Although this was paid, you have billed with a referring/ordering provider that does not match our system record. Unless corrected this will not be paid in the future.<br />Start: 07/01/2011 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N545</td><td class="description">Payment reduced based on status as an unsuccessful eprescriber per the Electronic Prescribing (eRx) Incentive Program.<br />Start: 07/01/2011</td></tr>

<tr class="prod_set current"><td class="code">N546</td><td class="description">Payment represents a previous reduction based on the Electronic Prescribing (eRx) Incentive Program.<br />Start: 07/01/2011</td></tr>

<tr class="prod_set current"><td class="code">N547</td><td class="description">A refund request (Frequency Type Code 8) was processed previously.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set current"><td class="code">N548</td><td class="description">Alert: Patient's calendar year deductible has been met.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set current"><td class="code">N549</td><td class="description">Alert: Patient's calendar year out-of-pocket maximum has been met.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set current"><td class="code">N550</td><td class="description">Alert: You have not responded to requests to revalidate your provider/supplier enrollment information. Your failure to revalidate your enrollment information will result in a payment hold in the near future.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set current"><td class="code">N551</td><td class="description">Payment adjusted based on the Ambulatory Surgical Center (ASC) Quality Reporting Program.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set current"><td class="code">N552</td><td class="description">Payment adjusted to reverse a previous withhold/bonus amount.<br />Start: 03/06/2012</td></tr>

<tr class="prod_set deactivated"><td class="code">N553</td><td class="description">Payment adjusted based on a Low Income Subsidy (LIS) retroactive coverage or status change.<br />Start: 03/06/2012 | Stop: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N554</td><td class="description">Missing/Incomplete/Invalid Family Planning Indicator.<br />Start: 07/01/2012 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N555</td><td class="description">Missing medication list.<br />Start: 07/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N556</td><td class="description">Incomplete/invalid medication list.<br />Start: 07/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N557</td><td class="description">This claim/service is not payable under our service area. The claim must be filed to the Payer/Plan in whose service area the specimen was collected.<br />Start: 07/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N558</td><td class="description">This claim/service is not payable under our service area. The claim must be filed to the Payer/Plan in whose service area the equipment was received.<br />Start: 07/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N559</td><td class="description">This claim/service is not payable under our service area. The claim must be filed to the Payer/Plan in whose service area the Ordering Physician is located.<br />Start: 07/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N560</td><td class="description">The pilot program requires an interim or final claim within 60 days of the Notice of  Admission. A claim was not received.<br />Start: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N561</td><td class="description">The bundled claim originally submitted for this episode of care includes related readmissions. You may resubmit the original claim to receive a corrected payment based on this readmission.<br />Start: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N562</td><td class="description">The provider number of your incoming claim does not match the provider number on the processed Notice of Admission (NOA) for this bundled payment.<br />Start: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N563</td><td class="description">Alert: Missing required provider/supplier issuance of advance patient notice of non-coverage. The patient is not liable for payment for this service.<br />Start: 11/01/2012 | Last Modified: 11/01/2015<br />Notes: Related to M39 (Modified 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N564</td><td class="description">Patient did not meet the inclusion criteria for the demonstration project or pilot program.<br />Start: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N565</td><td class="description">Alert: This non-payable reporting code requires a modifier. Future claims containing this non-payable reporting code must include an appropriate modifier for the claim to be processed.<br />Start: 11/01/2012 | Last Modified: 03/01/2013<br />Notes: (Modified 3/1/13)</td></tr>

<tr class="prod_set current"><td class="code">N566</td><td class="description">Alert: This procedure code requires functional reporting. Future claims containing this procedure code must include an applicable non-payable code and appropriate modifiers for the claim to be processed.<br />Start: 11/01/2012</td></tr>

<tr class="prod_set current"><td class="code">N567</td><td class="description">Not covered when considered preventative.<br />Start: 03/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N568</td><td class="description">Alert: Initial payment based on the Notice of Admission (NOA) under the Bundled Payment Model IV initiative.<br />Start: 03/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N569</td><td class="description">Not covered when performed for the reported diagnosis.<br />Start: 03/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N570</td><td class="description">Missing/incomplete/invalid credentialing data.<br />Start: 03/01/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N571</td><td class="description">Alert: Payment will be issued quarterly by another payer/contractor.<br />Start: 03/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N572</td><td class="description">This procedure is not payable unless appropriate non-payable reporting codes and associated modifiers are submitted.<br />Start: 03/01/2013 | Last Modified: 07/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N573</td><td class="description">Alert: You have been overpaid and must refund the overpayment. The refund will be requested separately by another payer/contractor.<br />Start: 03/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N574</td><td class="description">Our records indicate the ordering/referring provider is of a type/specialty that cannot order or refer. Please verify that the claim ordering/referring provider information is accurate or contact the ordering/referring provider.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N575</td><td class="description">Mismatch between the submitted ordering/referring provider name and the ordering/referring provider name stored in our records.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N576</td><td class="description">Services not related to the specific incident/claim/accident/loss being reported.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N577</td><td class="description">Personal Injury Protection (PIP) Coverage.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N578</td><td class="description">Coverages do not apply to this loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N579</td><td class="description">Medical Payments Coverage (MPC).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N580</td><td class="description">Determination based on the provisions of the insurance policy.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N581</td><td class="description">Investigation of coverage eligibility is pending.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N582</td><td class="description">Benefits suspended pending the patient's cooperation.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N583</td><td class="description">Patient was not an occupant of our insured vehicle and therefore, is not an eligible injured person.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N584</td><td class="description">Not covered based on the insured's noncompliance with policy or statutory conditions.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N585</td><td class="description">Benefits are no longer available based on a final injury settlement.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N586</td><td class="description">The injured party does not qualify for benefits.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N587</td><td class="description">Policy benefits have been exhausted.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N588</td><td class="description">The patient has instructed that medical claims/bills are not to be paid.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N589</td><td class="description">Coverage is excluded to any person injured as a result of operating a motor vehicle while in an intoxicated condition or while the ability to operate such a vehicle is impaired by the use of a drug.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N590</td><td class="description">Missing independent medical exam detailing the cause of injuries sustained and medical necessity of services rendered.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N591</td><td class="description">Payment based on an Independent Medical Examination (IME) or Utilization Review (UR).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N592</td><td class="description">Adjusted because this is not the initial prescription or exceeds the amount allowed for the initial prescription.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N593</td><td class="description">Not covered based on failure to attend  a scheduled Independent Medical Exam (IME).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N594</td><td class="description">Records reflect the injured party did not complete an Application for Benefits for this loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N595</td><td class="description">Records reflect the injured party did not complete an Assignment of Benefits for this loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N596</td><td class="description">Records reflect the injured party did not complete a Medical Authorization for this loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N597</td><td class="description">Adjusted based on a medical/dental provider's apportionment of care between related injuries and other unrelated medical/dental conditions/injuries.<br />Start: 07/15/2013 | Last Modified: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N598</td><td class="description">Health care policy coverage is primary.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N599</td><td class="description">Our payment for this service is based upon a reasonable amount pursuant to both the terms and conditions of the policy of insurance under which the subject claim is being made as well as the Florida No-Fault Statute, which permits, when determining a reasonable charge for a service, an insurer to consider usual and customary charges and payments accepted by the provider, reimbursement levels in the community and various federal and state fee schedules applicable to automobile and other insurance coverages, and other information relevant to the reasonableness of the reimbursement for the service. The payment for this service is based upon 200% of the Participating Level of Medicare Part B fee schedule for the locale in which the services were rendered.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N600</td><td class="description">Adjusted based on the applicable fee schedule for the region in which the service was rendered.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N601</td><td class="description">In accordance with Hawaii Administrative Rules, Title 16, Chapter 23 Motor Vehicle Insurance Law payment is recommended based on Medicare Resource Based Relative Value Scale System applicable to Hawaii.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N602</td><td class="description">Adjusted based on the Redbook maximum allowance.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N603</td><td class="description">This fee is calculated according to the New Jersey medical fee schedules for Automobile Personal Injury Protection and Motor Bus Medical Expense Insurance Coverage.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N604</td><td class="description">In accordance with New York No-Fault Law, Regulation 68, this base fee was calculated according to the New York Workers' Compensation Board Schedule of Medical Fees, pursuant to Regulation 83 and / or Appendix 17-C of 11 NYCRR.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N605</td><td class="description">This fee was calculated based upon New York All Patients Refined Diagnosis Related Groups (APR-DRG), pursuant to Regulation 68.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N606</td><td class="description">The Oregon allowed amount for this procedure is based upon the Workers Compensation Fee Schedule (OAR 436-009).  The allowed amount has been calculated in accordance with Section 4 of ORS 742.524.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N607</td><td class="description">Service provided for non-compensable condition(s).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N608</td><td class="description">The fee schedule amount allowed is calculated at 110% of the Medicare Fee Schedule for this region, specialty and type of service.  This fee is calculated in compliance with Act 6.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N609</td><td class="description">80% of the provider's billed amount is being recommended for payment according to Act 6.<br />Start: 07/15/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N610</td><td class="description">Alert: Payment based on an appropriate level of care.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N611</td><td class="description">Claim in litigation.  Contact insurer for more information.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N612</td><td class="description">Medical provider not authorized/certified to provide treatment to  injured workers in this jurisdiction.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N613</td><td class="description">Alert: Although this was paid, you have billed with an ordering provider that needs to update their enrollment record. Please verify that the ordering provider information you submitted on the claim is accurate and if it is, contact the ordering provider instructing them to update their enrollment record. Unless corrected, a claim with this ordering provider will not be paid in the future.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N614</td><td class="description">Alert: Additional information is included in the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N615</td><td class="description">Alert: This enrollee receiving advance payments of the premium tax credit is in the grace period of three consecutive months for non-payment of premium. Under the Code of Federal Regulations, Title 45, Part 156.270, a Qualified Health Plan issuer must pay all appropriate claims for services rendered to the enrollee during the first month of the grace period and may pend claims for services rendered to the enrollee in the second and third months of the grace period.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N616</td><td class="description">Alert: This enrollee is in the first month of the advance premium tax credit grace period.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N617</td><td class="description">This enrollee is in the second or third month of the advance premium tax credit grace period.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N618</td><td class="description">Alert: This claim will automatically be reprocessed if the enrollee pays their premiums.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N619</td><td class="description">Coverage terminated for non-payment of premium.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N620</td><td class="description">Alert: This procedure code is for quality reporting/informational purposes only.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N621</td><td class="description">Charges for Jurisdiction required forms, reports, or chart notes are not payable.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N622</td><td class="description">Not covered based on the date of injury/accident.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N623</td><td class="description">Not covered when deemed unscientific/unproven/outmoded/experimental/excessive/inappropriate.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N624</td><td class="description">The associated Workers' Compensation claim has been withdrawn.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N625</td><td class="description">Missing/Incomplete/Invalid Workers' Compensation Claim Number.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N626</td><td class="description">New or established patient E/M codes are not payable with chiropractic care codes.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set deactivated"><td class="code">N627</td><td class="description">Service not payable per managed care contract.<br />Start: 07/15/2013 | Stop: 07/01/2014<br />Notes: Consider Use CARC 256</td></tr>

<tr class="prod_set current"><td class="code">N628</td><td class="description">Out-patient follow up visits on the same date of service as a scheduled test or treatment is disallowed.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N629</td><td class="description">Reviews/documentation/notes/summaries/reports/charts not requested.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N630</td><td class="description">Referral not authorized by attending physician.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N631</td><td class="description">Medical Fee Schedule does not list this code. An allowance was made for a comparable service.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set deactivated"><td class="code">N632</td><td class="description">According to the Official Medical Fee Schedule this service has a relative value of zero and therefore no payment is due.<br />Start: 07/15/2013 | Stop: 07/01/2014<br />Notes: Consider using W8</td></tr>

<tr class="prod_set current"><td class="code">N633</td><td class="description">Additional anesthesia time units are not allowed.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N634</td><td class="description">The allowance is calculated based on anesthesia time units.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N635</td><td class="description">The Allowance is calculated based on the anesthesia base units plus time.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N636</td><td class="description">Adjusted because this is reimbursable only once per injury.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N637</td><td class="description">Consultations are not allowed once treatment has been rendered by the same provider.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N638</td><td class="description">Reimbursement has been made according to the home health fee schedule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N639</td><td class="description">Reimbursement has been made according to the inpatient rehabilitation facilities fee schedule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N640</td><td class="description">Exceeds number/frequency approved/allowed within time period.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N641</td><td class="description">Reimbursement has been based on the number of body areas rated.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N642</td><td class="description">Adjusted when billed as individual tests instead of as a panel.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N643</td><td class="description">The services billed are considered Not Covered or Non-Covered (NC) in the applicable state fee schedule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N644</td><td class="description">Reimbursement has been made according to the bilateral procedure rule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N645</td><td class="description">Mark-up allowance.<br />Start: 07/15/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N646</td><td class="description">Reimbursement has been adjusted based on the guidelines for an assistant.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N647</td><td class="description">Adjusted based on diagnosis-related group (DRG).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N648</td><td class="description">Adjusted based on Stop Loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N649</td><td class="description">Payment based on invoice.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N650</td><td class="description">This policy was not in effect for this date of loss. No coverage is available.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N651</td><td class="description">No Personal Injury Protection/Medical Payments Coverage on the policy at the time of the loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N652</td><td class="description">The date of service is before the date of loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N653</td><td class="description">The date of injury does not match the reported date of loss.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N654</td><td class="description">Adjusted based on achievement of maximum medical improvement (MMI).<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N655</td><td class="description">Payment based on provider's geographic region.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N656</td><td class="description">An interest payment is being made because benefits are being paid outside the statutory requirement.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N657</td><td class="description">This should be billed with the appropriate code for these services.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N658</td><td class="description">The billed service(s) are not considered medical expenses.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N659</td><td class="description">This item is exempt from sales tax.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N660</td><td class="description">Sales tax has been included in the reimbursement.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N661</td><td class="description">Documentation does not support that the services rendered were medically necessary.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N662</td><td class="description">Alert: Consideration of payment will be made upon receipt of a final bill.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N663</td><td class="description">Adjusted based on an agreed amount.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N664</td><td class="description">Adjusted based on a legal settlement.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N665</td><td class="description">Services by an unlicensed provider are not reimbursable.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N666</td><td class="description">Only one evaluation and management code at this service level is covered during the course of care.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N667</td><td class="description">Missing prescription.<br />Start: 07/15/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N668</td><td class="description">Incomplete/invalid prescription.<br />Start: 07/15/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N669</td><td class="description">Adjusted based on the Medicare fee schedule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N670</td><td class="description">This service code has been identified as the primary procedure code subject to the Medicare Multiple Procedure Payment Reduction (MPPR) rule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N671</td><td class="description">Payment based on a jurisdiction cost-charge ratio.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N672</td><td class="description">Alert: Amount applied to Health Insurance Offset.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N673</td><td class="description">Reimbursement has been calculated based on an outpatient per diem or an outpatient factor and/or fee schedule amount.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N674</td><td class="description">Not covered unless a pre-requisite procedure/service has been provided.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N675</td><td class="description">Additional information is required from the injured party.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N676</td><td class="description">Service does not qualify for payment under the Outpatient Facility Fee Schedule.<br />Start: 07/15/2013</td></tr>

<tr class="prod_set current"><td class="code">N677</td><td class="description">Alert: Films/Images will not be returned.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N678</td><td class="description">Missing post-operative images/visual field results.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N679</td><td class="description">Incomplete/Invalid post-operative images/visual field results.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N680</td><td class="description">Missing/Incomplete/Invalid date of previous dental extractions.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N681</td><td class="description">Missing/Incomplete/Invalid full arch series.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N682</td><td class="description">Missing/Incomplete/Invalid history of prior periodontal therapy/maintenance.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N683</td><td class="description">Missing/Incomplete/Invalid prior treatment documentation.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N684</td><td class="description">Payment denied as this is a specialty claim submitted as a general claim.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N685</td><td class="description">Missing/Incomplete/Invalid Prosthesis, Crown or Inlay Code.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N686</td><td class="description">Missing/incomplete/Invalid questionnaire needed to complete payment determination.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N687</td><td class="description">Alert: This reversal is due to a retroactive disenrollment.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N688</td><td class="description">Alert: This reversal is due to a medical or utilization review decision.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N689</td><td class="description">Alert: This reversal is due to a retroactive rate change.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N690</td><td class="description">Alert: This reversal is due to a provider submitted appeal.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N691</td><td class="description">Alert: This reversal is due to a patient submitted appeal.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N692</td><td class="description">Alert: This reversal is due to an incorrect rate on the initial adjudication.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N693</td><td class="description">Alert: This reversal is due to a cancellation of the claim by the provider.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N694</td><td class="description">Alert: This reversal is due to a resubmission/change to the claim by the provider.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N695</td><td class="description">Alert: This reversal is due to incorrect patient financial responsibility information on the initial adjudication.<br />Start: 11/01/2013</td></tr>

<tr class="prod_set current"><td class="code">N696</td><td class="description">Alert: This reversal is due to a Coordination of Benefits or Third Party Liability Recovery retroactive adjustment.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N697</td><td class="description">Alert: This reversal is due to a payer's retroactive contract incentive program adjustment.<br />Start: 11/01/2013 | Last Modified: 03/14/2014<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N698</td><td class="description">Alert: This reversal is due to non-payment of the health insurance premiums (Health Insurance Exchange or other) by the end of the premium payment grace period, resulting in loss of coverage.<br />Start: 11/01/2013 | Last Modified: 11/01/2015<br />Notes: To be used with claim/service reversal. (Modified 3/14/2014, 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N699</td><td class="description">Payment adjusted based on the Physician Quality Reporting System (PQRS) Incentive Program.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N700</td><td class="description">Payment adjusted based on the Electronic Health Records (EHR) Incentive Program.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N701</td><td class="description">Payment adjusted based on the Value-based Payment Modifier.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N702</td><td class="description">Decision based on review of previously adjudicated claims or for claims in process for the same/similar type of services.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N703</td><td class="description">This service is incompatible with previously  adjudicated claims or claims in process.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N704</td><td class="description">Alert: You may not appeal this decision but can resubmit this claim/service with corrected information if warranted.<br />Start: 03/01/2014 | Last Modified: 03/14/2014<br />Notes: (Modified 3/14/2014)</td></tr>

<tr class="prod_set current"><td class="code">N705</td><td class="description">Incomplete/invalid documentation.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N706</td><td class="description">Missing documentation.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N707</td><td class="description">Incomplete/invalid orders.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N708</td><td class="description">Missing orders.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N709</td><td class="description">Incomplete/invalid notes.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N710</td><td class="description">Missing notes.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N711</td><td class="description">Incomplete/invalid summary.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N712</td><td class="description">Missing summary.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N713</td><td class="description">Incomplete/invalid report.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N714</td><td class="description">Missing report.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N715</td><td class="description">Incomplete/invalid chart.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N716</td><td class="description">Missing chart.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N717</td><td class="description">Incomplete/Invalid documentation of face-to-face examination.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N718</td><td class="description">Missing documentation of face-to-face examination.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N719</td><td class="description">Penalty applied based on plan requirements not being met.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N720</td><td class="description">Alert: The patient overpaid you. You may need to issue the patient a refund for the difference between the patient's payment and the amount shown as patient responsibility on this notice.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N721</td><td class="description">This service is only covered when performed as part of a clinical trial.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N722</td><td class="description">Patient must use Workers' Compensation Set-Aside (WCSA) funds to pay for the medical service or item.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N723</td><td class="description">Patient must use Liability set-aside (LSA) funds to pay for the medical service or item.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N724</td><td class="description">Patient must use No-Fault set-aside (NFSA) funds to pay for the medical service or item.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N725</td><td class="description">A liability insurer has reported having ongoing responsibility for medical services (ORM) for this diagnosis.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N726</td><td class="description">A conditional payment is not allowed.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N727</td><td class="description">A no-fault insurer has reported having ongoing responsibility for medical services (ORM) for this diagnosis.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N728</td><td class="description">A workers' compensation insurer has reported having ongoing responsibility for medical services (ORM) for this diagnosis.<br />Start: 03/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N729</td><td class="description">Missing patient medical/dental record for this service.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N730</td><td class="description">Incomplete/invalid patient medical/dental record for this service.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N731</td><td class="description">Incomplete/Invalid mental health assessment.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N732</td><td class="description">Services performed at an unlicensed facility are not reimbursable.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N733</td><td class="description">Regulatory surcharges are paid directly to the state.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set current"><td class="code">N734</td><td class="description">The patient is eligible for these medical services only when unable to work or perform normal activities due to an illness or injury.<br />Start: 11/01/2014</td></tr>

<tr class="prod_set deactivated"><td class="code">N735</td><td class="description">Adjustment without review of medical/dental record because the requested records were not received or were not received timely.<br />Start: 03/01/2015 | Stop: 01/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N736</td><td class="description">Incomplete/invalid Sleep Study Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N737</td><td class="description">Missing Sleep Study Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N738</td><td class="description">Incomplete/invalid Vein Study Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N739</td><td class="description">Missing Vein Study Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N740</td><td class="description">The member's Consumer Spending Account does not contain sufficient funds to cover the member's liability for this claim/service.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N741</td><td class="description">This is a site neutral payment.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current tobe"><td class="code">N742</td><td class="description">Alert: This claim was processed based on one or more ICD-9 codes. The transition to ICD-10 is required by October 1, 2015, for health care providers, health plans, and clearinghouses. More information can be found at http://www.cms.gov/Medicare/Coding/ICD10/ProviderResources.html<br />Start: 03/01/2015 | Stop: 11/01/2016 | Last Modified: 11/01/2015<br />Notes: (Modified 11/1/2015)</td></tr>

<tr class="prod_set current"><td class="code">N743</td><td class="description">Adjusted because the services may be related to an employment accident.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N744</td><td class="description">Adjusted because the services may be related to an auto accident.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N745</td><td class="description">Missing Ambulance Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N746</td><td class="description">Incomplete/invalid Ambulance Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N747</td><td class="description">This is a misdirected claim/service. Submit the claim to the payer/plan where the patient resides.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N748</td><td class="description">Adjusted because the related hospital charges have not been received.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N749</td><td class="description">Missing Blood Gas Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N750</td><td class="description">Incomplete/invalid Blood Gas Report.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N751</td><td class="description">Adjusted because the drug is covered under a Medicare Part D plan.<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N752</td><td class="description">Missing/incomplete/invalid HIPPS Treatment Authorization Code (TAC).<br />Start: 03/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N753</td><td class="description">Missing/incomplete/invalid Attachment Control Number.<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N754</td><td class="description">Missing/incomplete/invalid Referring Provider or Other Source Qualifier on the 1500 Claim Form.<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N755</td><td class="description">Missing/incomplete/invalid ICD Indicator.<br />Start: 07/01/2015 | Last Modified: 03/01/2016<br />Notes: (Modified 3/1/2016)</td></tr>

<tr class="prod_set current"><td class="code">N756</td><td class="description">Missing/incomplete/invalid point of drop-off address.<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N757</td><td class="description">Adjusted based on the Federal Indian Fees schedule (MLR).<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N758</td><td class="description">Adjusted based on the prior authorization decision.<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N759</td><td class="description">Payment adjusted based on the National Electrical Manufacturers Association (NEMA) Standard XR-29-2013.<br />Start: 07/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N760</td><td class="description">This facility is not authorized to receive payment for the service(s).<br />Start: 11/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N761</td><td class="description">This provider is not authorized to receive payment for the service(s).<br />Start: 11/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N762</td><td class="description">This facility is not certified for Tomosynthesis (3-D) mammography.<br />Start: 11/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N763</td><td class="description">The demonstration code is not appropriate for this claim; resubmit without a demonstration code.<br />Start: 11/01/2015</td></tr>

<tr class="prod_set current"><td class="code">N764</td><td class="description">Missing/incomplete/invalid Hematocrit (HCT) value.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N765</td><td class="description">This payer does not cover co-insurance assessed by a previous payer.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N766</td><td class="description">This payer does not cover co-payment assessed by a previous payer.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N767</td><td class="description">The Medicaid state requires provider to be enrolled in the member's Medicaid state program prior to any claim benefits being processed.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N768</td><td class="description">Incomplete/invalid initial evaluation report.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N769</td><td class="description">A lateral diagnosis is required.<br />Start: 03/01/2016</td></tr>

<tr class="prod_set current"><td class="code">N770</td><td class="description">The adjustment request received from the provider has been processed. Your original claim has been adjusted based on the information received.<br />Start: 03/01/2016</td></tr>

</remarks>
"""
