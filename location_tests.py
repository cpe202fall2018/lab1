# CPE 202 Location Class Test Cases, Lab 1

import unittest
from location import *

class TestLocation(unittest.TestCase):

    def test_repr(self):
        loc = Location('SLO', 35.3, -120.7)
        str1 = "Location('SLO', 35.3, -120.7)"
        str2 = "Location(SLO, 35.3, -120.7)"
        res = repr(loc)
        #print(res)
        self.assertTrue(res == str1 or res == str2)
    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
