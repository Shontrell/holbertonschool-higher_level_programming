#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    import json
    with open(filename) as x:
        my_str = x.read()
    return json.loads(my_str)
