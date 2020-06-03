#!/usr/bin/python3
"""
Creates class Student and addes parameter to public method: def to_json()
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
