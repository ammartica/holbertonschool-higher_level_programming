#!/usr/bin/python3
"""Contains subclass named Rectangle"""


from models.base import Base


class Rectangle(Base):
    """subclass Rectangle inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter for private instance attribute width"""
        return self.__width

    @property
    def height(self):
        """getter for private instance attribute height"""
        return self.__height

    @property
    def x(self):
        """getter for private instance attribute x"""
        return self.__x

    @property
    def y(self):
        """getter for private instance attribute y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for private instance attribute width"""

    @height.setter
    def height(self, value):
        """setter for private instance attribute height"""

    @x.setter
    def x(self, value):
        """setter for private instance attribute x"""

    @y.setter
    def y(self, value):
        """setter for private instance attribute y"""
