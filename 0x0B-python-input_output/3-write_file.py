#!/usr/bin/python3
"""
a function that writes a string to a text file and returns \
the number of characters written
"""


def write_file(filename="", text=""):
    chnumb = 0
    with open(filename, 'w') as x:
        chnumb = x.write(text)
    return (chnumb)
