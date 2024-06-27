#!/usr/bin/python3
""" This module provides a function to calculate the perimeter
    of an island described in a given grid.
"""


def island_perimeter(grid):
    """ Calculate the perimeter of the island in the grid.

    Parameters:
    grid (List[List[int]]): A 2D list of integers where 0 represents water
    and 1 represents land.

    Returns:
    int: The perimeter of the island.
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
