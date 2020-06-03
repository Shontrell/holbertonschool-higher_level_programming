#!/usr/bin/python3
"""
a function that appends a string at the end of a text \
file and returns the number of characters added
"""


def append_write(filename="", text=""):
    chnumb = 0
    with open(filename, 'a') as x:
        chnumb = x.write(text)
    return (chnumb)
