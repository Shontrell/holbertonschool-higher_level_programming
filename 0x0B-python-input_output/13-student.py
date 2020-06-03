#!/usr/bin/python3
"""
Creates class Student and adds public method: def reload_from_json()
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return (self.__dict__)
        else:
            newdict = {}
            orig = self.__dict__
            for x in attrs:
                for y in orig:
                    if (x == y):
                        newdict[x] = orig[x]
            return (newdict)

    def reload_from_json(self, json):
        orig = self.__dict__
        for x in json:
            for y in orig:
                if (x == y):
                    setattr(self, x, json[x])
