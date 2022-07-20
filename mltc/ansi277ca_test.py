import os
import unittest

import mltc.x12 as x12
import mltc.ansi277ca as ansi277ca

_DATA_DIR=os.path.join("test_data", "277ca")

def _get_test_files(group):
    bnames = os.listdir(os.path.join(_DATA_DIR, group))
    fnames = [ os.path.join(_DATA_DIR, group, bname) for bname in bnames ]
    return [ fname for fname in fnames if os.path.isfile(fname) ]

class TestAnsi277CA(unittest.TestCase):
    def test_medicare(self):
        for fname in _get_test_files("medicare"):
            file_obj = open(fname)
            a277cadoc = ansi277ca.Ansi277caDocument(file_obj)

    def test_uhc(self):
        for fname in _get_test_files("uhc"):
            file_obj = open(fname)
            a277cadoc = ansi277ca.Ansi277caDocument(file_obj)

    def test_malformed(self):
        for fname in _get_test_files("malformed"):
            file_obj = open(fname)
            self.assertRaises(x12.X12ParseError,
                    ansi277ca.parse_x12_doc, file_obj)

if __name__ == "__main__":
    unittest.main()
