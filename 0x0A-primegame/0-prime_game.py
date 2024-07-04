#!/usr/bin/python3
"""
This module defines a function `isWinner` that determines the winner of a game
played between Maria and Ben. The game involves selecting prime numbers and
removing their multiples from a set of consecutive integers.
"""

def isWinner(x, nums):
    """
    Determines the winner after x rounds of the game.

    Parameters:
    x (int): Number of rounds
    nums (list of int): List containing the 'n' value for each round

    Returns:
    str: Name of the player that won the most rounds ("Maria" or "Ben")
         If no clear winner, returns None
    """
    if x <= 0 or nums is None or x != len(nums):
        return None

    ben = 0
    maria = 0
    max_n = max(nums)

    a = [1] * (max_n + 1)

    a[0], a[1] = 0, 0

    # Generating array of prime numbers using Sieve of Eratosthenes algo
    for i in range(2, max_n + 1):
        if a[i] == 1:
            for j in range(i * i, max_n + 1, i):
                a[j] = 0

    for n in nums:
        if sum(a[0:n + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None
