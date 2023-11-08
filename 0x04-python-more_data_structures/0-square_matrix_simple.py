#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    N_matrix = []
    for row in matrix:
        N_matrix.append(list(map(lambda x: x**2, row)))

    return N_matrix
