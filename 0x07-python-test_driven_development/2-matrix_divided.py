#!/usr/bin/python3
"""Module named 2-matrix_divided

    Contains function named matrix_divided(matrix, div)
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix
    """
    commonError = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list:
        raise TypeError(commonError)
    size = len(matrix[0])
    for i in matrix:
        if type(i) is not list:
            raise TypeError(commonError)
        if size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if type(j) not in [int, float]:
                raise TypeError(commonError)
    return [[round(j / div, 2) for j in i] for i in matrix]
