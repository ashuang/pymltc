import os
import unittest

import medltc.x12 as x12
import medltc.ansi277ca as ansi277ca

_DATA_DIR=os.path.join("test_data", "277ca")

def _get_test_files(group):
    bnames = os.listdir(os.path.join(_DATA_DIR, group))
    return [ os.path.join(_DATA_DIR, group, bname) for bname in bnames ]

class TestAnsi277CA(unittest.TestCase):
    def test_medicare(self):
        for fname in _get_test_files("medicare"):
            file_obj = open(fname)
            a277cax12 = ansi277ca.parse_277ca(file_obj)
            a277cadoc = ansi277ca.Ansi277caDocument(a277cax12)

    def test_malformed(self):
        for fname in _get_test_files("malformed"):
            file_obj = open(fname)
            self.assertRaises(x12.X12ParseError,
                    ansi277ca.parse_277ca, file_obj)

if __name__ == "__main__":
    unittest.main()
