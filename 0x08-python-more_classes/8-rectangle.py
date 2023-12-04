#!/usr/bin/python3

"""
A class  rectangle that defines a rectangle
"""


class Rectangle:
    """
    Instantiation of the number of instance and print_symbol
    """
    number_of_instances = 0
    print_symbol = "#"

    """
    Initialization of an object instance
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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
        return '\n'.join([str(self.print_symbol) * self.__width] *
                         self.__height)

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
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    """
    applying the static method that returns the biggest rectangle
    based on the area.
    """
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Definition of an object instance bigger_or_equal
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
