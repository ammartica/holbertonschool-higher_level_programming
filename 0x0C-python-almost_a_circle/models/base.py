#!/usr/bin/python3
"""Contains a class named Base"""

import json


class Base:
    """Class named Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialize Base class"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries"""
        if not list_dictionaries or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)
"""
    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string of list_objs to a file"""
        if list_objs is None:
            ls = []
        file_name = cls.__name__ + ".jason"
        with open(file_name, "w", encoding="utf-8") as f:"""
