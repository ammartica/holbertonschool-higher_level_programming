#!/usr/bin/python3
"""Contains class named MyList"""


class MyList(list):
    """child class named MyList that inherits from list class"""
    def __init__(self):
        """initializes object"""
        super().__init__()

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
