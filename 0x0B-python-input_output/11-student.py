#!/usr/bin/python3
"""Defines a class named Student"""


class Student:
    """Defines a Student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of Student"""
        new_dict = {}
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for a in attrs:
            if type(a) is not str:
                return self.__dict__
            if a in self.__dict__:
                new_dict[a] = self.__dict__[a]
        return new_dict

    def reload_from_json(self, json):
        """replaces attributes of the student instance"""
        for key in json:
            setattr(self, key, json[key])
