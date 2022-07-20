"""Source:

http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-codes/

Date: 3/7/2016
"""

__CODE_MAP = {
"0" : "Cannot provide further status electronically.",
"1" : "For more detailed information, see remittance advice.",
"2" : "More detailed information in letter.",
"3" : "Claim has been adjudicated and is awaiting payment cycle.",
"6" : "Balance due from the subscriber.",
"12" : "One or more originally submitted procedure codes have been combined.",
"15" : "One or more originally submitted procedure code have been modified.",
"16" : "Claim/encounter has been forwarded to entity.",
"17" : "Claim/encounter has been forwarded by third party entity to entity.",
"18" : "Entity received claim/encounter, but returned invalid status.",
"19" : "Entity acknowledges receipt of claim/encounter.",
"20" : "Accepted for processing.",
"21" : "Missing or invalid information.",
"23" : "Returned to Entity.",
"24" : "Entity not approved as an electronic submitter.",
"25" : "Entity not approved.",
"26" : "Entity not found.",
"27" : "Policy canceled.",
"29" : "Subscriber and policy number/contract number mismatched.",
"30" : "Subscriber and subscriber id mismatched.",
"31" : "Subscriber and policyholder name mismatched.",
"32" : "Subscriber and policy number/contract number not found.",
"33" : "Subscriber and subscriber id not found.",
"34" : "Subscriber and policyholder name not found.",
"35" : "Claim/encounter not found.",
"37" : "Predetermination is on file, awaiting completion of services.",
"38" : "Awaiting next periodic adjudication cycle.",
"39" : "Charges for pregnancy deferred until delivery.",
"40" : "Waiting for final approval.",
"41" : "Special handling required at payer site.",
"42" : "Awaiting related charges.",
"44" : "Charges pending provider audit.",
"45" : "Awaiting benefit determination.",
"46" : "Internal review/audit.",
"47" : "Internal review/audit - partial payment made.",
"49" : "Pending provider accreditation review.",
"50" : "Claim waiting for internal provider verification.",
"51" : "Investigating occupational illness/accident.",
"52" : "Investigating existence of other insurance coverage.",
"53" : "Claim being researched for Insured ID/Group Policy Number error.",
"54" : "Duplicate of a previously processed claim/line.",
"55" : "Claim assigned to an approver/analyst.",
"56" : "Awaiting eligibility determination.",
"57" : "Pending COBRA information requested.",
"59" : "Information was requested by a non-electronic method.",
"60" : "Information was requested by an electronic method.",
"61" : "Eligibility for extended benefits.",
"64" : "Re-pricing information.",
"65" : "Claim/line has been paid.",
"66" : "Payment reflects usual and customary charges.",
"72" : "Claim contains split payment.",
"73" : "Payment made to entity, assignment of benefits not on file.",
"78" : "Duplicate of an existing claim/line, awaiting processing.",
"81" : "Contract/plan does not cover pre-existing conditions.",
"83" : "No coverage for newborns.",
"84" : "Service not authorized.",
"85" : "Entity not primary.",
"86" : "Diagnosis and patient gender mismatch.",
"88" : "Entity not eligible for benefits for submitted dates of service.",
"89" : "Entity not eligible for dental benefits for submitted dates of service.",
"90" : "Entity not eligible for medical benefits for submitted dates of service.",
"91" : "Entity not eligible/not approved for dates of service.",
"92" : "Entity does not meet dependent or student qualification.",
"93" : "Entity is not selected primary care provider.",
"94" : "Entity not referred by selected primary care provider.",
"95" : "Requested additional information not received.",
"Notes:" : "If known, the payer must report a second claim status code identifying the requested information.",
"96" : "No agreement with entity.",
"97" : "Patient eligibility not found with entity.",
"98" : "Charges applied to deductible.",
"99" : "Pre-treatment review.",
"100" : "Pre-certification penalty taken.",
"101" : "Claim was processed as adjustment to previous claim.",
"102" : "Newborn's charges processed on mother's claim.",
"103" : "Claim combined with other claim(s).",
"104" : "Processed according to plan provisions (Plan refers to provisions that exist between the Health Plan and the Consumer or Patient)",
"105" : "Claim/line is capitated.",
"106" : "This amount is not entity's responsibility.",
"107" : "Processed according to contract provisions (Contract refers to provisions that exist between the Health Plan and a Provider of Health Care Services)",
"109" : "Entity not eligible.",
"110" : "Claim requires pricing information.",
"111" : "At the policyholder's request these claims cannot be submitted electronically.",
"114" : "Claim/service should be processed by entity.",
"116" : "Claim submitted to incorrect payer.",
"117" : "Claim requires signature-on-file indicator.",
"121" : "Service line number greater than maximum allowable for payer.",
"123" : "Additional information requested from entity.",
"124" : "Entity's name, address, phone and id number.",
"125" : "Entity's name.",
"126" : "Entity's address.",
"127" : "Entity's Communication Number.",
"128" : "Entity's tax id.",
"129" : "Entity's Blue Cross provider id.",
"130" : "Entity's Blue Shield provider id.",
"131" : "Entity's Medicare provider id.",
"132" : "Entity's Medicaid provider id.",
"133" : "Entity's UPIN.",
"134" : "Entity's CHAMPUS provider id.",
"135" : "Entity's commercial provider id.",
"136" : "Entity's health industry id number.",
"137" : "Entity's plan network id.",
"138" : "Entity's site id .",
"139" : "Entity's health maintenance provider id (HMO).",
"140" : "Entity's preferred provider organization id (PPO).",
"141" : "Entity's administrative services organization id (ASO).",
"142" : "Entity's license/certification number.",
"143" : "Entity's state license number.",
"144" : "Entity's specialty license number.",
"145" : "Entity's specialty/taxonomy code.",
"146" : "Entity's anesthesia license number.",
"147" : "Entity's qualification degree/designation (e.g. RN,PhD,MD).",
"148" : "Entity's social security number.",
"149" : "Entity's employer id.",
"150" : "Entity's drug enforcement agency (DEA) number.",
"152" : "Pharmacy processor number.",
"153" : "Entity's id number.",
"154" : "Relationship of surgeon & assistant surgeon.",
"155" : "Entity's relationship to patient.",
"156" : "Patient relationship to subscriber",
"157" : "Entity's Gender.",
"158" : "Entity's date of birth.",
"159" : "Entity's date of death.",
"160" : "Entity's marital status.",
"161" : "Entity's employment status.",
"162" : "Entity's health insurance claim number (HICN).",
"163" : "Entity's policy number.",
"164" : "Entity's contract/member number.",
"165" : "Entity's employer name, address and phone.",
"166" : "Entity's employer name.",
"167" : "Entity's employer address.",
"168" : "Entity's employer phone number.",
"170" : "Entity's employee id.",
"171" : "Other insurance coverage information (health, liability, auto, etc.).",
"172" : "Other employer name, address and telephone number.",
"173" : "Entity's name, address, phone, gender, DOB, marital status, employment status and relation to subscriber.",
"174" : "Entity's student status.",
"175" : "Entity's school name.",
"176" : "Entity's school address.",
"177" : "Transplant recipient's name, date of birth, gender, relationship to insured.",
"178" : "Submitted charges.",
"179" : "Outside lab charges.",
"180" : "Hospital s semi-private room rate.",
"181" : "Hospital s room rate.",
"182" : "Allowable/paid from other entities coverage NOTE: This code requires the use of an entity code.",
"183" : "Amount entity has paid.",
"184" : "Purchase price for the rented durable medical equipment.",
"185" : "Rental price for durable medical equipment.",
"186" : "Purchase and rental price of durable medical equipment.",
"187" : "Date(s) of service.",
"188" : "Statement from-through dates.",
"189" : "Facility admission date",
"190" : "Facility discharge date",
"191" : "Date of Last Menstrual Period (LMP)",
"192" : "Date of first service for current series/symptom/illness.",
"193" : "First consultation/evaluation date.",
"194" : "Confinement dates.",
"195" : "Unable to work dates/Disability Dates.",
"196" : "Return to work dates.",
"197" : "Effective coverage date(s).",
"198" : "Medicare effective date.",
"199" : "Date of conception and expected date of delivery.",
"200" : "Date of equipment return.",
"201" : "Date of dental appliance prior placement.",
"202" : "Date of dental prior replacement/reason for replacement.",
"203" : "Date of dental appliance placed.",
"204" : "Date dental canal(s) opened and date service completed.",
"205" : "Date(s) dental root canal therapy previously performed.",
"206" : "Most recent date of curettage, root planing, or periodontal surgery.",
"207" : "Dental impression and seating date.",
"208" : "Most recent date pacemaker was implanted.",
"209" : "Most recent pacemaker battery change date.",
"210" : "Date of the last x-ray.",
"211" : "Date(s) of dialysis training provided to patient.",
"212" : "Date of last routine dialysis.",
"213" : "Date of first routine dialysis.",
"214" : "Original date of prescription/orders/referral.",
"215" : "Date of tooth extraction/evolution.",
"216" : "Drug information.",
"217" : "Drug name, strength and dosage form.",
"218" : "NDC number.",
"219" : "Prescription number.",
"222" : "Drug dispensing units and average wholesale price (AWP).",
"223" : "Route of drug/myelogram administration.",
"224" : "Anatomical location for joint injection.",
"225" : "Anatomical location.",
"226" : "Joint injection site.",
"227" : "Hospital information.",
"228" : "Type of bill for UB claim",
"229" : "Hospital admission source.",
"230" : "Hospital admission hour.",
"231" : "Hospital admission type.",
"232" : "Admitting diagnosis.",
"233" : "Hospital discharge hour.",
"234" : "Patient discharge status.",
"235" : "Units of blood furnished.",
"236" : "Units of blood replaced.",
"237" : "Units of deductible blood.",
"238" : "Separate claim for mother/baby charges.",
"239" : "Dental information.",
"240" : "Tooth surface(s) involved.",
"241" : "List of all missing teeth (upper and lower).",
"242" : "Tooth numbers, surfaces, and/or quadrants involved.",
"243" : "Months of dental treatment remaining.",
"244" : "Tooth number or letter.",
"245" : "Dental quadrant/arch.",
"246" : "Total orthodontic service fee, initial appliance fee, monthly fee, length of service.",
"247" : "Line information.",
"249" : "Place of service.",
"250" : "Type of service.",
"251" : "Total anesthesia minutes.",
"252" : "Entity's authorization/certification number.",
"254" : "Principal diagnosis code.",
"255" : "Diagnosis code.",
"256" : "DRG code(s).",
"257" : "ADSM-III-R code for services rendered.",
"258" : "Days/units for procedure/revenue code.",
"259" : "Frequency of service.",
"260" : "Length of medical necessity, including begin date.",
"261" : "Obesity measurements.",
"262" : "Type of surgery/service for which anesthesia was administered.",
"263" : "Length of time for services rendered.",
"264" : "Number of liters/minute & total hours/day for respiratory support.",
"265" : "Number of lesions excised.",
"266" : "Facility point of origin and destination - ambulance.",
"267" : "Number of miles patient was transported.",
"268" : "Location of durable medical equipment use.",
"269" : "Length/size of laceration/tumor.",
"270" : "Subluxation location.",
"271" : "Number of spine segments.",
"272" : "Oxygen contents for oxygen system rental.",
"273" : "Weight.",
"274" : "Height.",
"275" : "Claim.",
"276" : "UB04/HCFA-1450/1500 claim form",
"277" : "Paper claim.",
"279" : "Claim/service must be itemized",
"281" : "Related confinement claim.",
"282" : "Copy of prescription.",
"283" : "Medicare entitlement information is required to determine primary coverage",
"284" : "Copy of Medicare ID card.",
"286" : "Other payer's Explanation of Benefits/payment information.",
"287" : "Medical necessity for service.",
"288" : "Hospital late charges",
"290" : "Pre-existing information.",
"291" : "Reason for termination of pregnancy.",
"292" : "Purpose of family conference/therapy.",
"293" : "Reason for physical therapy.",
"294" : "Supporting documentation.",
"295" : "Attending physician report.",
"296" : "Nurse's notes.",
"297" : "Medical notes/report.",
"298" : "Operative report.",
"299" : "Emergency room notes/report.",
"300" : "Lab/test report/notes/results.",
"301" : "MRI report.",
"305" : "Radiology/x-ray reports and/or interpretation",
"306" : "Detailed description of service.",
"307" : "Narrative with pocket depth chart.",
"308" : "Discharge summary.",
"310" : "Progress notes for the six months prior to statement date.",
"311" : "Pathology notes/report.",
"312" : "Dental charting.",
"313" : "Bridgework information.",
"314" : "Dental records for this service.",
"315" : "Past perio treatment history.",
"316" : "Complete medical history.",
"318" : "X-rays/radiology films",
"319" : "Pre/post-operative x-rays/photographs.",
"320" : "Study models.",
"322" : "Recent Full Mouth X-rays",
"323" : "Study models, x-rays, and/or narrative.",
"324" : "Recent x-ray of treatment area and/or narrative.",
"325" : "Recent fm x-rays and/or narrative.",
"326" : "Copy of transplant acquisition invoice.",
"327" : "Periodontal case type diagnosis and recent pocket depth chart with narrative.",
"329" : "Exercise notes.",
"330" : "Occupational notes.",
"331" : "History and physical.",
"333" : "Patient release of information authorization.",
"334" : "Oxygen certification.",
"335" : "Durable medical equipment certification.",
"336" : "Chiropractic certification.",
"337" : "Ambulance certification/documentation.",
"339" : "Enteral/parenteral certification.",
"340" : "Pacemaker certification.",
"341" : "Private duty nursing certification.",
"342" : "Podiatric certification.",
"343" : "Documentation that facility is state licensed and Medicare approved as a surgical facility.",
"344" : "Documentation that provider of physical therapy is Medicare Part B approved.",
"345" : "Treatment plan for service/diagnosis",
"346" : "Proposed treatment plan for next 6 months.",
"352" : "Duration of treatment plan.",
"353" : "Orthodontics treatment plan.",
"354" : "Treatment plan for replacement of remaining missing teeth.",
"360" : "Benefits Assignment Certification Indicator",
"363" : "Possible Workers' Compensation",
"364" : "Is accident/illness/condition employment related?",
"365" : "Is service the result of an accident?",
"366" : "Is injury due to auto accident?",
"374" : "Is prescribed lenses a result of cataract surgery?",
"375" : "Was refraction performed?",
"380" : "CRNA supervision/medical direction.",
"382" : "Did provider authorize generic or brand name dispensing?",
"383" : "Nerve block use (surgery vs. pain management)",
"384" : "Is prosthesis/crown/inlay placement an initial placement or a replacement?",
"385" : "Is appliance upper or lower arch & is appliance fixed or removable?",
"386" : "Orthodontic Treatment/Purpose Indicator",
"387" : "Date patient last examined by entity.",
"388" : "Date post-operative care assumed",
"389" : "Date post-operative care relinquished",
"390" : "Date of most recent medical event necessitating service(s)",
"391" : "Date(s) dialysis conducted",
"394" : "Date(s) of most recent hospitalization related to service",
"395" : "Date entity signed certification/recertification",
"396" : "Date home dialysis began",
"397" : "Date of onset/exacerbation of illness/condition",
"398" : "Visual field test results",
"400" : "Claim is out of balance",
"401" : "Source of payment is not valid",
"402" : "Amount must be greater than zero.",
"403" : "Entity referral notes/orders/prescription",
"406" : "Brief medical history as related to service(s)",
"407" : "Complications/mitigating circumstances",
"408" : "Initial certification",
"409" : "Medication logs/records (including medication therapy)",
"414" : "Necessity for concurrent care (more than one physician treating the patient)",
"417" : "Prior testing, including result(s) and date(s) as related to service(s)",
"419" : "Individual test(s) comprising the panel and the charges for each test",
"420" : "Name, dosage and medical justification of contrast material used for radiology procedure",
"428" : "Reason for transport by ambulance",
"430" : "Nearest appropriate facility",
"431" : "Patient's condition/functional status at time of service.",
"432" : "Date benefits exhausted",
"433" : "Copy of patient revocation of hospice benefits",
"434" : "Reasons for more than one transfer per entitlement period",
"435" : "Notice of Admission",
"441" : "Entity professional qualification for service(s)",
"442" : "Modalities of service",
"443" : "Initial evaluation report",
"449" : "Projected date to discontinue service(s)",
"450" : "Awaiting spend down determination",
"451" : "Preoperative and post-operative diagnosis",
"452" : "Total visits in total number of hours/day and total number of hours/week",
"453" : "Procedure Code Modifier(s) for Service(s) Rendered",
"454" : "Procedure code for services rendered.",
"455" : "Revenue code for services rendered.",
"456" : "Covered Day(s)",
"457" : "Non-Covered Day(s)",
"458" : "Coinsurance Day(s)",
"459" : "Lifetime Reserve Day(s)",
"460" : "NUBC Condition Code(s)",
"464" : "Payer Assigned Claim Control Number",
"465" : "Principal Procedure Code for Service(s) Rendered",
"466" : "Entity's Original Signature.",
"467" : "Entity Signature Date.",
"468" : "Patient Signature Source",
"469" : "Purchase Service Charge",
"470" : "Was service purchased from another entity?",
"471" : "Were services related to an emergency?",
"472" : "Ambulance Run Sheet",
"473" : "Missing or invalid lab indicator",
"474" : "Procedure code and patient gender mismatch",
"475" : "Procedure code not valid for patient age",
"476" : "Missing or invalid units of service",
"477" : "Diagnosis code pointer is missing or invalid",
"478" : "Claim submitter's identifier",
"479" : "Other Carrier payer ID is missing or invalid",
"480" : "Entity's claim filing indicator.",
"481" : "Claim/submission format is invalid.",
"483" : "Maximum coverage amount met or exceeded for benefit period.",
"484" : "Business Application Currently Not Available",
"485" : "More information available than can be returned in real time mode. Narrow your current search criteria.",
"486" : "Principal Procedure Date",
"487" : "Claim not found, claim should have been submitted to/through 'entity'.",
"488" : "Diagnosis code(s) for the services rendered.",
"489" : "Attachment Control Number",
"490" : "Other Procedure Code for Service(s) Rendered",
"491" : "Entity not eligible for encounter submission.",
"492" : "Other Procedure Date",
"493" : "Version/Release/Industry ID code not currently supported by information holder",
"494" : "Real-Time requests not supported by the information holder, resubmit as batch request",
"495" : "Requests for re-adjudication must reference the newly assigned payer claim control number for this previously adjusted claim. Correct the payer claim control number and re-submit.",
"496" : "Submitter not approved for electronic claim submissions on behalf of this entity.",
"497" : "Sales tax not paid",
"498" : "Maximum leave days exhausted",
"499" : "No rate on file with the payer for this service for this entity",
"500" : "Entity's Postal/Zip Code.",
"501" : "Entity's State/Province.",
"502" : "Entity's City.",
"503" : "Entity's Street Address.",
"504" : "Entity's Last Name.",
"505" : "Entity's First Name.",
"506" : "Entity is changing processor/clearinghouse. This claim must be submitted to the new processor/clearinghouse.",
"507" : "HCPCS",
"508" : "ICD9 NOTE: At least one other status code is required to identify the related procedure code or diagnosis code.",
"509" : "External Cause of Injury Code (E-code).",
"510" : "Future date.",
"511" : "Invalid character.",
"512" : "Length invalid for receiver's application system.",
"513" : "HIPPS Rate Code for services Rendered",
"514" : "Entity's Middle Name",
"515" : "Managed Care review",
"516" : "Other Entity's Adjudication or Payment/Remittance Date.",
"517" : "Adjusted Repriced Claim Reference Number",
"518" : "Adjusted Repriced Line item Reference Number",
"519" : "Adjustment Amount",
"520" : "Adjustment Quantity",
"521" : "Adjustment Reason Code",
"522" : "Anesthesia Modifying Units",
"523" : "Anesthesia Unit Count",
"524" : "Arterial Blood Gas Quantity",
"525" : "Begin Therapy Date",
"526" : "Bundled or Unbundled Line Number",
"527" : "Certification Condition Indicator",
"528" : "Certification Period Projected Visit Count",
"529" : "Certification Revision Date",
"530" : "Claim Adjustment Indicator",
"531" : "Claim Disproportinate Share Amount",
"532" : "Claim DRG Amount",
"533" : "Claim DRG Outlier Amount",
"534" : "Claim ESRD Payment Amount",
"535" : "Claim Frequency Code",
"536" : "Claim Indirect Teaching Amount",
"537" : "Claim MSP Pass-through Amount",
"538" : "Claim or Encounter Identifier",
"539" : "Claim PPS Capital Amount",
"540" : "Claim PPS Capital Outlier Amount",
"541" : "Claim Submission Reason Code",
"542" : "Claim Total Denied Charge Amount",
"543" : "Clearinghouse or Value Added Network Trace",
"544" : "Clinical Laboratory Improvement Amendment",
"545" : "Contract Amount",
"546" : "Contract Code",
"547" : "Contract Percentage",
"548" : "Contract Type Code",
"549" : "Contract Version Identifier",
"550" : "Coordination of Benefits Code",
"551" : "Coordination of Benefits Total Submitted Charge",
"552" : "Cost Report Day Count",
"553" : "Covered Amount",
"554" : "Date Claim Paid",
"555" : "Delay Reason Code",
"556" : "Demonstration Project Identifier",
"557" : "Diagnosis Date",
"558" : "Discount Amount",
"559" : "Document Control Identifier",
"560" : "Entity's Additional/Secondary Identifier.",
"561" : "Entity's Contact Name.",
"562" : "Entity's National Provider Identifier (NPI).",
"563" : "Entity's Tax Amount.",
"564" : "EPSDT Indicator",
"565" : "Estimated Claim Due Amount",
"566" : "Exception Code",
"567" : "Facility Code Qualifier",
"568" : "Family Planning Indicator",
"569" : "Fixed Format Information",
"571" : "Frequency Count",
"572" : "Frequency Period",
"573" : "Functional Limitation Code",
"574" : "HCPCS Payable Amount Home Health",
"575" : "Homebound Indicator",
"576" : "Immunization Batch Number",
"577" : "Industry Code",
"578" : "Insurance Type Code",
"579" : "Investigational Device Exemption Identifier",
"580" : "Last Certification Date",
"581" : "Last Worked Date",
"582" : "Lifetime Psychiatric Days Count",
"583" : "Line Item Charge Amount",
"584" : "Line Item Control Number",
"585" : "Denied Charge or Non-covered Charge",
"586" : "Line Note Text",
"587" : "Measurement Reference Identification Code",
"588" : "Medical Record Number",
"589" : "Provider Accept Assignment Code",
"590" : "Medicare Coverage Indicator",
"591" : "Medicare Paid at 100% Amount",
"592" : "Medicare Paid at 80% Amount",
"593" : "Medicare Section 4081 Indicator",
"594" : "Mental Status Code",
"595" : "Monthly Treatment Count",
"596" : "Non-covered Charge Amount",
"597" : "Non-payable Professional Component Amount",
"598" : "Non-payable Professional Component Billed Amount",
"599" : "Note Reference Code",
"600" : "Oxygen Saturation Qty",
"601" : "Oxygen Test Condition Code",
"602" : "Oxygen Test Date",
"603" : "Old Capital Amount",
"604" : "Originator Application Transaction Identifier",
"605" : "Orthodontic Treatment Months Count",
"606" : "Paid From Part A Medicare Trust Fund Amount",
"607" : "Paid From Part B Medicare Trust Fund Amount",
"608" : "Paid Service Unit Count",
"609" : "Participation Agreement",
"610" : "Patient Discharge Facility Type Code",
"611" : "Peer Review Authorization Number",
"612" : "Per Day Limit Amount",
"613" : "Physician Contact Date",
"614" : "Physician Order Date",
"615" : "Policy Compliance Code",
"616" : "Policy Name",
"617" : "Postage Claimed Amount",
"618" : "PPS-Capital DSH DRG Amount",
"619" : "PPS-Capital Exception Amount",
"620" : "PPS-Capital FSP DRG Amount",
"621" : "PPS-Capital HSP DRG Amount",
"622" : "PPS-Capital IME Amount",
"623" : "PPS-Operating Federal Specific DRG Amount",
"624" : "PPS-Operating Hospital Specific DRG Amount",
"625" : "Predetermination of Benefits Identifier",
"626" : "Pregnancy Indicator",
"627" : "Pre-Tax Claim Amount",
"628" : "Pricing Methodology",
"629" : "Property Casualty Claim Number",
"630" : "Referring CLIA Number",
"631" : "Reimbursement Rate",
"632" : "Reject Reason Code",
"633" : "Related Causes Code (Accident, auto accident, employment)",
"634" : "Remark Code",
"635" : "Repriced Ambulatory Patient Group Code",
"636" : "Repriced Line Item Reference Number",
"637" : "Repriced Saving Amount",
"638" : "Repricing Per Diem or Flat Rate Amount",
"639" : "Responsibility Amount",
"640" : "Sales Tax Amount",
"642" : "Service Authorization Exception Code",
"643" : "Service Line Paid Amount",
"644" : "Service Line Rate",
"645" : "Service Tax Amount",
"646" : "Ship, Delivery or Calendar Pattern Code",
"647" : "Shipped Date",
"648" : "Similar Illness or Symptom Date",
"649" : "Skilled Nursing Facility Indicator",
"650" : "Special Program Indicator",
"651" : "State Industrial Accident Provider Number",
"652" : "Terms Discount Percentage",
"653" : "Test Performed Date",
"654" : "Total Denied Charge Amount",
"655" : "Total Medicare Paid Amount",
"656" : "Total Visits Projected This Certification Count",
"657" : "Total Visits Rendered Count",
"658" : "Treatment Code",
"659" : "Unit or Basis for Measurement Code",
"660" : "Universal Product Number",
"661" : "Visits Prior to Recertification Date Count CR702",
"662" : "X-ray Availability Indicator",
"663" : "Entity's Group Name.",
"664" : "Orthodontic Banding Date",
"665" : "Surgery Date",
"666" : "Surgical Procedure Code",
"667" : "Real-Time requests not supported by the information holder, do not resubmit",
"668" : "Missing Endodontics treatment history and prognosis",
"669" : "Dental service narrative needed.",
"670" : "Funds applied from a consumer spending account such as consumer directed/driven health plan (CDHP), Health savings account (H S A) and or other similar accounts",
"671" : "Funds may be available from a consumer spending account such as consumer directed/driven health plan (CDHP), Health savings account (H S A) and or other similar accounts",
"672" : "Other Payer's payment information is out of balance",
"673" : "Patient Reason for Visit",
"674" : "Authorization exceeded",
"675" : "Facility admission through discharge dates",
"676" : "Entity possibly compensated by facility.",
"677" : "Entity not affiliated.",
"678" : "Revenue code and patient gender mismatch",
"679" : "Submit newborn services on mother's claim",
"680" : "Entity's Country.",
"681" : "Claim currency not supported",
"682" : "Cosmetic procedure",
"683" : "Awaiting Associated Hospital Claims",
"684" : "Rejected. Syntax error noted for this claim/service/inquiry. See Functional or Implementation Acknowledgement for details. (Note: Only for use to reject claims or status requests in transactions that were 'accepted with errors' on a 997 or 999 Acknowledgement.)",
"685" : "Claim could not complete adjudication in real time. Claim will continue processing in a batch mode. Do not resubmit.",
"686" : "The claim/ encounter has completed the adjudication cycle and the entire claim has been voided",
"687" : "Claim estimation can not be completed in real time. Do not resubmit.",
"688" : "Present on Admission Indicator for reported diagnosis code(s).",
"689" : "Entity was unable to respond within the expected time frame.",
"690" : "Multiple claims or estimate requests cannot be processed in real time.",
"691" : "Multiple claim status requests cannot be processed in real time.",
"692" : "Contracted funding agreement-Subscriber is employed by the provider of services",
"693" : "Amount must be greater than or equal to zero.",
"694" : "Amount must not be equal to zero.",
"695" : "Entity's Country Subdivision Code.",
"696" : "Claim Adjustment Group Code.",
"697" : "Invalid Decimal Precision.",
"698" : "Form Type Identification",
"699" : "Question/Response from Supporting Documentation Form",
"700" : "ICD10.",
"701" : "Initial Treatment Date",
"702" : "Repriced Claim Reference Number",
"703" : "Advanced Billing Concepts (ABC) code",
"704" : "Claim Note Text",
"705" : "Repriced Allowed Amount",
"706" : "Repriced Approved Amount",
"707" : "Repriced Approved Ambulatory Patient Group Amount",
"708" : "Repriced Approved Revenue Code",
"709" : "Repriced Approved Service Unit Count",
"710" : "Line Adjudication Information.",
"711" : "Stretcher purpose",
"712" : "Obstetric Additional Units",
"713" : "Patient Condition Description",
"714" : "Care Plan Oversight Number",
"715" : "Acute Manifestation Date",
"716" : "Repriced Approved DRG Code",
"717" : "This claim has been split for processing.",
"718" : "Claim/service not submitted within the required timeframe (timely filing).",
"719" : "NUBC Occurrence Code(s)",
"720" : "NUBC Occurrence Code Date(s)",
"721" : "NUBC Occurrence Span Code(s)",
"722" : "NUBC Occurrence Span Code Date(s)",
"723" : "Drug days supply",
"724" : "Drug dosage",
"725" : "NUBC Value Code(s)",
"726" : "NUBC Value Code Amount(s)",
"727" : "Accident date",
"728" : "Accident state",
"729" : "Accident description",
"730" : "Accident cause",
"731" : "Measurement value/test result",
"732" : "Information submitted inconsistent with billing guidelines.",
"733" : "Prefix for entity's contract/member number.",
"734" : "Verifying premium payment",
"735" : "This service/claim is included in the allowance for another service or claim.",
"736" : "A related or qualifying service/claim has not been received/adjudicated.",
"737" : "Current Dental Terminology (CDT) Code",
"738" : "Home Infusion EDI Coalition (HEIC) Product/Service Code",
"739" : "Jurisdiction Specific Procedure or Supply Code",
"740" : "Drop-Off Location",
"741" : "Entity must be a person.",
"742" : "Payer Responsibility Sequence Number Code",
"743" : "Entity's credential/enrollment information.",
"744" : "Services/charges related to the treatment of a hospital-acquired condition or preventable medical error.",
"745" : "Identifier Qualifier",
"746" : "Duplicate Submission",
"747" : "Hospice Employee Indicator",
"748" : "Corrected Data",
"749" : "Date of Injury/Illness",
"750" : "Auto Accident State or Province Code",
"751" : "Ambulance Pick-up State or Province Code",
"752" : "Ambulance Drop-off State or Province Code",
"753" : "Co-pay status code.",
"754" : "Entity Name Suffix.",
"755" : "Entity's primary identifier.",
"756" : "Entity's Received Date.",
"757" : "Last seen date.",
"758" : "Repriced approved HCPCS code.",
"759" : "Round trip purpose description.",
"760" : "Tooth status code.",
"761" : "Entity's referral number.",
"762" : "Locum Tenens Provider Identifier. Code must be used with Entity Code 82 - Rendering Provider",
"763" : "Ambulance Pickup ZipCode",
"764" : "Professional charges are non covered.",
"765" : "Institutional charges are non covered.",
"766" : "Services were performed during a Health Insurance Exchange (HIX) premium payment grace period.",
"767" : "Qualifications for emergent/urgent care",
"768" : "Service date outside the accidental injury coverage period.",
"769" : "DME Repair or Maintenance",
"770" : "Duplicate of a claim processed or in process as a crossover/coordination of benefits claim.",
"771" : "Claim submitted prematurely. Please resubmit after crossover/payer to payer COB allotted waiting period.",
"772" : "The greatest level of diagnosis code specificity is required."
    }

def code_to_str(code):
    return __CODE_MAP[code]
