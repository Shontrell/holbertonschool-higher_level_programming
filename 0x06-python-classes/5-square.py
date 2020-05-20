#!/usr/bin/python3
"""defining class Square"""


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
        self.__size = size

    @property
    def size(self):
        """
        retrieving size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        setting size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def area(self):
        """
        public instance method:
            area()
        Return:
            current square area
        """
        return ((self.__size) * (self.__size))

    def my_print(self):
        """
        public instance method:
            my_print()
        Return:
            square with the character #
        """
        if self.__size == 0:
            print("")
        else:
            for x in range(self.__size):
                for y in range(self.__size):
                    print("#", end="")
                print("")
