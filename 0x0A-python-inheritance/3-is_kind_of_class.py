#!/usr/bin/python3
"""Module contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """returns bool if object is instance of class or child class"""
    return (isinstance(obj, a_class))
