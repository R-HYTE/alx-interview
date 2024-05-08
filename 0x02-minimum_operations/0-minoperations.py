#!/usr/bin/python3
"""
This module defines a function minOperations that computes the
minimum number of "Copy All" and "Paste" operations needed
to create a specified number of 'H' characters in a text file,
starting from a single 'H'. The function utilizes the mathematical
principle of prime factorization to minimize the number of operations
required by efficiently grouping pastes wherever possible.

The algorithm's efficiency stems from the understanding that the optimal way
to expand the number of 'H' characters using the least operations is through
repetitive multiplication of the largest possible groups of 'H' characters
we can manage at each step. The approach is somewhat analogous to factoring
an integer, where each factor represents a block of 'H's that can be copied
and pasted together.

"""


def minOperations(n):
    """
    Calculate the minimum number of operations needed to reach exactly n 'H'
    characters in a text file, starting from a single 'H'.
    The only allowed operations are 'Copy All' and 'Paste'.

    Parameters:
    - n (int): The target number of 'H' characters to achieve.

    Returns:
    - int: Minimum number of operations required to achieve n 'H' characters.
           If n is less than or equal to 1,
           returns 0 as no operations are needed or possible to multiply.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor * factor <= n:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    if n > 1:
        operations += n

    return operations
