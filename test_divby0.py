from divby0 import Divby0
import unittest
import pytest

class Divby0_test(unittest.TestCase):

    test1 = Divby0()

    def test_divby0(self):
        self.assertEqual(self.test1.divby0(4, 2), True)
        self.assertEqual(self.test1.divby0(-100, 10), True)
        self.assertEqual(self.test1.divby0(50, 25), True)
if __name__ == "__main__":
    unittest.main()