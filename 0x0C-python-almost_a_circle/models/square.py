#!/usr/bin/python3
"""child class Square of Rectangle"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """subclass Square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.size)

    @property
    def size(self):
        """getter for private instance attribute size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for private instance attribute size"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns args to attributes"""
        if args and args is not None:
            for i, a in enumerate(args):
                if i == 0:
                    self.id = args[0]
                elif i == 1:
                    self.size = args[1]
                elif i == 2:
                    self.x = args[2]
                elif i == 3:
                    self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns dict representation of a Square"""
        return {'id': self.id, 'size': self.size, 'x': self.x,
                'y': self.y}
