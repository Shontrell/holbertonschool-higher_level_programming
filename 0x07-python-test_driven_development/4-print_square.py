#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """
    Args:
        size: the size length of the square
    Raise:
        TypeError: size must be an integer
        ValueError: size must be >= 0
    Return:
        a square with the character #
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        print(size * "#")
