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
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        ls = list_objs.copy()
        for i, v in enumerate(ls):
            ls[i] = ls[i].to_dictionary()
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(ls))

    @classmethod
    def create(cls, **dictionary):
        """returns instance with all attributes already set"""
