#!/usr/bin/python3
"""a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name: first name string
        last_name: last name string
    Raise:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    Return:
        My name is <first name> <last name>
    """

    if type(first_name) is not str or first_name == None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name == None:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
