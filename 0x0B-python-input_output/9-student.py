#!/usr/bin/python3
"""
A Module that defines a class Student

"""


class Student:
    """
    Instantiating with the required public instance attributes.

    """

    def __init__(self, first_name, last_name, age):

        """
        A method that initializes the attributes

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that retrieves a  dictinary representation
        of an instance
        """
        return self.__dict__.copy()
