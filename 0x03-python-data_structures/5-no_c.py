#!/usr/bin/python3
def no_c(my_string):
    Z = ""  # An empty string to store Z
    for char in my_string:  # iterate through each character in my_string
        if char != 'c' and char != 'C':  # to check for c and C
            Z += char  # if no c or C, add char to Z
    return Z
