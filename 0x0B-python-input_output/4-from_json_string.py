#!/usr/bin/python3
"""
Importing module json to parse a string
"""

import json


def from_json_string(my_str):
    """
    A function that imports the json module to parse a string and
    convert it to a python structure
    """
    return json.loads(my_str)
