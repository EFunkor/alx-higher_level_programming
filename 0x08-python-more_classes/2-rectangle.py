#!/usr/bin/python3

"""
A rectangle class that defines a rectangle with private isnatmce
atrributes
"""


class Rectangle:

    """
    initiatilization of the an object instance
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    Definition of an object instance height
    """
    @property
    def height(self):
        """
        return the height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """
    Definition of an object instance width of the rectangle
    """
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """
    computing an object instance area of tge rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
    function definition for the perimeter of the rectangle
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
