#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """
    Args:
        filename: name of file
    """
    with open(filename) as x:
        for line in x:
            print(line, end="")
