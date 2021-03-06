#!/usr/bin/python3
"""
class Square unittesting
"""


import unittest
import pep8


class test_Square(unittest.TestCase):
    """
    Testing Square
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
