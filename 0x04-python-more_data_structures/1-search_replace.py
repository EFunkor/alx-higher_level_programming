#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # To create a new list storing the modified elements
    new_list = []

    for integer in my_list:
        if integer == search:
            new_list.append(replace)
        else:
            new_list.append(integer)

    return new_list
