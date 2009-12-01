"""Provides read/write access to a dBase IV 2.0 DBF database file.  The
interface tries to adhere to the original dBase IV programming environment,
with a single record pointer marking the current position within the file.

Does not provide methods to create .DBF files or modify their structure.
"""
# $Id: dbf.py,v 1.4 2006/07/14 22:30:16 albert Exp $
#
# using dbf file format as specified by this website
# http://www.geocities.com/geoff_wass/dBASE/GaryWhite/dBASE/FAQ/qformt.htm
# some things were different in actual implementation
#
# 

import binascii
import datetime
from datetime import date
from datetime import time
import struct

Character = 'C'
Date = 'D'
Float = 'F'
Numeric = 'N'
Logical = 'L'
Memo = 'M'

def ccyymmdd2date(ccyymmdd):
    if len(ccyymmdd) != 8:
        raise ValueError("invalid string %s" % ccyymmdd)
    year = int(ccyymmdd[0:4])
    month = int(ccyymmdd[4:6])
    day = int(ccyymmdd[6:8])

    if month < 1 or month > 12 or day < 1 or day > 31:
        raise ValueError("invalid date")

    return date(year, month, day)

def date2ccyymmdd(d):
    return d.strftime("%Y%m%d")

class field:
    def __init__(self, rawtext, offset):
        assert len(rawtext) == 32
#        print binascii.hexlify(rawtext)
        self.name = rawtext[:11]
        i = self.name.find("\0")
        if i > 0: self.name = self.name[:i]

        self.type = rawtext[11]
        if self.type not in [ "C", "D", "F", "L", "M", "N" ]:
            raise ValueError("invalid field type [%s]" % self.type)
        self.len = ord(rawtext[16])
        self.decimal = ord(rawtext[17])
        self.offset = offset
#        self.work_area_id = rawtext[20]
#        t = ord(rawtext[31])
#        if t == 0: 
#            self.mdx = False
#        elif t == 1:
#            self.mdx = True
#        else:
#            raise ValueError("invalid mdx field flag")

    def info(self):
        s = "[%s, %s, %d, %d]" % (self.name, self.type, self.len, self.decimal)
        return s

class record:
    def __init__(self, fields, rawtext):
        self.dirty = False
        self.r = {}
        self.fields = fields
        self.deleted = False
        self.values = []

        if fields == None: return  # EOF record

        checksum = 0
        for fld in fields:
            checksum += fld.len

        # size of a record should be the sum of the field lengths plus one byte
        # that marks whether the record is deleted or not
        if checksum != len(rawtext)- 1:
            raise ValueError("sum of field lengths = %d, textlen = %d" % \
                    (checksum, len(rawtext)))

        self.deleted = (rawtext[0] == '\x2a')
        if rawtext[0] not in [ '\x2a', '\x20' ]:
            pass
#            import sys
#            sys.stderr.write("invalid delete flag 0x%X\n" % ord(rawtext[0]))
        for fld in fields:
            rawval = rawtext[fld.offset:fld.offset + fld.len]
            if fld.type == "C":
                # character
                self.r[fld.name] = rawval
                self.values.append(rawval)
            elif fld.type == "D":
                # date
                try:
                    d = ccyymmdd2date(rawval)
                    self.values.append(d)
                    self.r[fld.name] = d
                except ValueError:
                    self.r[fld.name] = None
                    self.values.append(None)
            elif fld.type == "F":
                # float
                try:
                    v = float(rawval)
                    self.values.append(v)
                    self.r[fld.name] = v
                except ValueError:
                    self.values.append(None)
                    self.r[fld.name] = None
            elif fld.type == "L":
                # logical
                self.r[fld.name] = rawval[0]
                self.values.append(rawval[0])
            elif fld.type == "M":
                # memo

                # TODO
                self.r[fld.name] = rawval
                self.values.append(rawval)
            elif fld.type == "N":
                #                print binascii.hexlify(rawval), rawval
                # decimal
                try:
                    if fld.decimal > 0:
                        v = float(rawval)
                        self.values.append(v)
                        self.r[fld.name] = v
                    else:
                        v = float(rawval)
                        self.values.append(v)
                        self.r[fld.name] = int(rawval)
                except ValueError:
                    self.r[fld.name] = None
                    self.values.append(None)
            else:
                assert False, "invalid field type"

    def get_rawtext(self):
        """returns the raw string that would be inserted into the .DBF file if
        this record were flushed to disk.
        """
        recordlen = 1
        for fld in self.fields: recordlen += fld.len
        rawtext = '\x20' * recordlen
        if self.deleted: rawtext = '\x2a' * recordlen

        for fld in self.fields:
            v = self.r[fld.name]
            rawval = ""
            if fld.type == "C":
                rawval = v
            elif fld.type == "D":
                if v is None:
                    rawval = ' ' * fld.len
                else:
                    rawval = date2ccyymmdd(v)
            elif fld.type == "F":
                if v is None:
                    rawval = ' ' * fld.len
                else:
                    rawval = ("%f" % v)[:fld.len]
            elif fld.type == "L":
                rawval = v
            elif fld.type == "M":
                # TODO
                rawval = v
            elif fld.type == "N":
                if v is None:
                    rawval = ' ' * fld.len
                elif fld.decimal == 0:
                    rawval = "%d" % v
                else:
                    i = "%d" % int(v)
                    d = ("%f" % (v - int(v)))[2:fld.decimal + 2]
                    rawval = ("%s.%s" % (i,d))[:fld.len]
                
                if len(rawval) < fld.len: 
                    rawval = ' ' * (fld.len - len(rawval)) + rawval
                if len(rawval) > fld.len: rawval = rawval[:fld.len]
#                print "[%s]" % rawval
            else:
                assert False, "invalid field type"

            assert len(rawval) == fld.len

            rawtext = rawtext[:fld.offset] + rawval + \
                    rawtext[fld.offset + fld.len:]

        assert len(rawtext) == recordlen
        return rawtext

    def toDict(self):
        return self.r.copy()

    def __getitem__(self, key):
        return self.r[key.upper()]

    def __setitem__(self, key, value):
        key = key.upper()
        # type checking, make sure value is of right type and length
        fld = None

        for f in self.fields:
            if f.name == key: 
                fld = f
                break
        if not fld:
            raise ValueError("bad field name")

        if fld.type == "C":
            sval = str(value)
            if len(sval) > fld.len:
                raise ValueError("value too long")
            if len(value) < fld.len:
                value += ' ' * (fld.len - len(value))
        elif fld.type == "D":
            # don't do anything with sval... just make sure it works
            sval = value.strftime("%Y%m%d")
        elif fld.type in "FN":
            if value is not None:
                # make sure that the argument is a valid number
                sval = "%f" % value

                # check that the value is in bounds
                if fld.decimal:
                    toobig = 10 ** (fld.len - fld.decimal - 1)
                    toosmall = - ( 10 ** (fld.len - fld.decimal - 2) )
                else:
                    toobig = 10 ** fld.len
                    toosmall = - ( 10 ** (fld.len - 1) )
                if value >= toobig or value <= toosmall:
                    raise ValueError("Numeric value out of bounds")
        elif fld.type == "L":
            if len(value) != 1 or value not in "TF ":
                raise ValueError("invalid logical value")
        elif fld.type == "M":
            raise NotImplementedError
        else: assert False, "invalid field type"
            
        self.r[key] = value
        self.dirty = True

    def prettyPrint(self):
        if not self.fields:
            print "EOF"
        else:
            for fld in self.fields:
                print "%s: [%s]" % (fld.name, str(self.r[fld.name]))

class dbf:
    def __init__(self, filename):
        self.f = None
        self.fields = []
        self.version = None
        self.db4memo = None
        self.anymemo = None
        self.sqltable = None
        self.update_year = None
        self.update_month = None
        self.update_day = None
        self.numrecords = None
        self.headersize = None
        self.recordsize = None
        self.mdxff = None
        self.__eof = None
        self.nrecs = 0
        self.position = -1
        self.r = None

        self.open(filename)
        
    def open(self, filename):
        """If a current file is open, closes it.  Tries to open specified
        filename as a dBase IV 2.0 file
        """
        
        if self.f is not None:
            self.close()

        self.f = None
        f = file(filename, "rb+")
        self.f = f
        
        header = f.read(32)

        magic, \
        self.update_year, \
        self.update_month, \
        self.update_day, \
        self.numrecords, \
        self.headersize, \
        self.recordsize = \
                struct.unpack("BBBBIHH20x", header)

        # check dbf magic
        self.version = magic & 0x3
        self.db4memo = (magic & 0x4 != 0)
        self.anymemo = (magic & 0x80 != 0)
        self.sqltable = (magic & 0x70 != 0)

        if( self.version != 0x3 ):
            raise ValueError("does not appear to be a dBase IV 2.0 file")

        self.update_year += 1900

        # read in the field descriptor array
        self.numFields = (self.headersize - 33) / 32

        self.fields = []
        offset = 1
        for i in range(self.numFields):
            rawtext = f.read(32)
            newfield = field( rawtext, offset )
            self.fields.append( newfield )
            offset += newfield.len

        ft = f.read(1)
        if ft != "\x0D":
            raise ValueError("invalid Field terminator [%s]") % hex(ord(ft))
        #f.read(2)

        checksum = 0
        for fld in self.fields:
            checksum += fld.len

        # size of a record should be the sum of the field lengths plus one byte
        # that marks whether the record is deleted or not
        if checksum != self.recordsize - 1:
            raise ValueError("sum of field lengths = %d, recordsize = %d" % \
                    (checksum, self.recordsize))

        self.__eof = record(None,None)

        # calculate how many records there are in this dbf
        self.f.seek(0, 2)
        self.nrecs = (self.f.tell() - self.headersize) / self.recordsize

        self.f.seek(self.headersize)

        self.position = -1
        self.__readRecord()

    def __readRecord(self):
        rawtext = self.f.read(self.recordsize)
        if( len(rawtext) == 1):
            assert rawtext == "\x1a"
            self.r = self.__eof
            self.f.seek(-1, 1)
            self.position = -1
            return 
        self.r = record(self.fields, rawtext)
        self.f.seek(-self.recordsize, 1)

        self.position = (self.f.tell() - self.headersize) / self.recordsize

    def info(self):
        s = "last update: %s %s, %s\n" % ( self.update_month, self.update_day,
                self.update_year)
        s += "records: %s\n" % self.numrecords
        s += "header size: %s\n" % self.headersize
        s += "record size: %s\n" % self.recordsize
        s += "fields: %s\n" % self.numFields
        for field in self.fields:
            s += "    %s\n" % field.info()
        return s


    def close(self):
        """Flushes the current record to disk and closes the file
        """
        if self.f is not None:
            self.flush_record()
            self.f.close()
            self.f = None
            self.r = None
        else:
            raise ValueError("no files are open")

    def eof(self):
        """True if the current position is at the end of the file, and there is
        no valid record to access
        """
        return (self.r == self.__eof)

    def skip(self, amount = 1):
        """flushes the current record to disk, and skips the specified number
        of records.  Can be either positive or negative.  If the end of file
        is reached, eof() will return true.  If the beginning of the file is
        reached, will remain at the first record
        """
        self.flush_record()

        if amount > 0:
            for i in range(amount):
                self.f.seek(self.recordsize, 1)
        else:
            for i in range(-amount):
                if self.f.tell() != self.headersize:
                    self.f.seek(-self.recordsize, 1)
        self.__readRecord()

    def go(self, recordno):
        """flushes the current record to disk and seeks to the specified
        record.  If the record is out of bounds, raises a ValueError."""
        self.flush_record()

        if recordno < 0:
            raise ValueError("Record out of range")
        self.f.seek(self.headersize + recordno * self.recordsize)
        # if we've seeked to the end of the file, then seek to the last
        # record
        t = self.f.read(1)
        if len(t) == 0:
            self.f.seek(-1,2)
            self.__readRecord()
            raise ValueError("Record out of range")
        else:
            self.f.seek(-1,1)
        self.__readRecord()

    def gobottom(self):
        """flushes the current record to disk and seeks to the very last
        record""" 
        self.flush_record()

        self.f.seek(-(self.recordsize + 1), 2)
        if self.f.tell() < self.headersize:
            self.f.seek(self.headersize)
        self.__readRecord()

    def delete(self):
        """marks a record for deletion.  marked entries can be permanently 
        removed by a call to pack()
        """
        if self.eof(): raise ValueError("EOF")
        if not self.r.deleted:
            self.r.deleted = True
            self.f.write("\x2a")
            self.f.seek(-1,1)

    def recall(self):
        """recalls (undeletes) a record marked for deletion.  no effect if
        record is not marked for deletion
        """
        if self.eof(): raise ValueError("EOF")
        if self.r.deleted:
            self.r.deleted = False
            self.f.write("\x2a")
            self.f.seek(-1,1)

    def pack(self):
        """Flushes the .DBF to disk, permanently erasing records marked for
        deletion.  Seeks to the first record when done.
        """
        self.flush_record()

        self.f.seek(self.headersize, 0)

        lastrecord = 0
        deleted = 0

        for i in range(self.numrecords):
            self.f.seek(self.headersize + i * self.recordsize, 0)

            text = self.f.read(1)
            self.f.seek(-1, 1)

            if text == "\x20": 
                if lastrecord != i:
                    # pack this record, overwriting the last deleted record
                    rawtext = self.f.read(self.recordsize)
                    assert len(rawtext) == self.recordsize
                    self.f.seek(self.headersize + lastrecord * \
                            self.recordsize, 0)
                    self.f.write(rawtext)

                lastrecord += 1
            else:
                deleted += 1

        if deleted > 0:
            # at least one record was deleted and packed away.  now write the
            # EOF byte and truncate the file size
            self.f.write("\x1a")
            self.f.truncate()

            self.numrecords -= deleted

            # now write the number of records
            self.f.seek(4,0)
            self.f.write(struct.pack("i", self.numrecords))

        self.go(0)

    def flush_record(self):
        """flushes the current record to disk if it has been modified.
        Otherwise, no effect"""

        if self.eof(): return

        if self.r.dirty:
            self.f.write(self.r.get_rawtext())
            self.f.seek(-1 * self.recordsize, 1)

    def append_blank(self):
        """appends a blank record to the end of the file, and seeks to it.  
        Flushes the current record first."""
        self.flush_record()
        self.f.seek(-1, 2)
        # the new record
        data = "\x20" + " " * (self.recordsize - 1)
        # the EOF byte
        data += "\x1a"
        self.f.write(data)
        self.numrecords += 1

        # write the new number of records
        self.f.seek(4,0)
        self.f.write(struct.pack("i", self.numrecords))

        self.f.seek(-1 * (self.recordsize + 1), 2)
        self.__readRecord()

    def __getitem__(self, key):
        """gets the value of a field in the current record"""
        if self.r != self.__eof:
            return self.r[key]
        else:
            raise ValueError("EOF")

    def __setitem__(self, key, value):
        """sets the value of a field in the current record"""
        if self.eof():
            raise ValueError("EOF")
        
        self.r[key] = value

def create( fname, field_descriptors ):
    numfields = len(field_descriptors)
    
    magic = 0x3
    now = datetime.datetime.now()
    uyear = now.year - 1900
    umonth = now.month
    uday = now.day
    numrecords = 0
    headersize = 32 * numfields + 33
    recordsize = 1

    fds = []
    
    for f in field_descriptors:
        name, type, width, dec, index = f
        recordsize += width

        if len(name) > 11:
            raise ValueError("Name %s too long" % name)
        if len(type) != 1 or type not in "CDFLN":  # TODO add Memo (M)
            raise ValueError("Invalid field type")
        if dec > width + 1 or width < 1 or dec < 0:
            raise ValueError("Invalid width/decimal")
        if index:
            raise NotImplementedError("Index not yet supported")
        if type == Character and dec != 0:
            raise ValueError("Invalid decimal for character field")
        if type == Date and (dec != 0 or width != 8):
            raise ValueError("Width/Decimal must be 8,0 for Date")

        res1 = "\x41\x02\x87\x13" # XXX ???
        res1 = "\0" * 4
        res2 = "\0\0"
        wkid = "\x01"
        res3 = "\0" * 10
        mdx = "\0"

        fstr = name + "\0" * (11-len(name)) + type + res1 + \
                chr(width) + chr(dec) + res2 + wkid + res3 + mdx
        #print binascii.hexlify(fstr), len(fstr)
        assert len(fstr) == 32
        fds.append(fstr)

    f = file(fname,"wb+")
    header = struct.pack("BBBBIHH20x", magic, uyear, umonth, uday, numrecords,
            headersize, recordsize)
    f.write(header)
    for fstr in fds:
        f.write(fstr)
    f.write("\x0D\x1A")
    f.close()

    return dbf(fname)
        
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print "must specify dbf file"
        sys.exit(1)

    a = dbf(sys.argv[1])
    print a.info()

    try:
        a.go(8)
    except ValueError:
        pass
    print "eof: %s" % a.eof()
    a.go(1)
    print "eof: %s" % a.eof()
    a.go(0)
    while not a.eof():
        print "============= %d / %d" % (a.position, a.nrecs)
        print "deleted: %s" % str(a.r.deleted)
        a.r.prettyPrint()
        print "[%s]" % a.r.get_rawtext()
        a.skip(1)
    a.skip(-8)
    print "============= %d / %d" % (a.position, a.nrecs)
    print "deleted: %s" % str(a.r.deleted)
    a.r.prettyPrint()

# $Log: dbf.py,v $
# Revision 1.4  2006/07/14 22:30:16  albert
# month/day swap
#
# Revision 1.3  2006/07/14 16:43:10  albert
# *** empty log message ***
#
# Revision 1.2  2006/07/09 16:40:14  albert
# *** empty log message ***
#
# Revision 1.4  2006/05/06 18:40:48  albert
# create
#
# Revision 1.3  2005/09/03 20:03:03  albert
# open dbf files in binary mode
#
# Revision 1.2  2005/06/26 18:07:28  albert
# *** empty log message ***
#
# Revision 1.1  2005/06/25 05:21:49  albert
# *** empty log message ***
#
