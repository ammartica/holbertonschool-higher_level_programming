#!/usr/bin/python3
"""Module named 0-add integer

    Contains one function named add_integer(a, b=98)

"""


def add_integer(a, b=98):
    """
    Returns sum of arguments
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
