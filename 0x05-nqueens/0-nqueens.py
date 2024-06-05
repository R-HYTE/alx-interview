#!/usr/bin/env python3
"""
N Queens Puzzle Solver

This module provides a solution to the N Queens puzzle, which is the challenge
of placing N non-attacking queens on an N×N chessboard. It uses a backtracking
algorithm to find all possible solutions.

Usage:
    python nqueens.py N

Where:
    N must be an integer greater than or equal to 4.

If the user calls the program with the wrong number of arguments, prints:
    Usage: nqueens N

If N is not an integer, prints:
    N must be a number

If N is smaller than 4, prints:
    N must be at least 4

The program prints every possible solution to the problem,
one solution per line.
Each solution is represented as a list of pairs [i, j], where i and j are the
row and column indices of a queen on the board.
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col].

    Args:
        board (list): The chessboard.
        row (int): The row index.
        col (int): The column index.

    Returns:
        bool: True if it's safe to place the queen, False otherwise.
    """
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, solutions):
    """
    Use backtracking to place queens on the board.

    Args:
        board (list): The chessboard.
        col (int): The current column index.
        solutions (list): The list to store all the solutions.
    """
    if col >= len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            solve_nqueens_util(board, col + 1, solutions)
            board[i][col] = 0


def solve_nqueens(N):
    """
    Initialize the board and find all solutions.

    Args:
        N (int): The size of the chessboard.

    Returns:
        list: A list of all possible solutions.
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, solutions)
    return solutions


def main():
    """
    Validate input and run the solver.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
