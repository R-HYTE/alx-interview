#!/usr/bin/python3
"""
    This module has a function that unlocks boxes where each box
    has a set of keys that may unlock another box
"""


def canUnlockAll(boxes):
    """Method that determines if all the boxes can be opened
        Arg:
            boxes: Is a list of lists.
    """
    n = len(boxes)
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # First box is unlocked
    queue = [0]  # Queue initialized with the first box which is open

    while queue:
        current = queue.pop(0)  # Get current box
        for key in boxes[current]:  # Iterate over keys in the current box
            if key < n and not unlocked[key]:
                unlocked[key] = True  # Unlock the box
                queue.append(key)  # Add this box to queue for more exploration
    return all(unlocked)
