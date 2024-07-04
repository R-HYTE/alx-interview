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

    def sieve_of_eratosthenes(max_num):
        """
        Generates a list of boolean values indicating prime numbers
        up to max_num.

        Parameters:
        max_num (int): The maximum number to check for primality

        Returns:
        list of bool: List where True indicates a prime number
        """
        is_prime = [True] * (max_num + 1)
        p = 2
        while p * p <= max_num:
            if is_prime[p]:
                for i in range(p * p, max_num + 1, p):
                    is_prime[i] = False
            p += 1
        is_prime[0] = is_prime[1] = False
        return is_prime

    max_n = max(nums)
    is_prime = sieve_of_eratosthenes(max_n)

    def canWin(n):
        """
        Determines if the first player (Maria) can win given the number n.

        Parameters:
        n (int): The upper limit of the range of numbers

        Returns:
        bool: True if Maria can win, False otherwise
        """
        if n == 1:
            return False

        moves = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                moves += 1

        return moves % 2 == 1

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if canWin(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
