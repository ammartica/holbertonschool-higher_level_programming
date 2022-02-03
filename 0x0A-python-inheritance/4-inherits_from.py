#!/usr/bin/python3
"""
Module contains inherits_from function
"""


def inherits_from(obj, a_class):
    """returns bool if object is instance of a class that inherited from specified class"""
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
