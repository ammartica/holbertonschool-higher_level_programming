#!/usr/bin/python3
"""
Contains the function write_file
"""


def write_file(filename="", text=""):
    """returns total chars written"""
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
