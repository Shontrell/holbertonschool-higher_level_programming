#!/usr/bin/python3
"""
a function that creates an Object from a “JSON file”
"""


def load_from_json_file(filename):
    """
    Args:
        filename: name of file
    Return:
        an object from a JSON file
    """
    import json
    with open(filename) as x:
        my_str = x.read()
    return json.loads(my_str)
