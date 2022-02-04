#!/usr/bin/python3
"""Contains class named BaseGeometry"""


class BaseGeometry:
    """Class named BaseGeometry"""
    def area(self):
        """raises Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """raises error if value isn't integer"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
