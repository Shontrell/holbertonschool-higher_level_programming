#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    else:
        matrix2 = []
        for i in matrix:
            sqmatrix = list(map((lambda x: x * x), i))
            matrix2.append(sqmatrix)
        return (matrix2)
