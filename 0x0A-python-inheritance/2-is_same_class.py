#!/usr/bin/python3
"""
a function that returns True if the object is exactly an \
instance of the specified class
"""


def is_same_class(obj, a_class):
    """
    Args:
        obj: object
        a_class: class
    Return:
        True if the object is exactly an instance of the \
        specified class, otherwise False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
