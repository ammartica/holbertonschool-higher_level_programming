#!/usr/bin/python3
"""Module named 4-print_square

    Contains function named print_square(size)
"""


def print_square(size):
    """
    Prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
