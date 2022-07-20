# Utility program to fix the delete flag on a dBase IV .DBF file.  We've had a
# problem where some of our records are corrupted, and the delete flags are
# incorrect.  This causes problems when trying to import the .DBF file into an
# external program such as Microsoft Access.  This program scans the .DBF for
# invalid delete flags, and replaces invalid flags with a valid one (i.e.,
# not-deleted-flag)
import sys
from dbf import dbf

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "must specify dbf file"
        sys.exit(1)

    a = dbf(sys.argv[1])

    position = 0
    while True:
        # Read in the current record
        record_data = a.f.read(a.recordsize)

        # Stop processing if we've reached the end of the file.
        if len(record_data) != a.recordsize:
            break

        # Check to see if the delete flag is valid, and fix it if not
        deleted_byte = record_data[0]
        if deleted_byte not in [ '\x2a', '\x20' ]:
            print("Fixing bad delete flag '0x%X' at record %d" % \
                    (ord(deleted_byte), position))
            a.f.seek(-a.recordsize, 1)
            a.f.write("\x20")
            a.f.seek(a.recordsize-1, 1)

        position += 1
