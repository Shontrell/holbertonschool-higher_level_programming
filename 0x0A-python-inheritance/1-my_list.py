#!/usr/bin/python3
"""a class Mylist that inherits from list"""


class MyList(list):
    def print_sorted(self):
        """
        Args:
            self: variable for the object
        """
        cl = self.copy()
        cl.sort()
        print(cl)
