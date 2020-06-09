#!/usr/bin/python3
"""Creating class Base"""


import json
import os


class Base:
    """
    Args:
        id: public instance attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return:
            the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return ("[]")
        else:
            return(json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        objlist = []
        obj = ""
        with open(filename, 'w') as x:
            if list_objs is None:
                obj = cls.to_json_string(objlist)
            else:
                for i in list_objs:
                    objlist.append(i.to_dictionary())
                obj = cls.to_json_string(objlist)
            x.write(obj)

    @staticmethod
    def from_json_string(json_string):
        """
        Return:
            the list of the JSON string representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """
        Return:
            an instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return (dummy)

    @classmethod
    def load_from_file(cls):
        """
        Return:
            a list of instances
        """
        filename = cls.__name__ + ".json"
        jsonstr = ""
        holdlist = []
        instlist = []
        if os.path.exists(filename) is False:
            return (holdlist)
        else:
            with open(filename, 'r') as x:
                jsonstr = x.read()
                holdlist = cls.from_json_string(jsonstr)
                for i in holdlist:
                    instlist.append(cls.create(**i))
            return(instlist)
