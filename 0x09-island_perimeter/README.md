# Island Perimeter Calculation

This project provides a function `island_perimeter(grid)` that calculates the perimeter of an island described in a given grid. The grid is a list of lists of integers where:

- `0` represents water.
- `1` represents land.

Each cell in the grid is square with a side length of 1. Cells are connected horizontally and vertically (not diagonally). The grid is rectangular and surrounded by water. There is only one island in the grid, and it does not have any lakes (water completely surrounded by land).

## Function Description

The function `island_perimeter(grid)` takes a 2D grid of integers as input and returns the perimeter of the island.

### Parameters

- `grid` (List[List[int]]): A list of lists of integers representing the grid.

### Returns

- `int`: The perimeter of the island.

## Implementation

The function iterates through each cell in the grid and checks if the cell is part of the land (`1`). For each land cell, it checks its four neighbors (up, down, left, right). If a neighboring cell is water (`0`) or is out of the grid bounds, it contributes to the perimeter count.
