#!/usr/bin/python3
"""
Making Change Module
"""


def makeChange(coins, total):
    """ Determine the fewest number of coins
        needed to meet a given amount total.

    Parameters:
    coins (list): Integers representing the values of the coins in possession.
    total (int): An integer representing the total amount you need to meet.

    Returns:
    int: The fewest number of coins needed to meet the total.
        If the total is 0 or less, returns 0.

         If the total cannot be met by any combination of the coins,
         returns -1.
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] <= total else -1
