#!/usr/bin/python3
"""Module contains inherits_from function"""


def inherits_from(obj, a_class):
    """returns bool if object is instance of class from other class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
