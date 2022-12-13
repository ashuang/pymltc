import argparse
import datetime
import random
import re
import sys

import dbf
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog = 'remove_pii')

    parser.add_argument('--max-count', type=int, default=sys.maxsize)
    parser.add_argument('input')
    parser.add_argument('output')

    args = parser.parse_args()

    in_dbf = dbf.dbf(args.input)

    fields_to_sanitize = set([
        "LASTNAME",
        "FIRSTNAME",
        "ADDRESS1",
        "SS",
        "DOB",
        "PHONE",
        "BILLADDR1",
        "BILLADDR2",
        "BILLPHONE",
        "BILLPHONE",
        "MEDICARE",
        "COINSURE1",
        "COINSURE2",
        "BILLNOTE",
        "COINS_NO",
        "SUB_LNAME",
        "SUB_FNAME",
        "NOTE1",
        "NOTE2",
        ])

    field_descriptors = [ [ field.name, field.type, field.len, field.decimal, False ] \
            for field in in_dbf.fields ]

    out_dbf = dbf.create(args.output, field_descriptors)

    max_count = min(in_dbf.numrecords, args.max_count)

    print("Processing {} records".format(max_count))

    san_re = re.compile('[^ ]')

    def sanitize(field_name, value):
        if field_name not in fields_to_sanitize or value is None:
            return value
        if type(value) == datetime.date:
            return datetime.date(value.year, random.randint(1, 11), random.randint(1, 28))
        vlen = len(value)
        return value[:3] + san_re.sub("X", value[3:])


    for i in range(max_count):
        out_dbf.append_blank()

        for field in in_dbf.fields:
            in_val = in_dbf[field.name]
            out_val = sanitize(field.name, in_val)
            out_dbf[field.name] = out_val

        in_dbf.skip(1)

    print("Processed {} records".format(max_count))
