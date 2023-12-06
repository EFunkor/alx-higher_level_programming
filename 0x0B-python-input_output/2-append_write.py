#!/usr/bin/python3

"""
A method to append a string to a text file (UTF8)
"""


def append_write(filename="", text=""):
    """
    A function that appends a string to a file
    Return: Number of characters added

    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
