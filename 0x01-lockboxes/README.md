# Lockboxes Solver

The `Lockboxes Solver` is a Python program designed to determine if it is possible to unlock every box in a series of sequentially numbered lockboxes. Each box may contain keys to other boxes, and the objective is to discover whether all boxes can be unlocked starting from the initially unlocked box (box 0).

## Description

This utility utilizes a Breadth-First Search (BFS) algorithm to navigate through a list of boxes, where each box contains zero or more keys to other boxes. The function `canUnlockAll(boxes)` accepts a list of lists, with each sublist representing the keys contained within a corresponding box.

## Installation

This module does not require any external libraries beyond Python's standard library. It is compatible with Python 3.6 or newer. To set up, simply clone this repository to your local machine:

```bash
git clone https://github.com/R-HYTE/alx-interview.git
cd alx-interview/0x01-lockboxes
