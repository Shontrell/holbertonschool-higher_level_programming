#!/usr/bin/python3
"""a function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """
    Args:
        matrix: list of lists of integers or floats
        div: must be a number (integer or float)
    Raise:
        TypeError: matrix must be a matrix (list of lists) of integers/floats
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero
    Return:
        a new matrix
    """
    newmatrix = []
    TE1 = "div must be a number"
    TE2 = "Each row of the matrix must have the same size"
    TE3 = "matrix must be a matrix (list of lists) of integers/floats"

    if type(div) is not int and type(div) is not float:
        raise TypeError(TE1)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError(TE2)
        nm2 = []
        for numbers in row:
            if type(numbers) is not int and type(numbers) is not float:
                raise TypeError(TE3)
            else:
                rounds = round(numbers / div, 2)
                nm2.append(rounds)
        newmatrix.append(nm2)

    return (newmatrix)
