from xml.dom import minidom

from remittance_advice_remark_codes import REMITTANCE_ADVICE_REMARK_CODES_RAW
from claim_adjustment_reason_codes import CLAIM_ADJUSTMENT_REASON_CODES_RAW

def get_text(nodes):
    return (''.join([node.data for node in nodes if node.nodeType == node.TEXT_NODE])).strip()

def __get_remarks():
    doc = minidom.parseString(REMITTANCE_ADVICE_REMARK_CODES_RAW)
    result = {}
    for row in doc.documentElement.getElementsByTagName("tr"):
        code_col, desc_col = row.getElementsByTagName("td")
        code = code_col.childNodes[0].data.strip().upper() 
        description = get_text(desc_col.childNodes)
        result[code] = description
#        print code, description
    return result

def __get_reason_codes():
    doc = minidom.parseString(CLAIM_ADJUSTMENT_REASON_CODES_RAW)
    result = {}
    for row in doc.documentElement.getElementsByTagName("tr"):
        code_col, desc_col = row.getElementsByTagName("td")
        code = code_col.childNodes[0].data.strip().upper() 
        description = get_text(desc_col.childNodes)
        result[code] = description
#        print code, description
    return result

__remarks = __get_remarks()
__reasons = __get_reason_codes()

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

def CLPStatusCodeIsPaid(code):
    return code in [ "1", "2", "3", "19", "20", "21" ]

if __name__ == "__main__":
    import sys
    import getopt

    def usage():
        print "usage: ansi835codes.py [--todbf=DBFNAME] < reasons | remarks >"
        sys.exit(1)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["todbf="])
    except getopt.GetoptError, err:
        usage()

    dbfname = None
    for o, a in opts:
        if o == "--todbf":
            dbfname = a

    if not args:
        usage()

    which_codes = args[0]

    if which_codes == "remarks":
        codes = __remarks
    elif which_codes == "reasons":
        codes = __reasons
    else:
        usage()

    if dbfname:
        import dbf
        db = dbf.create( dbfname, 
                 [ ( "CODE",     "C", 5,  0, False ),
                   ( "DESC",     "C", 254,  0, False ),
                   ] )
        keys = codes.keys()
        keys.sort()
        for code in keys:
            description = codes[code]
            db.append_blank()
            db["CODE"] = code
            db["DESC"] = description[:254]
    else:
        keys = codes.keys()
        keys.sort()
        for code in keys:
            print code, codes[code]
