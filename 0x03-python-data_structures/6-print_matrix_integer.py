#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        
        for integer in range(len(row)):
            print("{:d}" .format(row[integer]), end="")

            # add a space if next int is not last
            if integer < len(row) - 1:
                print(" ", end="")

        print("")  # new line print
