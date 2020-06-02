#!/usr/bin/python3
"""
a function that returns the list of available attributes \
and methods of an object
"""


def lookup(obj):
    """
    Args:
        obj: object
    Return:
        a list object
    """
    return (dir(obj))
