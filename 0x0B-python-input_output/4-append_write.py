#!/usr/bin/python3
"""
a function that appends a string at the end of a text \
file and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Args:
        filename: name of file
        text: string to be appended at end of text file
    Return:
        the number of characters added
    """
    chnumb = 0
    with open(filename, 'a') as x:
        chnumb = x.write(text)
    return (chnumb)
