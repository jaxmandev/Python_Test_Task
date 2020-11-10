# import the class with the functionality to test
from divby0 import Divby0

# import after "pip download unittest/pytest"
import unittest
import pytest

# inherit testing capabilities
class Divby0_test(unittest.TestCase):

    # create object of the class Divby0()
    test1 = Divby0()
    
    # method must be called test_... to function
    def test_divby0(self):
        self.assertEqual(self.test1.divby0(4, 2), True)
        self.assertEqual(self.test1.divby0(-100, 10), True)
        self.assertEqual(self.test1.divby0(50, 25), True)
        
# if we run this module directly, run the code in the conditional
# unittest.main() will run the tests

if __name__ == "__main__":
    unittest.main()
