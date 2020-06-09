#!/usr/bin/python3
"""
class Base unittesting
"""


import unittest
import pep8


class test_Base(unittest.TestCase):
    """
    Testing Base
    """
    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['file1.py', 'file2.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_idset(self):
        """
        Testing to see if id is set
        """
        tb = Base()
        self.assertEqual(tb.id, 1)
        tb2 = Base(2)
        self.assertEqual(tb2.id, 2)

    def test_to_json_string(self):
        """
        Testing to_json_string method
        """
        testlist = [{'id': 2, 'x': 5, 'y': 6}]
        self.assertCountEqual(Base.to_json_string(testlist),
                              '[{'id': 2, 'x': 5, 'y': 6}]')
