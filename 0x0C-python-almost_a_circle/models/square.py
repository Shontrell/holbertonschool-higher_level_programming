#!/usr/bin/python3
"""
class Square that inherits from class Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Args:
        size: size of the square
        x: position
        y: position
        id: id
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Return:
            getting the size
        """
        return (self.width)

    @size.setter
    def size(self, size):
        """setting width and height to size"""
        self.width = size
        self.height = size

    def __str__(self):
        """
        Return:
            [Square] (<id>) <x>/<y> - <size>
        """
        args = [self.id, self.x, self.y, self.width]
        return ("[Square] ({}) {}/{} - {}".format(*args))

    def update(self, *args, **kwargs):
        """ update: updates the instance attributes"""
        arglist = ['id', 'width', 'x', 'y']
        if args is not None and len(args) != 0:
            a = 0
            for arg in args:
                if a < 4:
                    setattr(self, arglist[a], arg)
                    a += 1
        else:
            for key, value in kwargs.items():
                for i in arglist:
                    if i == key:
                        setattr(self, key, value)
                if key == 'size':
                    setattr(self, 'width', value)

    def to_dictionary(self):
        """
        Return:
            the dictionary represntation of a Square
        """
        return ({'id': self.id, 'size': self.width, 'x': self.x, 'y': self.y})
