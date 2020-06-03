#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """adding area and printing rectangle width and height"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return(self.__width * self.__height)

    def __str__(self):
        str1 = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return (str1)