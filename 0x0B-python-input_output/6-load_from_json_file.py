#!/usr/bin/python3
"""
Importing the module json for use in a function that loads an object
from a JSON FILE

"""
import json


def load_from_json_file(filename):
    """
    A function that creates an object from a JSON file

    """
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
