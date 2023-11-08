#!/usr/bin/python3
# 0-square_matrix_simple.py


def square_matrix_simple(matrix=[]):
    """
    Calculate the square of each integer in a matrix.

    :param matrix: A list of lists representing a matrix.
    :type matrix: list of lists of integers
    :return: A new matrix with the square of each integer.
    :rtype: list of lists of integers
    """
    return ([list(map(lambda x: x * x, row)) for row in matrix])
