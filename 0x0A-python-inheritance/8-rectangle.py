#!/usr/bin/python3
"""Defines a subclass named Rectangle that
inherits from BaseGeometry class"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """child class represents Rectangle"""
    def __init__(self, width, height):
        """initialize attributes of rectangle object"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

