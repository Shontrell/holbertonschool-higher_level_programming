#!/usr/bin/python3
"""Defining class Square """


class Square:
    """private instance attribute: size"""
    def __init__(self, size=0):
        """
        Args:
            size: size of the square
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
