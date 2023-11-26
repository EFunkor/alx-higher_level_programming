#!/usr/bin/python3
"""

This module is composed by a function that prints a square with the character #

"""


def print_square(size):
    """
    Function that prints a square with the character #

    Prints the size of the square.

    """
    # check if size is an integer
    if not isinstance(size, int) or (isinstance(size, float) and
                                     size.is_integer() is False):
        raise TypeError("size must be an integer")
    # check if size is a non-integer negative
    if size < 0:
        raise ValueError("size must be >= 0")
    # print the square with the character #

    for i in range(size):
        print("#" * size)
