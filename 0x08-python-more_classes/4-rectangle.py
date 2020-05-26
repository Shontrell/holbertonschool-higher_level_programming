#!/usr/bin/python3
"""
Creates a class Rectangle that defines a rectangle by width, height, area \
and perimeter
"""


class Rectangle:
    """
    Args:
        width: integer
        height: integer
    Raise:
        TypeError: width must be an integer
        TypeError: height must be an integer
        ValueError: width must be >= 0
        ValueError: height must be >= 0
    Return:
        area: (width * height)
        perimeter: (width * 2) + (height * 2)
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        return (self.__height)

    @property
    def width(self):
        return (self.__width)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return (0)
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ("")
        character = ""
        for x in range(self.height):
            for y in range(self.width):
                character = character + "#"
            if (x < self.height - 1):
                character = character + "\n"
        return (character)

    def __repr__(self):
        w = str(self.__width)
        h = str(self.__height)
        return "Rectangle(" + w + ", " + h + ")"
