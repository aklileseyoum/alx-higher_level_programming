#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for i in range(len(matrix)):
       for row in matrix:
           new.append(row[i]**2)
    return new
