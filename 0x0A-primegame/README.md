# Prime Game Winner Determination

## Overview

This project implements an algorithm to determine the winner of a prime number game played between Maria and Ben. The game involves selecting prime numbers from a set of consecutive integers and removing their multiples. Maria always goes first, and both players play optimally.

## Algorithm Description

### Sieve of Eratosthenes

The core of the algorithm relies on the Sieve of Eratosthenes to efficiently identify prime numbers up to the maximum value in the given rounds. This method marks non-prime numbers by iterating through and eliminating the multiples of each prime starting from 2.

### Game Simulation

For each round:
1. Initialize the set of numbers from 1 to `n`.
2. Maria starts by choosing the smallest prime and removing it along with its multiples.
3. Ben follows by choosing the next available prime and removing it along with its multiples.
4. The game continues until no more primes can be chosen.

The player who cannot make a move loses the game. The algorithm tracks the number of moves and determines the winner based on the parity (odd or even) of the number of moves.

## Why This Algorithm?

1. **Efficiency:** The Sieve of Eratosthenes is an efficient algorithm for finding all prime numbers up to a given limit, which is crucial for handling the upper constraints of the problem.
2. **Optimal Play Simulation:** The game simulation ensures that both players play optimally, which is essential for accurately determining the winner.
3. **Clarity:** The use of helper functions and detailed documentation provides clear understanding and maintenance of the code.

## Usage

To determine the winner for a set of rounds, use the `isWinner` function:

```python
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))  # Output: "Ben"
```

The function takes the number of rounds `x` and a list `nums` containing the values of `n` for each round. It returns the name of the player who won the most rounds or `None` if there is no clear winner.
