#!/usr/bin/python3
"""a function that returns the number of lines of a text file"""


def number_of_lines(filename=""):
    lc = 0
    with open(filename) as x:
        for line in x:
            lc += 1
    return (lc)
