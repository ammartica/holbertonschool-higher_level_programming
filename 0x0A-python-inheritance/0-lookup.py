#!/usr/bin/python3
"""Module contains lookup() function"""


def lookup(obj):
    """returns list of available attr and methods of an object"""
    return dir(obj)
