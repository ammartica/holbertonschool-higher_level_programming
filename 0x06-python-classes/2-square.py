#!/usr/bin/python3
"""Defines a class named Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Method that initializes square

        Args:
            size (int): size of a square

        Returns:
            Nothing
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
