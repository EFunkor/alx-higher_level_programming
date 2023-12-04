#!/usr/bin/python3
"""
Implementation of a rectangle class that defines a rectangle and has
a private instamce attribute

"""


class Rectangle:
    """
    A class that defines a rectangle
    """

    def __init__(self, width=0, height=0):

        """
        instantiation with height.
        """
        self.height = height
        """
        instantiation with width
        """
        self.width = width

    """
    An object instance that defines the height of the rectangle
    """
    @property
    def height(self):

        """
        Returns: The size of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
