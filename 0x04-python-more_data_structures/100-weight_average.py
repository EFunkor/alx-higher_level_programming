#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 0

    num = 0
    deno_minator = 0
    for element in my_list:
        x, y = element
        num = num + x * y
        deno_minator = deno_minator + y
    return num/deno_minator
