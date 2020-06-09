#!/usr/bin/python3
"""class Rectangle that inherits from Base"""


from models.base import Base


class Rectangle(Base):
    """
    Args:
        width: rectangle's width
        height: rectangle's height
        x: private instance attribute
        y: private instance attribute
        id: id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Return:
            getting the width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """setting the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value <= 0:
                raise ValueError("width must be > 0")
            else:
                self.__width = value

    @property
    def height(self):
        """
        Return:
            getting the height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """setting the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value <= 0:
                raise ValueError("height must be > 0")
            else:
                self.__height = value

    @property
    def x(self):
        """
        Return:
            getting private instance attribute x
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """setting private instance attribute x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        else:
            if value < 0:
                raise ValueError("x must be >= 0")
            else:
                self.__x = value

    @property
    def y(self):
        """
        Return:
            getting private instance attribute y
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """setting private instance attribute y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        else:
            if value < 0:
                raise ValueError("y must be >= 0")
            else:
                self.__y = value

    def area(self):
        """
        Return:
            area of the rectangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        Prints in stdout the Rectangle instance with the character #
        """
        print("\n" * self.__y, end="")
        for a in range(self.__height):
            for c in range(self.__x):
                print(" ", end="")
            for b in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Return:
            [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        args = (self.id, self.__x, self.__y, self.__width, self.__height)
        return("[Rectangle] ({}) {}/{} - {}/{}".format(*args))

    def update(self, *args, **kwargs):
        """
        assigns a key/value argument to attributes
        """
        arglist = ['id', 'width', 'height', 'x', 'y']
        a = 0
        if args is not None and len(args) != 0:
            for arg in args:
                if a < 5:
                    setattr(self, arglist[a], arg)
                    a += 1
        else:
            for key, value in kwargs.items():
                for i in arglist:
                    if (i == key):
                        setattr(self, key, value)

    def to_dictionary(self):
        """
        Return:
            the dictionary represntation of a Rectangle
        """
        return ({'id': self.id, 'width': self.__width, 'height': self.__height,
                 'x': self.__x, 'y': self.__y})
