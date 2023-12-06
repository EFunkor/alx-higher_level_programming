#!/usr/bin/python3
"""
Importing the json module to save an object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    A funtion that saves an object to a text file i json representation.

    """

    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
