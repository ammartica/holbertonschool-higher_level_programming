#!/usr/bin/python3
"""Subclass named Rectangle that inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class represents Rectangle"""
    def __init__(self, width, height):
        """initialize attributes of rectangle object"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """retrurns rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """returns rectangle description"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
