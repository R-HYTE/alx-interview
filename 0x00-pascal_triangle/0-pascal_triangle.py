#!/usr/bin/python3
"""

This module defines the `pascal_triangle` function that
generates Pascal's triangle up to a specified number of rows.

"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows of Pascal's triangle to generate.

    Returns:
        List[List[int]]: A list of lists, where each sublist
            represents a row in Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    current_row = [1]
    for _ in range(n):
        triangle.append(current_row)
        next_row = [1]
        for j in range(1, len(current_row)):
            next_row.append(current_row[j - 1] + current_row[j])
        next_row.append(1)
        current_row = next_row

    return triangle
