# N Queens Puzzle Solver

The N Queens puzzle is a classic algorithmic problem that challenges you to place N non-attacking queens on an N×N chessboard. This program solves the N Queens problem using a backtracking algorithm and prints all possible solutions.

## How the Algorithm Works

### 1. Backtracking Approach

The algorithm uses backtracking to find all possible solutions to the N Queens problem. Backtracking is a general algorithmic technique that incrementally builds candidates for the solution and abandons a candidate as soon as it determines that the candidate cannot possibly be completed to a valid solution.

### 2. Safe Placement Check

To place a queen safely on the board, the algorithm checks the following conditions:

- No other queens are placed in the same row.
- No other queens are placed in the same column.
- No other queens are placed in the same diagonal.

### 3. Recursive Solution

The algorithm places queens one by one in different columns, starting from the leftmost column. For each column, it tries placing the queen in all rows and checks if placing the queen in the current row is safe. If safe, it places the queen and recursively attempts to place the next queen in the next column. If placing the queen in any row leads to a solution, it returns true. If no row is safe in the current column, it backtracks by removing the queen from the current row and tries the next row.

### 4. Collecting Solutions

When the algorithm successfully places queens in all columns (i.e., a valid solution is found), it collects the positions of the queens and stores them in a list of solutions.

## Pseudocode

```python
function solve_nqueens(N):
    board = NxN grid initialized to 0
    solutions = empty list
    solve_nqueens_util(board, 0, solutions)
    return solutions

function solve_nqueens_util(board, col, solutions):
    if col >= N:
        add current board configuration to solutions
        return
    for each row in 0 to N-1:
        if is_safe(board, row, col):
            place queen at board[row][col]
            solve_nqueens_util(board, col + 1, solutions)
            remove queen from board[row][col]

function is_safe(board, row, col):
    for each cell in the left side of the row:
        if cell has a queen:
            return false
    for each cell in the upper left diagonal:
        if cell has a queen:
            return false
    for each cell in the lower left diagonal:
        if cell has a queen:
            return false
    return true
```
