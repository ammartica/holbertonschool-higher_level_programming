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
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON string json_string"""
        if not json_string or json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes JSON string of list_objs to a file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary()
                                            for i in list_objs]))

    @classmethod
    def create(cls, **dictionary):
        """returns instance with attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        file_name = cls.__name__ + ".json"
        ls = []
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                ls2 = cls.from_json_string(f.read())
                for i in ls2:
                    ls.append(cls.create(**i))
        except:
            pass
        return ls
