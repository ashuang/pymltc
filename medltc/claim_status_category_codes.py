"""Adapted from http://www.wpc-edi.com/reference/codelists/healthcare/claim-status-category-codes/

Date: 12/26/2014
"""

__CODE_MAP = {
"A0" : "Forwarded to another entity",
"A1" : "Receipt acknowledged",
"A2" : "Accepted for adjustication",
"A3" : "Rejected: unprocessable",
"A4" : "Not found in the adjudication system",
"A5" : "Split upon acceptance into the adjudication system",
"A6" : "Rejected: Missing Information",
"A7" : "Rejected: Invalid Information",
"A8" : "Rejected: Relational field in error",
"P0" : "Pending",
"P1" : "Pending/In Process",
"P2" : "Suspended, pending review",
"P3" : "Waiting for information from provider",
"P4" : "Waiting for information from patient",
"P5" : "Pending/Payer Administrative/System hold",
"F0" : "Finalized: no more action will be taken",
"F1" : "Finalized: paid",
"F2" : "Finalized: denied",
"F3" : "Finalized: changed",
"F3F" : "Finalized: Forwarded to another entity",
"F3N" : "Finalized: Processing complete",
"F4" : "Finalized: No further payment forthcoming",
"R0" : "Requests for additional Information/General Requests-Requests that don't fall into other R-type categories.",
"R1" : "Requests for additional Information/Entity Requests-Requests for information about specific entities (subscribers, patients, various providers).",
"R3" : "Requests for additional Information/Claim/Line-Requests for information that could normally be submitted on a claim.",
"R4" : "Requests for additional Information/Documentation-Requests for additional supporting documentation. Examples: certification, x-ray, notes.",
"R5" : "Request for additional information/more specific detail-Additional information as a follow up to a previous request is needed. The original information was received but is inadequate. More specific/detailed information is requested.",
"R6" : "Requests for additional information - Regulatory requirements",
"R7" : "Requests for additional information - Confirm care is consistent with Health Plan policy coverage",
"R8" : "Requests for additional information - Confirm care is consistent with health plan coverage exceptions",
"R9" : "Requests for additional information - Determination of medical necessity",
"R10" : "Requests for additional information - Support a filed grievance or appeal",
"R11" : "Requests for additional information - Pre-payment review of claims",
"R12" : "Requests for additional information - Clarification or justification of use for specified procedure code",
"R13" : "Requests for additional information - Original documents submitted are not readable. Used only for subsequent request(s).",
"R14" : "Requests for additional information - Original documents received are not what was requested. Used only for subsequent request(s).",
"R15" : "Requests for additional information - Workers Compensation coverage determination.",
"R16" : "Requests for additional information - Eligibility determination",
"R17" : "Replacement of a Prior Request. Used to indicate that the current attachment request replaces a prior attachment request.",
"E0" : "Response not possible - error on submitted request data",
"E1" : "Response not possible - System Status",
"E2" : "Information Holder is not responding; resubmit at a later time.",
"E3" : "Correction required - relational fields in error.",
"E4" : "Trading partner agreement specific requirement not met: Data correction required. (Note: A status code identifying the type of information requested must be sent)",
"D0" : "Data Search Unsuccessful - The payer is unable to return status on the requested claim(s) based on the submitted search criteria." }

def code_to_str(code):
    return __CODE_MAP[code]
