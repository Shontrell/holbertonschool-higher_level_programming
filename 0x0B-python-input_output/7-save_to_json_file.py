#!/usr/bin/python3
"""
a function that writes an Object to a text file, using a JSON representation
"""


def save_to_json_file(my_obj, filename):
    import json
    with open(filename, 'w') as x:
        obj = json.dumps(my_obj)
        x.write(obj)
