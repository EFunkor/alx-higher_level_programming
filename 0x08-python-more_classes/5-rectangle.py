#!/usr/bin/python3

"""
A class  rectangle that defines a rectangle
"""


class Rectangle:

    """
    Initialization of an object instance
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """
    Definition of object instance height of the rectangle
    """
    @property
    def height(self):
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
    method definition for an object instance area of the rectangle
    """
    def area(self):
        return self.__width * self.__height

    """
    Definition of the object instance perimeter of the rectangle
    """
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    """
    function definition for printing the rectangle with #
    """
    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join(['#' * self.__width] * self.__height)

    """
    recreate a new instance using repr()
    """
    def __repr__(self):
        return f'Rectangle({self.__width}, {self.__height})'

    """
    condition to print a message when an instance of the rectangle
    is deleted.

    """
    def __del__(self):
        print("Bye rectangle...")
