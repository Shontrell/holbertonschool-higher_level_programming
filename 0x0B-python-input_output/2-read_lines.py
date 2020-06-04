#!/usr/bin/python3
"""a function that reads n lines of a text file and prints it to stdout"""


def read_lines(filename="", nb_lines=0):
    """
    Args:
        filename: name of file
        nb_lines: number of lines to be read
    """
    lc = 0
    with open(filename) as x:
        if nb_lines <= 0:
            for line in x:
                print(line, end="")
        else:
            for y in range(nb_lines):
                print(x.readline(), end="")
