# downloaded on Mar 7, 2016
# http://www.wpc-edi.com/reference/codelists/healthcare/claim-adjustment-reason-codes/
CLAIM_ADJUSTMENT_REASON_CODES_RAW = """
<claim_adjustment_reason_codes>
<tr class="prod_set current"><td class="code">1</td><td class="description">Deductible Amount<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">2</td><td class="description">Coinsurance Amount<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">3</td><td class="description">Co-payment Amount<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">4</td><td class="description">The procedure code is inconsistent with the modifier used or a required modifier is missing. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">5</td><td class="description">The procedure code/bill type is inconsistent with the place of service. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">6</td><td class="description">The procedure/revenue code is inconsistent with the patient's age. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">7</td><td class="description">The procedure/revenue code is inconsistent with the patient's gender. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">8</td><td class="description">The procedure code is inconsistent with the provider type/specialty (taxonomy). Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">9</td><td class="description">The diagnosis is inconsistent with the patient's age. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">10</td><td class="description">The diagnosis is inconsistent with the patient's gender. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">11</td><td class="description">The diagnosis is inconsistent with the procedure. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">12</td><td class="description">The diagnosis is inconsistent with the provider type. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">13</td><td class="description">The date of death precedes the date of service.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">14</td><td class="description">The date of birth follows the date of service.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">15</td><td class="description">The authorization number is missing, invalid, or does not apply to the billed services or provider.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">16</td><td class="description">Claim/service lacks information or has submission/billing error(s) which is needed for adjudication. Do not use this code for claims attachment(s)/other documentation. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.) Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 11/01/2013</span></td></tr>

<tr class="prod_set deactivated"><td class="code">17</td><td class="description">Requested information was not provided or was insufficient/incomplete. At least one Remark Code must be provided (may be comprised of either the Remittance Advice Remark Code or NCPDP Reject Reason Code.)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/21/2008 | Stop: 07/01/2009</span></td></tr>

<tr class="prod_set current"><td class="code">18</td><td class="description">Exact duplicate claim/service (Use only with Group Code OA except where state workers' compensation regulations requires CO)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/02/2013</span></td></tr>

<tr class="prod_set current"><td class="code">19</td><td class="description">This is a work-related injury/illness and thus the liability of the Worker's Compensation Carrier.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">20</td><td class="description">This injury/illness is covered by the liability carrier.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">21</td><td class="description">This injury/illness is the liability of the no-fault carrier.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">22</td><td class="description">This care may be covered by another payer per coordination of benefits.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">23</td><td class="description">The impact of prior payer(s) adjudication including payments and/or adjustments. (Use only with Group Code OA)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2012</span></td></tr>

<tr class="prod_set current"><td class="code">24</td><td class="description">Charges are covered under a capitation agreement/managed care plan.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">25</td><td class="description">Payment denied. Your Stop loss deductible has not been met.<span class="dates"><br />Start: 01/01/1995 | Stop: 04/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">26</td><td class="description">Expenses incurred prior to coverage.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">27</td><td class="description">Expenses incurred after coverage terminated.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">28</td><td class="description">Coverage not in effect at the time the service was provided.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Redundant to codes 26 and 27.</i></span></td></tr>

<tr class="prod_set current"><td class="code">29</td><td class="description">The time limit for filing has expired.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">30</td><td class="description">Payment adjusted because the patient has not met the required eligibility, spend down, waiting, or residency requirements.<span class="dates"><br />Start: 01/01/1995 | Stop: 02/01/2006</span></td></tr>

<tr class="prod_set current"><td class="code">31</td><td class="description">Patient cannot be identified as our insured.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">32</td><td class="description">Our records indicate that this dependent is not an eligible dependent as defined.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">33</td><td class="description">Insured has no dependent coverage.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">34</td><td class="description">Insured has no coverage for newborns.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">35</td><td class="description">Lifetime benefit maximum has been reached.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 10/31/2002</span></td></tr>

<tr class="prod_set deactivated"><td class="code">36</td><td class="description">Balance does not exceed co-payment amount.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">37</td><td class="description">Balance does not exceed deductible.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">38</td><td class="description">Services not provided or authorized by designated (network/primary care) providers.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/02/2013 | Stop: 01/01/2013<br /><i>Notes: CARC codes 242 and 243 are replacements for this deactivated code</i></span></td></tr>

<tr class="prod_set current"><td class="code">39</td><td class="description">Services denied at the time authorization/pre-certification was requested.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">40</td><td class="description">Charges do not meet qualifications for emergent/urgent care. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">41</td><td class="description">Discount agreed to in Preferred Provider contract.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">42</td><td class="description">Charges exceed our fee schedule or maximum allowable amount. (Use CARC 45)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 10/31/2006 | Stop: 06/01/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">43</td><td class="description">Gramm-Rudman reduction.<span class="dates"><br />Start: 01/01/1995 | Stop: 07/01/2006</span></td></tr>

<tr class="prod_set current"><td class="code">44</td><td class="description">Prompt-pay discount.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">45</td><td class="description">Charge exceeds fee schedule/maximum allowable or contracted/legislated fee arrangement. Note: This adjustment amount cannot equal the total service or claim charge amount; and must not duplicate provider adjustment amounts (payments and contractual reductions) that have resulted from prior payer(s) adjudication. (Use only with Group Codes PR or CO depending upon liability)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 11/01/2015</span></td></tr>

<tr class="prod_set deactivated"><td class="code">46</td><td class="description">This (these) service(s) is (are) not covered.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 96.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">47</td><td class="description">This (these) diagnosis(es) is (are) not covered, missing, or are invalid.<span class="dates"><br />Start: 01/01/1995 | Stop: 02/01/2006</span></td></tr>

<tr class="prod_set deactivated"><td class="code">48</td><td class="description">This (these) procedure(s) is (are) not covered.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 96.</i></span></td></tr>

<tr class="prod_set current"><td class="code">49</td><td class="description">This is a non-covered service because it is a routine/preventive exam or a diagnostic/screening procedure done in conjunction with a routine/preventive exam. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 11/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">50</td><td class="description">These are non-covered services because this is not deemed a 'medical necessity' by the payer. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">51</td><td class="description">These are non-covered services because this is a pre-existing condition. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">52</td><td class="description">The referring/prescribing/rendering provider is not eligible to refer/prescribe/order/perform the service billed.<span class="dates"><br />Start: 01/01/1995 | Stop: 02/01/2006</span></td></tr>

<tr class="prod_set current"><td class="code">53</td><td class="description">Services by an immediate relative or a member of the same household are not covered.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">54</td><td class="description">Multiple physicians/assistants are not covered in this case. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">55</td><td class="description">Procedure/treatment/drug is deemed experimental/investigational by the payer. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 04/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">56</td><td class="description">Procedure/treatment has not been deemed 'proven to be effective' by the payer. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">57</td><td class="description">Payment denied/reduced because the payer deems the information submitted does not support this level of service, this many services, this length of service, this dosage, or this day's supply.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Split into codes 150, 151, 152, 153 and 154.</i></span></td></tr>

<tr class="prod_set current"><td class="code">58</td><td class="description">Treatment was deemed by the payer to have been rendered in an inappropriate or invalid place of service. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">59</td><td class="description">Processed based on multiple or concurrent procedure rules. (For example multiple surgery or diagnostic imaging, concurrent anesthesia.) Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">60</td><td class="description">Charges for outpatient services are not covered when performed within a period of time prior to or after inpatient services.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">61</td><td class="description">Penalty for failure to obtain second surgical opinion. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">62</td><td class="description">Payment denied/reduced for absence of, or exceeded, pre-certification/authorization.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 10/31/2006 | Stop: 04/01/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">63</td><td class="description">Correction to a prior claim.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">64</td><td class="description">Denial reversed per Medical Review.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">65</td><td class="description">Procedure code was incorrect. This payment reflects the correct code.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">66</td><td class="description">Blood Deductible.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">67</td><td class="description">Lifetime reserve days. (Handled in QTY, QTY01=LA)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">68</td><td class="description">DRG weight. (Handled in CLP12)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">69</td><td class="description">Day outlier amount.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">70</td><td class="description">Cost outlier - Adjustment to compensate for additional costs.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/30/2001</span></td></tr>

<tr class="prod_set deactivated"><td class="code">71</td><td class="description">Primary Payer amount.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2000<br /><i>Notes: Use code 23.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">72</td><td class="description">Coinsurance day. (Handled in QTY, QTY01=CD)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">73</td><td class="description">Administrative days.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">74</td><td class="description">Indirect Medical Education Adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">75</td><td class="description">Direct Medical Education Adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">76</td><td class="description">Disproportionate Share Adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">77</td><td class="description">Covered days. (Handled in QTY, QTY01=CA)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">78</td><td class="description">Non-Covered days/Room charge adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">79</td><td class="description">Cost Report days. (Handled in MIA15)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">80</td><td class="description">Outlier days. (Handled in QTY, QTY01=OU)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">81</td><td class="description">Discharges.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">82</td><td class="description">PIP days.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">83</td><td class="description">Total visits.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">84</td><td class="description">Capital Adjustment. (Handled in MIA)<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">85</td><td class="description">Patient Interest Adjustment (Use Only Group code PR)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 07/09/2007<br /><i>Notes: Only use when the payment of interest is the responsibility of the patient.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">86</td><td class="description">Statutory Adjustment.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Duplicative of code 45.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">87</td><td class="description">Transfer amount.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009 | Stop: 01/01/2012</span></td></tr>

<tr class="prod_set deactivated"><td class="code">88</td><td class="description">Adjustment amount represents collection against receivable created in prior overpayment.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">89</td><td class="description">Professional fees removed from charges.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">90</td><td class="description">Ingredient cost adjustment. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 07/01/2009</span></td></tr>

<tr class="prod_set current"><td class="code">91</td><td class="description">Dispensing fee adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">92</td><td class="description">Claim Paid in full.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">93</td><td class="description">No Claim level Adjustments.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: As of 004010, CAS at the claim level is optional.</i></span></td></tr>

<tr class="prod_set current"><td class="code">94</td><td class="description">Processed in Excess of charges.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">95</td><td class="description">Plan procedures not followed.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">96</td><td class="description">Non-covered charge(s). At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.) Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">97</td><td class="description">The benefit for this service is included in the payment/allowance for another service/procedure that has already been adjudicated. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">98</td><td class="description">The hospital must file the Medicare claim for this inpatient non-physician service.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">99</td><td class="description">Medicare Secondary Payer Adjustment Amount.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">100</td><td class="description">Payment made to patient/insured/responsible party/employer.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 01/27/2008</span></td></tr>

<tr class="prod_set current"><td class="code">101</td><td class="description">Predetermination: anticipated payment upon completion of services or claim adjudication.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 02/28/1999</span></td></tr>

<tr class="prod_set current"><td class="code">102</td><td class="description">Major Medical Adjustment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">103</td><td class="description">Provider promotional discount (e.g., Senior citizen discount).<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/30/2001</span></td></tr>

<tr class="prod_set current"><td class="code">104</td><td class="description">Managed care withholding.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">105</td><td class="description">Tax withholding.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">106</td><td class="description">Patient payment option/election not in effect.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">107</td><td class="description">The related or qualifying claim/service was not identified on this claim. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">108</td><td class="description">Rent/purchase guidelines were not met. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">109</td><td class="description">Claim/service not covered by this payer/contractor. You must send the claim/service to the correct payer/contractor.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 01/29/2012</span></td></tr>

<tr class="prod_set current"><td class="code">110</td><td class="description">Billing date predates service date.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">111</td><td class="description">Not covered unless the provider accepts assignment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">112</td><td class="description">Service not furnished directly to the patient and/or not documented.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">113</td><td class="description">Payment denied because service/procedure was provided outside the United States or as a result of war.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 02/28/2001 | Stop: 06/30/2007<br /><i>Notes: Use Codes 157, 158 or 159.</i></span></td></tr>

<tr class="prod_set current"><td class="code">114</td><td class="description">Procedure/product not approved by the Food and Drug Administration.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">115</td><td class="description">Procedure postponed, canceled, or delayed.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">116</td><td class="description">The advance indemnification notice signed by the patient did not comply with requirements.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">117</td><td class="description">Transportation is only covered to the closest facility that can provide the necessary care.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">118</td><td class="description">ESRD network support adjustment.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">119</td><td class="description">Benefit maximum for this time period or occurrence has been reached.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 02/29/2004</span></td></tr>

<tr class="prod_set deactivated"><td class="code">120</td><td class="description">Patient is covered by a managed care plan.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 24.</i></span></td></tr>

<tr class="prod_set current"><td class="code">121</td><td class="description">Indemnification adjustment - compensation for outstanding member responsibility.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">122</td><td class="description">Psychiatric reduction.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">123</td><td class="description">Payer refund due to overpayment.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Refer to implementation guide for proper handling of reversals.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">124</td><td class="description">Payer refund amount - not our patient.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 06/30/1999 | Stop: 06/30/2007<br /><i>Notes: Refer to implementation guide for proper handling of reversals.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">125</td><td class="description">Submission/billing error(s). At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009 | Stop: 11/01/2013</span></td></tr>

<tr class="prod_set deactivated"><td class="code">126</td><td class="description">Deductible -- Major Medical<span class="dates"><br />Start: 02/28/1997 | Last Modified: 09/30/2007 | Stop: 04/01/2008<br /><i>Notes: Use Group Code PR and code 1.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">127</td><td class="description">Coinsurance -- Major Medical<span class="dates"><br />Start: 02/28/1997 | Last Modified: 09/30/2007 | Stop: 04/01/2008<br /><i>Notes: Use Group Code PR and code 2.</i></span></td></tr>

<tr class="prod_set current"><td class="code">128</td><td class="description">Newborn's services are covered in the mother's Allowance.<span class="dates"><br />Start: 02/28/1997</span></td></tr>

<tr class="prod_set current"><td class="code">129</td><td class="description">Prior processing information appears incorrect. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 02/28/1997 | Last Modified: 01/30/2011</span></td></tr>

<tr class="prod_set current"><td class="code">130</td><td class="description">Claim submission fee.<span class="dates"><br />Start: 02/28/1997 | Last Modified: 06/30/2001</span></td></tr>

<tr class="prod_set current"><td class="code">131</td><td class="description">Claim specific negotiated discount.<span class="dates"><br />Start: 02/28/1997</span></td></tr>

<tr class="prod_set current"><td class="code">132</td><td class="description">Prearranged demonstration project adjustment.<span class="dates"><br />Start: 02/28/1997</span></td></tr>

<tr class="prod_set current"><td class="code">133</td><td class="description">The disposition of this service line is pending further review. (Use only with Group Code OA). Note: Use of this code requires a reversal and correction when the service line is finalized (use only in Loop 2110 CAS segment of the 835 or Loop 2430 of the 837).<span class="dates"><br />Start: 07/01/2014 | Last Modified: 03/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">134</td><td class="description">Technical fees removed from charges.<span class="dates"><br />Start: 10/31/1998</span></td></tr>

<tr class="prod_set current"><td class="code">135</td><td class="description">Interim bills cannot be processed.<span class="dates"><br />Start: 10/31/1998 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">136</td><td class="description">Failure to follow prior payer's coverage rules. (Use only with Group Code OA)<span class="dates"><br />Start: 10/31/1998 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">137</td><td class="description">Regulatory Surcharges, Assessments, Allowances or Health Related Taxes.<span class="dates"><br />Start: 02/28/1999 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">138</td><td class="description">Appeal procedures not followed or time limits not met.<span class="dates"><br />Start: 06/30/1999 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">139</td><td class="description">Contracted funding agreement - Subscriber is employed by the provider of services.<span class="dates"><br />Start: 06/30/1999</span></td></tr>

<tr class="prod_set current"><td class="code">140</td><td class="description">Patient/Insured health identification number and name do not match.<span class="dates"><br />Start: 06/30/1999</span></td></tr>

<tr class="prod_set deactivated"><td class="code">141</td><td class="description">Claim spans eligible and ineligible periods of coverage.<span class="dates"><br />Start: 06/30/1999 | Last Modified: 09/30/2007 | Stop: 07/01/2012</span></td></tr>

<tr class="prod_set current"><td class="code">142</td><td class="description">Monthly Medicaid patient liability amount.<span class="dates"><br />Start: 06/30/2000 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">143</td><td class="description">Portion of payment deferred.<span class="dates"><br />Start: 02/28/2001</span></td></tr>

<tr class="prod_set current"><td class="code">144</td><td class="description">Incentive adjustment, e.g. preferred product/service.<span class="dates"><br />Start: 06/30/2001</span></td></tr>

<tr class="prod_set deactivated"><td class="code">145</td><td class="description">Premium payment withholding<span class="dates"><br />Start: 06/30/2002 | Last Modified: 09/30/2007 | Stop: 04/01/2008<br /><i>Notes: Use Group Code CO and code 45.</i></span></td></tr>

<tr class="prod_set current"><td class="code">146</td><td class="description">Diagnosis was invalid for the date(s) of service reported.<span class="dates"><br />Start: 06/30/2002 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">147</td><td class="description">Provider contracted/negotiated rate expired or not on file.<span class="dates"><br />Start: 06/30/2002</span></td></tr>

<tr class="prod_set current"><td class="code">148</td><td class="description">Information from another provider was not provided or was insufficient/incomplete. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 06/30/2002 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">149</td><td class="description">Lifetime benefit maximum has been reached for this service/benefit category.<span class="dates"><br />Start: 10/31/2002</span></td></tr>

<tr class="prod_set current"><td class="code">150</td><td class="description">Payer deems the information submitted does not support this level of service.<span class="dates"><br />Start: 10/31/2002 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">151</td><td class="description">Payment adjusted because the payer deems the information submitted does not support this many/frequency of services.<span class="dates"><br />Start: 10/31/2002 | Last Modified: 01/27/2008</span></td></tr>

<tr class="prod_set current"><td class="code">152</td><td class="description">Payer deems the information submitted does not support this length of service. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 10/31/2002 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">153</td><td class="description">Payer deems the information submitted does not support this dosage.<span class="dates"><br />Start: 10/31/2002 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">154</td><td class="description">Payer deems the information submitted does not support this day's supply.<span class="dates"><br />Start: 10/31/2002 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">155</td><td class="description">Patient refused the service/procedure.<span class="dates"><br />Start: 06/30/2003 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">156</td><td class="description">Flexible spending account payments. Note: Use code 187.<span class="dates"><br />Start: 09/30/2003 | Last Modified: 01/25/2009 | Stop: 10/01/2009</span></td></tr>

<tr class="prod_set current"><td class="code">157</td><td class="description">Service/procedure was provided as a result of an act of war.<span class="dates"><br />Start: 09/30/2003 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">158</td><td class="description">Service/procedure was provided outside of the United States.<span class="dates"><br />Start: 09/30/2003 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">159</td><td class="description">Service/procedure was provided as a result of terrorism.<span class="dates"><br />Start: 09/30/2003 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">160</td><td class="description">Injury/illness was the result of an activity that is a benefit exclusion.<span class="dates"><br />Start: 09/30/2003 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">161</td><td class="description">Provider performance bonus<span class="dates"><br />Start: 02/29/2004</span></td></tr>

<tr class="prod_set deactivated"><td class="code">162</td><td class="description">State-mandated Requirement for Property and Casualty, see Claim Payment Remarks Code for specific explanation.<span class="dates"><br />Start: 02/29/2004 | Stop: 07/01/2014<br /><i>Notes: Use code P1</i></span></td></tr>

<tr class="prod_set current"><td class="code">163</td><td class="description">Attachment/other documentation referenced on the claim was not received.<span class="dates"><br />Start: 06/30/2004 | Last Modified: 06/02/2013</span></td></tr>

<tr class="prod_set current"><td class="code">164</td><td class="description">Attachment/other documentation referenced on the claim was not received in a timely fashion.<span class="dates"><br />Start: 06/30/2004 | Last Modified: 06/02/2013</span></td></tr>

<tr class="prod_set current"><td class="code">165</td><td class="description">Referral absent or exceeded.<span class="dates"><br />Start: 10/31/2004 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">166</td><td class="description">These services were submitted after this payers responsibility for processing claims under this plan ended.<span class="dates"><br />Start: 02/28/2005</span></td></tr>

<tr class="prod_set current"><td class="code">167</td><td class="description">This (these) diagnosis(es) is (are) not covered. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">168</td><td class="description">Service(s) have been considered under the patient's medical plan. Benefits are not available under this dental plan.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">169</td><td class="description">Alternate benefit has been provided.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">170</td><td class="description">Payment is denied when performed/billed by this type of provider. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">171</td><td class="description">Payment is denied when performed/billed by this type of provider in this type of facility. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">172</td><td class="description">Payment is adjusted when performed/billed by a provider of this specialty. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">173</td><td class="description">Service/equipment was not prescribed by a physician.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">174</td><td class="description">Service was not prescribed prior to delivery.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">175</td><td class="description">Prescription is incomplete.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">176</td><td class="description">Prescription is not current.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">177</td><td class="description">Patient has not met the required eligibility requirements.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">178</td><td class="description">Patient has not met the required spend down requirements.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">179</td><td class="description">Patient has not met the required waiting requirements. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">180</td><td class="description">Patient has not met the required residency requirements.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">181</td><td class="description">Procedure code was invalid on the date of service.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">182</td><td class="description">Procedure modifier was invalid on the date of service.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">183</td><td class="description">The referring provider is not eligible to refer the service billed. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">184</td><td class="description">The prescribing/ordering provider is not eligible to prescribe/order the service billed. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">185</td><td class="description">The rendering provider is not eligible to perform the service billed. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">186</td><td class="description">Level of care change adjustment.<span class="dates"><br />Start: 06/30/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">187</td><td class="description">Consumer Spending Account payments (includes but is not limited to Flexible Spending Account, Health Savings Account, Health Reimbursement Account, etc.)<span class="dates"><br />Start: 06/30/2005 | Last Modified: 01/25/2009</span></td></tr>

<tr class="prod_set current"><td class="code">188</td><td class="description">This product/procedure is only covered when used according to FDA recommendations.<span class="dates"><br />Start: 06/30/2005</span></td></tr>

<tr class="prod_set current"><td class="code">189</td><td class="description">'Not otherwise classified' or 'unlisted' procedure code (CPT/HCPCS) was billed when there is a specific procedure code for this procedure/service<span class="dates"><br />Start: 06/30/2005</span></td></tr>

<tr class="prod_set current"><td class="code">190</td><td class="description">Payment is included in the allowance for a Skilled Nursing Facility (SNF) qualified stay.<span class="dates"><br />Start: 10/31/2005</span></td></tr>

<tr class="prod_set deactivated"><td class="code">191</td><td class="description">Not a work related injury/illness and thus not the liability of the workers' compensation carrier Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF)<span class="dates"><br />Start: 10/31/2005 | Last Modified: 10/17/2010 | Stop: 07/01/2014<br /><i>Notes: Use code P2</i></span></td></tr>

<tr class="prod_set current"><td class="code">192</td><td class="description">Non standard adjustment code from paper remittance. Note: This code is to be used by providers/payers providing Coordination of Benefits information to another payer in the 837 transaction only. This code is only used when the non-standard code cannot be reasonably mapped to an existing Claims Adjustment Reason Code, specifically Deductible, Coinsurance and Co-payment.<span class="dates"><br />Start: 10/31/2005 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">193</td><td class="description">Original payment decision is being maintained. Upon review, it was determined that this claim was processed properly.<span class="dates"><br />Start: 02/28/2006 | Last Modified: 01/27/2008</span></td></tr>

<tr class="prod_set current"><td class="code">194</td><td class="description">Anesthesia performed by the operating physician, the assistant surgeon or the attending physician.<span class="dates"><br />Start: 02/28/2006 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">195</td><td class="description">Refund issued to an erroneous priority payer for this claim/service.<span class="dates"><br />Start: 02/28/2006 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">196</td><td class="description">Claim/service denied based on prior payer's coverage determination.<span class="dates"><br />Start: 06/30/2006 | Stop: 02/01/2007<br /><i>Notes: Use code 136.</i></span></td></tr>

<tr class="prod_set current"><td class="code">197</td><td class="description">Precertification/authorization/notification absent.<span class="dates"><br />Start: 10/31/2006 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">198</td><td class="description">Precertification/authorization exceeded.<span class="dates"><br />Start: 10/31/2006 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">199</td><td class="description">Revenue code and Procedure code do not match.<span class="dates"><br />Start: 10/31/2006</span></td></tr>

<tr class="prod_set current"><td class="code">200</td><td class="description">Expenses incurred during lapse in coverage<span class="dates"><br />Start: 10/31/2006</span></td></tr>

<tr class="prod_set current"><td class="code">201</td><td class="description">Patient is responsible for amount of this claim/service through 'set aside arrangement' or other agreement. (Use only with Group Code PR)  At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 10/31/2006 | Last Modified: 09/28/2014<br /><i>Notes: Not for use by Workers' Compensation payers; use code P3 instead.</i></span></td></tr>

<tr class="prod_set current"><td class="code">202</td><td class="description">Non-covered personal comfort or convenience services.<span class="dates"><br />Start: 02/28/2007 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">203</td><td class="description">Discontinued or reduced service.<span class="dates"><br />Start: 02/28/2007 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">204</td><td class="description">This service/equipment/drug is not covered under the patient's current benefit plan<span class="dates"><br />Start: 02/28/2007</span></td></tr>

<tr class="prod_set current"><td class="code">205</td><td class="description">Pharmacy discount card processing fee<span class="dates"><br />Start: 07/09/2007</span></td></tr>

<tr class="prod_set current"><td class="code">206</td><td class="description">National Provider Identifier - missing.<span class="dates"><br />Start: 07/09/2007 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">207</td><td class="description">National Provider identifier - Invalid format<span class="dates"><br />Start: 07/09/2007 | Last Modified: 06/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">208</td><td class="description">National Provider Identifier - Not matched.<span class="dates"><br />Start: 07/09/2007 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">209</td><td class="description">Per regulatory or other agreement. The provider cannot collect this amount from the patient. However, this amount may be billed to subsequent payer. Refund to patient if collected. (Use only with Group code OA)<span class="dates"><br />Start: 07/09/2007 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">210</td><td class="description">Payment adjusted because pre-certification/authorization not received in a timely fashion<span class="dates"><br />Start: 07/09/2007</span></td></tr>

<tr class="prod_set current"><td class="code">211</td><td class="description">National Drug Codes (NDC) not eligible for rebate, are not covered.<span class="dates"><br />Start: 07/09/2007</span></td></tr>

<tr class="prod_set current"><td class="code">212</td><td class="description">Administrative surcharges are not covered<span class="dates"><br />Start: 11/05/2007</span></td></tr>

<tr class="prod_set current"><td class="code">213</td><td class="description">Non-compliance with the physician self referral prohibition legislation or payer policy.<span class="dates"><br />Start: 01/27/2008</span></td></tr>

<tr class="prod_set deactivated"><td class="code">214</td><td class="description">Workers' Compensation claim adjudicated as non-compensable. This Payer not liable for claim or service/treatment. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Workers' Compensation only<span class="dates"><br />Start: 01/27/2008 | Last Modified: 10/17/2010 | Stop: 07/01/2014<br /><i>Notes: Use code P4</i></span></td></tr>

<tr class="prod_set current"><td class="code">215</td><td class="description">Based on subrogation of a third party settlement<span class="dates"><br />Start: 01/27/2008</span></td></tr>

<tr class="prod_set current"><td class="code">216</td><td class="description">Based on the findings of a review organization<span class="dates"><br />Start: 01/27/2008</span></td></tr>

<tr class="prod_set deactivated"><td class="code">217</td><td class="description">Based on payer reasonable and customary fees. No maximum allowable defined by legislated fee arrangement. (Note: To be used for Property and Casualty only)<span class="dates"><br />Start: 01/27/2008 | Last Modified: 09/30/2012 | Stop: 07/01/2014<br /><i>Notes: Use code P5</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">218</td><td class="description">Based on entitlement to benefits. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Workers' Compensation only<span class="dates"><br />Start: 01/27/2008 | Last Modified: 10/17/2010 | Stop: 07/01/2014<br /><i>Notes: Use code P6</i></span></td></tr>

<tr class="prod_set current"><td class="code">219</td><td class="description">Based on extent of injury. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF).<span class="dates"><br />Start: 01/27/2008 | Last Modified: 10/17/2010</span></td></tr>

<tr class="prod_set deactivated"><td class="code">220</td><td class="description">The applicable fee schedule/fee database does not contain the billed code. Please resubmit a bill with the appropriate fee schedule/fee database code(s) that best describe the service(s) provided and supporting documentation if required. (Note: To be used for Property and Casualty only)<span class="dates"><br />Start: 01/27/2008 | Last Modified: 09/30/2012 | Stop: 07/01/2014<br /><i>Notes: Use code P7</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">221</td><td class="description">Claim is under investigation. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). (Note: To be used by Property  and  Casualty only)<span class="dates"><br />Start: 01/27/2008 | Last Modified: 07/01/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P8</i></span></td></tr>

<tr class="prod_set current"><td class="code">222</td><td class="description">Exceeds the contracted maximum number of hours/days/units by this provider for this period. This is not patient specific. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 06/01/2008 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">223</td><td class="description">Adjustment code for mandated federal, state or local law/regulation that is not already covered by another code and is mandated before a new code can be created.<span class="dates"><br />Start: 06/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">224</td><td class="description">Patient identification compromised by identity theft. Identity verification required for processing this and future claims.<span class="dates"><br />Start: 06/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">225</td><td class="description">Penalty or Interest Payment by Payer (Only used for plan to plan encounter reporting within the 837)<span class="dates"><br />Start: 06/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">226</td><td class="description">Information requested from the Billing/Rendering Provider was not provided or not provided timely or was insufficient/incomplete. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 09/21/2008 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">227</td><td class="description">Information requested from the patient/insured/responsible party was not provided or was insufficient/incomplete. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 09/21/2008 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">228</td><td class="description">Denied for failure of this provider, another provider or the subscriber to supply requested information to a previous payer for their adjudication<span class="dates"><br />Start: 09/21/2008</span></td></tr>

<tr class="prod_set current"><td class="code">229</td><td class="description">Partial charge amount not considered by Medicare due to the initial claim Type of Bill being 12X. Note: This code can only be used in the 837 transaction to convey Coordination of Benefits information when the secondary payer's cost avoidance policy allows providers to bypass claim submission to a prior payer. (Use only with Group Code PR)<span class="dates"><br />Start: 01/25/2009 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set deactivated"><td class="code">230</td><td class="description">No available or correlating CPT/HCPCS code to describe this service. Note: Used only by Property and Casualty.<span class="dates"><br />Start: 01/25/2009 | Stop: 07/01/2014<br /><i>Notes: Use code P9</i></span></td></tr>

<tr class="prod_set current"><td class="code">231</td><td class="description">Mutually exclusive procedures cannot be done in the same day/setting. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 07/01/2009 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">232</td><td class="description">Institutional Transfer Amount. Note - Applies to institutional claims only and explains the DRG amount difference when the patient care crosses multiple institutions.<span class="dates"><br />Start: 11/01/2009</span></td></tr>

<tr class="prod_set current"><td class="code">233</td><td class="description">Services/charges related to the treatment of a hospital-acquired condition or preventable medical error.<span class="dates"><br />Start: 01/24/2010</span></td></tr>

<tr class="prod_set current"><td class="code">234</td><td class="description">This procedure is not paid separately. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 01/24/2010</span></td></tr>

<tr class="prod_set current"><td class="code">235</td><td class="description">Sales Tax<span class="dates"><br />Start: 06/06/2010</span></td></tr>

<tr class="prod_set current"><td class="code">236</td><td class="description">This procedure or procedure/modifier combination is not compatible with another procedure or procedure/modifier combination provided on the same day according to the National Correct Coding Initiative or workers compensation state regulations/ fee schedule requirements.<span class="dates"><br />Start: 01/30/2011 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">237</td><td class="description">Legislated/Regulatory Penalty. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 06/05/2011</span></td></tr>

<tr class="prod_set current"><td class="code">238</td><td class="description">Claim spans eligible and ineligible periods of coverage, this is the reduction for the ineligible period. (Use only with Group Code PR)<span class="dates"><br />Start: 03/01/2012 | Last Modified: 07/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">239</td><td class="description">Claim spans eligible and ineligible periods of coverage. Rebill separate claims.<span class="dates"><br />Start: 03/01/2012 | Last Modified: 01/29/2012</span></td></tr>

<tr class="prod_set current"><td class="code">240</td><td class="description">The diagnosis is inconsistent with the patient's birth weight. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 06/03/2012</span></td></tr>

<tr class="prod_set current"><td class="code">241</td><td class="description">Low Income Subsidy (LIS) Co-payment Amount<span class="dates"><br />Start: 06/03/2012</span></td></tr>

<tr class="prod_set current"><td class="code">242</td><td class="description">Services not provided by network/primary care providers.<span class="dates"><br />Start: 06/03/2012 | Last Modified: 06/02/2013<br /><i>Notes: This code replaces deactivated code 38</i></span></td></tr>

<tr class="prod_set current"><td class="code">243</td><td class="description">Services not authorized by network/primary care providers.<span class="dates"><br />Start: 06/03/2012 | Last Modified: 06/02/2013<br /><i>Notes: This code replaces deactivated code 38</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">244</td><td class="description">Payment reduced to zero due to litigation. Additional information will be sent following the conclusion of litigation. To be used for Property  and  Casualty only.<span class="dates"><br />Start: 09/30/2012 | Stop: 07/01/2014<br /><i>Notes: Use code P10</i></span></td></tr>

<tr class="prod_set current"><td class="code">245</td><td class="description">Provider performance program withhold.<span class="dates"><br />Start: 09/30/2012</span></td></tr>

<tr class="prod_set current"><td class="code">246</td><td class="description">This non-payable code is for required reporting only.<span class="dates"><br />Start: 09/30/2012</span></td></tr>

<tr class="prod_set current"><td class="code">247</td><td class="description">Deductible for Professional service rendered in an Institutional setting and billed on an Institutional claim.<span class="dates"><br />Start: 09/30/2012<br /><i>Notes: For Medicare Bundled Payment use only, under the Patient Protection and Affordable Care Act (PPACA).</i></span></td></tr>

<tr class="prod_set current"><td class="code">248</td><td class="description">Coinsurance for Professional service rendered in an Institutional setting and billed on an Institutional claim.<span class="dates"><br />Start: 09/30/2012<br /><i>Notes: For Medicare Bundled Payment use only, under the Patient Protection and Affordable Care Act (PPACA).</i></span></td></tr>

<tr class="prod_set current"><td class="code">249</td><td class="description">This claim has been identified as a readmission. (Use only with Group Code CO)<span class="dates"><br />Start: 09/30/2012</span></td></tr>

<tr class="prod_set current"><td class="code">250</td><td class="description">The attachment/other documentation that was received was the incorrect attachment/document. The expected attachment/document is still missing. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT).<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">251</td><td class="description">The attachment/other documentation that was received was incomplete or deficient. The necessary information is still needed to process the claim. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT).<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">252</td><td class="description">An attachment/other documentation is required to adjudicate this claim/service. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT).<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/02/2013</span></td></tr>

<tr class="prod_set current"><td class="code">253</td><td class="description">Sequestration - reduction in federal payment<span class="dates"><br />Start: 06/02/2013 | Last Modified: 11/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">254</td><td class="description">Claim received by the dental plan, but benefits not available under this plan.  Submit these services to the patient's medical plan for further consideration.<span class="dates"><br />Start: 06/02/2013</span></td></tr>

<tr class="prod_set deactivated"><td class="code">255</td><td class="description">The disposition of the related Property  and  Casualty claim (injury or illness) is pending due to litigation. (Use only with Group Code OA)<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P11</i></span></td></tr>

<tr class="prod_set current"><td class="code">256</td><td class="description">Service not payable per managed care contract.<span class="dates"><br />Start: 06/02/2013</span></td></tr>

<tr class="prod_set current"><td class="code">257</td><td class="description">The disposition of the claim/service is undetermined during the premium payment grace period, per Health Insurance Exchange requirements. This claim/service will be reversed and corrected when the grace period ends (due to premium payment or lack of premium payment). (Use only with Group Code OA)<span class="dates"><br />Start: 11/01/2013 | Last Modified: 06/01/2014<br /><i>Notes: To be used after the first month of the grace period.</i></span></td></tr>

<tr class="prod_set current"><td class="code">258</td><td class="description">Claim/service not covered when patient is in custody/incarcerated. Applicable federal, state or local authority may cover the claim/service.<span class="dates"><br />Start: 11/01/2013</span></td></tr>

<tr class="prod_set current"><td class="code">259</td><td class="description">Additional payment for Dental/Vision service utilization.<span class="dates"><br />Start: 01/26/2014</span></td></tr>

<tr class="prod_set current"><td class="code">260</td><td class="description">Processed under Medicaid ACA Enhanced Fee Schedule<span class="dates"><br />Start: 01/26/2014</span></td></tr>

<tr class="prod_set current"><td class="code">261</td><td class="description">The procedure or service is inconsistent with the patient's history.<span class="dates"><br />Start: 06/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">262</td><td class="description">Adjustment for delivery cost. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">263</td><td class="description">Adjustment for shipping cost. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">264</td><td class="description">Adjustment for postage cost. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">265</td><td class="description">Adjustment for administrative cost. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">266</td><td class="description">Adjustment for compound preparation cost. Note: To be used for pharmaceuticals only.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">267</td><td class="description">Claim/service spans multiple months. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 11/01/2014 | Last Modified: 04/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">268</td><td class="description">The Claim spans two calendar years. Please resubmit one claim per calendar year.<span class="dates"><br />Start: 11/01/2014</span></td></tr>

<tr class="prod_set current"><td class="code">269</td><td class="description">Anesthesia not covered for this service/procedure. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present.<span class="dates"><br />Start: 03/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">270</td><td class="description">Claim received by the medical plan, but benefits not available under this plan. Submit these services to the patient's dental plan for further consideration.<span class="dates"><br />Start: 07/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">271</td><td class="description">Prior contractual reductions related to a current periodic payment as part of a contractual payment schedule when deferred amounts have been previously reported. (Use only with group code OA)<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">272</td><td class="description">Coverage/program guidelines were not met.<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">273</td><td class="description">Coverage/program guidelines were exceeded.<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">274</td><td class="description">Fee/Service not payable per patient Care Coordination arrangement.<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">275</td><td class="description">Prior payer's (or payers') patient responsibility (deductible, coinsurance, co-payment) not covered. (Use only with Group Code PR)<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">276</td><td class="description">Services denied by the prior payer(s) are not covered by this payer.<span class="dates"><br />Start: 11/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">277</td><td class="description">The disposition of the claim/service is undetermined during the premium payment grace period, per Health Insurance SHOP Exchange requirements. This claim/service will be reversed and corrected when the grace period ends (due to premium payment or lack of premium payment). (Use only with Group Code OA)<span class="dates"><br />Start: 11/01/2015<br /><i>Notes: To be used during 31 day SHOP grace period.</i></span></td></tr>

<tr class="prod_set current"><td class="code">A0</td><td class="description">Patient refund amount.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">A1</td><td class="description">Claim/Service denied. At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">A2</td><td class="description">Contractual adjustment.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 02/28/2007 | Stop: 01/01/2008<br /><i>Notes: Use Code 45 with Group Code 'CO' or use another appropriate specific adjustment code.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">A3</td><td class="description">Medicare Secondary Payer liability met.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">A4</td><td class="description">Medicare Claim PPS Capital Day Outlier Amount.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007 | Stop: 04/01/2008</span></td></tr>

<tr class="prod_set current"><td class="code">A5</td><td class="description">Medicare Claim PPS Capital Cost Outlier Amount.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">A6</td><td class="description">Prior hospitalization or 30 day transfer requirement not met.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">A7</td><td class="description">Presumptive Payment Adjustment<span class="dates"><br />Start: 01/01/1995 | Stop: 07/01/2015</span></td></tr>

<tr class="prod_set current"><td class="code">A8</td><td class="description">Ungroupable DRG.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">B1</td><td class="description">Non-covered visits.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B2</td><td class="description">Covered visits.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B3</td><td class="description">Covered charges.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">B4</td><td class="description">Late filing penalty.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current tobe"><td class="code">B5</td><td class="description">Coverage/program guidelines were not met or were exceeded.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 11/01/2015 | Stop: 05/01/2016<br /><i>Notes: This code has been replaced by 272 and 273.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">B6</td><td class="description">This payment is adjusted when performed/billed by this type of provider, by this type of provider in this type of facility, or by a provider of this specialty.<span class="dates"><br />Start: 01/01/1995 | Stop: 02/01/2006</span></td></tr>

<tr class="prod_set current"><td class="code">B7</td><td class="description">This provider was not certified/eligible to be paid for this procedure/service on this date of service. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">B8</td><td class="description">Alternative services were available, and should have been utilized. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">B9</td><td class="description">Patient is enrolled in a Hospice.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">B10</td><td class="description">Allowed amount has been reduced because a component of the basic procedure/test was paid. The beneficiary is not liable for more than the charge limit for the basic procedure/test.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">B11</td><td class="description">The claim/service has been transferred to the proper payer/processor for processing. Claim/service not covered by this payer/processor.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">B12</td><td class="description">Services not documented in patients' medical records.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">B13</td><td class="description">Previously paid. Payment for this claim/service may have been provided in a previous payment.<span class="dates"><br />Start: 01/01/1995</span></td></tr>

<tr class="prod_set current"><td class="code">B14</td><td class="description">Only one visit or consultation per physician per day is covered.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set current"><td class="code">B15</td><td class="description">This service/procedure requires that a qualifying service/procedure be received and covered. The qualifying other service/procedure has not been received/adjudicated. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information  REF), if present.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/20/2009</span></td></tr>

<tr class="prod_set current"><td class="code">B16</td><td class="description">'New Patient' qualifications were not met.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B17</td><td class="description">Payment adjusted because this service was not prescribed by a physician, not prescribed prior to delivery, the prescription is incomplete, or the prescription is not current.<span class="dates"><br />Start: 01/01/1995 | Stop: 02/01/2006</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B18</td><td class="description">This procedure code and modifier were invalid on the date of service.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/21/2008 | Stop: 03/01/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B19</td><td class="description">Claim/service adjusted because of the finding of a Review Organization.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">B20</td><td class="description">Procedure/service was partially or fully furnished by another provider.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">B21</td><td class="description">The charges were reduced because the service/care was partially furnished by another physician.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003</span></td></tr>

<tr class="prod_set current"><td class="code">B22</td><td class="description">This payment is adjusted based on the diagnosis.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 02/28/2001</span></td></tr>

<tr class="prod_set current"><td class="code">B23</td><td class="description">Procedure billed is not authorized per your Clinical Laboratory Improvement Amendment (CLIA) proficiency test.<span class="dates"><br />Start: 01/01/1995 | Last Modified: 09/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">D1</td><td class="description">Claim/service denied. Level of subluxation is missing or inadequate.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D2</td><td class="description">Claim lacks the name, strength, or dosage of the drug furnished.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D3</td><td class="description">Claim/service denied because information to indicate if the patient owns the equipment that requires the part or supply was missing.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D4</td><td class="description">Claim/service does not indicate the period of time for which this will be needed.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D5</td><td class="description">Claim/service denied. Claim lacks individual lab codes included in the test.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D6</td><td class="description">Claim/service denied. Claim did not include patient's medical record for the service.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D7</td><td class="description">Claim/service denied. Claim lacks date of patient's most recent physician visit.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D8</td><td class="description">Claim/service denied. Claim lacks indicator that 'x-ray is available for review.'<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D9</td><td class="description">Claim/service denied. Claim lacks invoice or statement certifying the actual cost of the lens, less discounts or the type of intraocular lens used.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 16 and remark codes if necessary.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D10</td><td class="description">Claim/service denied. Completed physician financial relationship form not on file.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D11</td><td class="description">Claim lacks completed pacemaker registration form.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D12</td><td class="description">Claim/service denied. Claim does not identify who performed the purchased diagnostic test or the amount you were charged for the test.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D13</td><td class="description">Claim/service denied. Performed by a facility/supplier in which the ordering/referring physician has a financial interest.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D14</td><td class="description">Claim lacks indication that plan of treatment is on file.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D15</td><td class="description">Claim lacks indication that service was supervised or evaluated by a physician.<span class="dates"><br />Start: 01/01/1995 | Stop: 10/16/2003<br /><i>Notes: Use code 17.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D16</td><td class="description">Claim lacks prior payer payment information.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 16 with appropriate claim payment remark code [N4].</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D17</td><td class="description">Claim/Service has invalid non-covered days.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 16 with appropriate claim payment remark code.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D18</td><td class="description">Claim/Service has missing diagnosis information.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 16 with appropriate claim payment remark code.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D19</td><td class="description">Claim/Service lacks Physician/Operative or other supporting documentation<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 16 with appropriate claim payment remark code.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D20</td><td class="description">Claim/Service missing service/product information.<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007<br /><i>Notes: Use code 16 with appropriate claim payment remark code.</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">D21</td><td class="description">This (these) diagnosis(es) is (are) missing or are invalid<span class="dates"><br />Start: 01/01/1995 | Stop: 06/30/2007</span></td></tr>

<tr class="prod_set deactivated"><td class="code">D22</td><td class="description">Reimbursement was adjusted for the reasons to be provided in separate correspondence. (Note: To be used for Workers' Compensation only) - Temporary code to be added for timeframe only until 01/01/2009. Another code to be established and/or for 06/2008 meeting for a revised code to replace or strategy to use another existing code<span class="dates"><br />Start: 01/27/2008 | Stop: 01/01/2009</span></td></tr>

<tr class="prod_set deactivated"><td class="code">D23</td><td class="description">This dual eligible patient is covered by Medicare Part D per Medicare Retro-Eligibility.  At least one Remark Code must be provided (may be comprised of either the NCPDP Reject Reason Code, or Remittance Advice Remark Code that is not an ALERT.)<span class="dates"><br />Start: 11/01/2009 | Stop: 01/01/2012</span></td></tr>

<tr class="prod_set current"><td class="code">P1</td><td class="description">State-mandated Requirement for Property and Casualty, see Claim Payment Remarks Code for specific explanation. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 162</i></span></td></tr>

<tr class="prod_set current"><td class="code">P2</td><td class="description">Not a work related injury/illness and thus not the liability of the workers' compensation carrier Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Workers' Compensation only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 191</i></span></td></tr>

<tr class="prod_set current"><td class="code">P3</td><td class="description">Workers' Compensation case settled. Patient is responsible for amount of this claim/service through WC 'Medicare set aside arrangement' or other agreement. To be used for Workers' Compensation only. (Use only with Group Code PR)<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 201</i></span></td></tr>

<tr class="prod_set current"><td class="code">P4</td><td class="description">Workers' Compensation claim adjudicated as non-compensable. This Payer not liable for claim or service/treatment. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Workers' Compensation only<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 214</i></span></td></tr>

<tr class="prod_set current"><td class="code">P5</td><td class="description">Based on payer reasonable and customary fees. No maximum allowable defined by legislated fee arrangement. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 217</i></span></td></tr>

<tr class="prod_set current"><td class="code">P6</td><td class="description">Based on entitlement to benefits. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 218</i></span></td></tr>

<tr class="prod_set current"><td class="code">P7</td><td class="description">The applicable fee schedule/fee database does not contain the billed code. Please resubmit a bill with the appropriate fee schedule/fee database code(s) that best describe the service(s) provided and supporting documentation if required. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 220</i></span></td></tr>

<tr class="prod_set current"><td class="code">P8</td><td class="description">Claim is under investigation. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') for the jurisdictional regulation. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF). To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 221</i></span></td></tr>

<tr class="prod_set current"><td class="code">P9</td><td class="description">No available or correlating CPT/HCPCS code to describe this service. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 230</i></span></td></tr>

<tr class="prod_set current"><td class="code">P10</td><td class="description">Payment reduced to zero due to litigation. Additional information will be sent following the conclusion of litigation. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 244</i></span></td></tr>

<tr class="prod_set current"><td class="code">P11</td><td class="description">The disposition of the related Property  and  Casualty claim (injury or illness) is pending due to litigation. To be used for Property and Casualty only. (Use only with Group Code OA)<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code 255</i></span></td></tr>

<tr class="prod_set current"><td class="code">P12</td><td class="description">Workers' compensation jurisdictional fee schedule adjustment.  Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Class of Contract Code Identification Segment (Loop 2100 Other Claim Related Information REF). If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Workers' Compensation only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W1</i></span></td></tr>

<tr class="prod_set current"><td class="code">P13</td><td class="description">Payment reduced or denied based on workers' compensation jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Workers' Compensation only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W2</i></span></td></tr>

<tr class="prod_set current"><td class="code">P14</td><td class="description">The Benefit for this Service is included in the payment/allowance for another service/procedure that has been performed on the same day. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W3</i></span></td></tr>

<tr class="prod_set current"><td class="code">P15</td><td class="description">Workers' Compensation Medical Treatment Guideline Adjustment. To be used for Workers' Compensation only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W4</i></span></td></tr>

<tr class="prod_set current"><td class="code">P16</td><td class="description">Medical provider not authorized/certified to provide treatment to injured workers in this jurisdiction. To be used for Workers' Compensation only. (Use with Group Code CO or OA)<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W5</i></span></td></tr>

<tr class="prod_set current"><td class="code">P17</td><td class="description">Referral not authorized by attending physician per regulatory requirement. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W6</i></span></td></tr>

<tr class="prod_set current"><td class="code">P18</td><td class="description">Procedure is not listed in the jurisdiction fee schedule.  An allowance has been made for a comparable service. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W7</i></span></td></tr>

<tr class="prod_set current"><td class="code">P19</td><td class="description">Procedure has a relative value of zero in the jurisdiction fee schedule, therefore no payment is due. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W8</i></span></td></tr>

<tr class="prod_set current"><td class="code">P20</td><td class="description">Service not paid under jurisdiction allowed outpatient facility fee schedule. To be used for Property and Casualty only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code W9</i></span></td></tr>

<tr class="prod_set current"><td class="code">P21</td><td class="description">Payment denied based on Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Property and Casualty Auto only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code Y1</i></span></td></tr>

<tr class="prod_set current"><td class="code">P22</td><td class="description">Payment adjusted based on Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Property and Casualty Auto only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code Y2</i></span></td></tr>

<tr class="prod_set current"><td class="code">P23</td><td class="description">Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional fee schedule adjustment. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Class of Contract Code Identification Segment (Loop 2100 Other Claim Related Information REF). If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Property and Casualty Auto only.<span class="dates"><br />Start: 11/01/2013<br /><i>Notes: This code replaces deactivated code Y3</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W1</td><td class="description">Workers' compensation jurisdictional fee schedule adjustment.  Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Class of Contract Code Identification Segment (Loop 2100 Other Claim Related Information REF). If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply.<span class="dates"><br />Start: 02/29/2000 | Last Modified: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P12</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W2</td><td class="description">Payment reduced or denied based on workers' compensation jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for Workers' Compensation only.<span class="dates"><br />Start: 10/17/2010 | Last Modified: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P13</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W3</td><td class="description">The Benefit for this Service is included in the payment/allowance for another service/procedure that has been performed on the same day. Note: Refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment Information REF), if present. For use by Property and Casualty only.<span class="dates"><br />Start: 09/30/2012 | Stop: 07/01/2014<br /><i>Notes: Use code P14</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W4</td><td class="description">Workers' Compensation Medical Treatment Guideline Adjustment.<span class="dates"><br />Start: 09/30/2012 | Stop: 07/01/2014<br /><i>Notes: Use code P15</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W5</td><td class="description">Medical provider not authorized/certified to provide treatment to injured workers in this jurisdiction. (Use with Group Code CO or OA)<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P16</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W6</td><td class="description">Referral not authorized by attending physician per regulatory requirement.<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P17</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W7</td><td class="description">Procedure is not listed in the jurisdiction fee schedule.  An allowance has been made for a comparable service.<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P18</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W8</td><td class="description">Procedure has a relative value of zero in the jurisdiction fee schedule, therefore no payment is due.<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P19</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">W9</td><td class="description">Service not paid under jurisdiction allowed outpatient facility fee schedule.<span class="dates"><br />Start: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P20</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">Y1</td><td class="description">Payment denied based on Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for P and C Auto only.<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P21</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">Y2</td><td class="description">Payment adjusted based on Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional regulations or payment policies, use only if no other code is applicable. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Insurance Policy Number Segment (Loop 2100 Other Claim Related Information REF qualifier 'IG') if the jurisdictional regulation applies. If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for P and C Auto only.<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P22</i></span></td></tr>

<tr class="prod_set deactivated"><td class="code">Y3</td><td class="description">Medical Payments Coverage (MPC) or Personal Injury Protection (PIP) Benefits jurisdictional fee schedule adjustment. Note: If adjustment is at the Claim Level, the payer must send and the provider should refer to the 835 Class of Contract Code Identification Segment (Loop 2100 Other Claim Related Information REF). If adjustment is at the Line Level, the payer must send and the provider should refer to the 835 Healthcare Policy Identification Segment (loop 2110 Service Payment information REF) if the regulations apply. To be used for P and C Auto only.<span class="dates"><br />Start: 09/30/2012 | Last Modified: 06/02/2013 | Stop: 07/01/2014<br /><i>Notes: Use code P23</i></span></td></tr>
</claim_adjustment_reason_codes>
"""
