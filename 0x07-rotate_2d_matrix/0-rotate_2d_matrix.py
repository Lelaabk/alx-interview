#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Rotate two dimension matrix 90 degrees clockwise"""
    n = len(matrix)
    for i in range(int(n / 2)):
        x = (n - i - 1)
        for j in range(i, x):
            y = (n - 1 - j)
            tmp = matrix[i][j]
            matrix[i][j] = matrix[y][i]
            matrix[y][i] = matrix[x][y]
            matrix[x][y] = matrix[j][x]
            matrix[j][x] = tmp
