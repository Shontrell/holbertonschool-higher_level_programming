#!/usr/bin/python3
def is_same_class(obj, a_class):
    """
    Args:
        obj: object to verify
        a_class: verify if this class is the class of obj
    Return:
        True if the object is exactly an instance of the \
        specified class, otherwise False
    """
    if type(obj) is a_class:
        return (True)
    else:
        return (False)
