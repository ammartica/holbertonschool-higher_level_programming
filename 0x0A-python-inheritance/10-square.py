#!/usr/bin/python3
"""Subclass named Square inherits from BaseGeometry and Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents a square"""
    def __init__(self, size):
        """instantiation of Square class"""
        self.__size = size
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2
