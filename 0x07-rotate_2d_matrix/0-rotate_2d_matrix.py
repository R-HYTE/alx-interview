#!/usr/bin/python3
""" This module provides a function to rotate a 2D matrix
    90 degrees clockwise in-place.
"""


def rotate_2d_matrix(matrix):
    """ Rotate a 2D matrix 90 degrees clockwise in-place.

    Args:
    - matrix (List[List[int]]): The 2D matrix to rotate.

    Returns:
    - None: The matrix is modified in-place.
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()
