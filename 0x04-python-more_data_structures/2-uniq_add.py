#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return
    newl = list(set(my_list))
    To_tal = 0
    for i in newl:
        To_tal = To_tal + i
    return To_tal
