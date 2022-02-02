#!/usr/bin/python3
"""
Contains the function append_write
"""


def append_write(filename="", text=""):
    """returns total chars appended"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
