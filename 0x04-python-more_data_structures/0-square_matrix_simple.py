#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """ this function returns a new matrix where;
    each value must be a square value of the input and the
    initial matrix cannot be modified. """
    return [[elem ** 2 for elem in row] for row in matrix]
