# Rotate 2D Matrix

This project provides a function `rotate_2d_matrix(matrix)` to rotate a 2D matrix 90 degrees clockwise in-place.

## Functionality

The `rotate_2d_matrix` function takes a 2D matrix represented as a list of lists of integers (`matrix`) and rotates it 90 degrees clockwise. The rotation is performed in-place, meaning the function modifies the original matrix directly without creating a new one.

### Input

- `matrix` (List[List[int]]): A 2D matrix where each sublist represents a row of the matrix. The matrix must be square (i.e., number of rows equals number of columns).

### Output

- None: The function modifies the matrix in-place. After calling `rotate_2d_matrix(matrix)`, the matrix will be rotated 90 degrees clockwise.

## Algorithm

The rotation algorithm consists of two main steps:

1. **Transpose the Matrix**: Swap elements across the diagonal (transpose operation).
   - For each element at position `(i, j)`, swap it with the element at position `(j, i)`.

2. **Reverse Each Row**: After transposing the matrix, reverse each row to achieve the 90-degree clockwise rotation.
   - Reverse each sublist (row) of the matrix.

### Example

Given the matrix:

```
[
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
```

After rotating 90 degrees clockwise, the matrix becomes:

```
[
[7, 4, 1],
[8, 5, 2],
[9, 6, 3]
]
```

## Usage

To use the `rotate_2d_matrix` function, import it into your Python script and call it with your matrix as follows:

```python
from rotate_2d_matrix import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)  # Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
```
