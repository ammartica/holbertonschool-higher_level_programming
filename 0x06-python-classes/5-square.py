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

    def area(self):
        """Method that calculates the area of the square

        Returns:
            Current square area
        """

        return (self.__size) ** 2

    @property
    def size(self):
        """Method that retrieves size of square

        Returns:
            Size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        """Method that sets the size value

        Args:
            value (int): size of a square

        Returns:
            Nothing
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    def my_print(self):
        """Method that prints in stdout the square with the # char

        Returns:
            Nothing
        """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
