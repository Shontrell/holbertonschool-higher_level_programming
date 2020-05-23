#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_3listmax(self):
        """Test a 3 int list for max_integer"""
        self.assertEqual(max_integer([7, 8, 9]), 9)

if __name__ == "__main__":
    unittest.main()
