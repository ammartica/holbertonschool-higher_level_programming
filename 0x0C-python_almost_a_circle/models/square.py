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
