#!/usr/bin/python3
"""class Square that inherits from Rectangle"""



Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Instantiation with size
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        str1 = "[Square] " + str(self.__size) + "/" + str(self.__size)
        return (str1)
