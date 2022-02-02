#!/usr/bin/python3
"""Defines a class named Student"""

class Student:
    """Defines a Student"""

    def __init__(self, first_name, last_name, age):
        """Initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves dictionary representation of Student"""
        return self.__dict__
