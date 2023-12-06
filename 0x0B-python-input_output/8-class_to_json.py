#!/usr/bin/python3
"""
A module that returns a dictinary
"""


def class_to_json(obj):
    """
    A function that returns the dictionary description for JSON
    serialization of an object.

    """
    res = {}
    if hasattr(obj, "__dict__"):
        res = obj.__dict__.copy()
    return res
