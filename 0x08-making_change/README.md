# Making Change Algorithm

## Problem Description
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

### Function Prototype
```python
def makeChange(coins, total):
    # Implementation here
```

### Parameters:
- `coins`: A list of integers representing the values of the coins in your possession.
- `total`: An integer representing the total amount you need to meet.

### Return:
- The function returns the fewest number of coins needed to meet the total.
- If the total is 0 or less, the function returns 0.
- If the total cannot be met by any combination of the coins, the function returns -1.

## Algorithm Description
To solve this problem efficiently, we can use a dynamic programming approach. This method allows us to build up the solution for the total amount by solving subproblems for all amounts leading up to the total.

### Steps:

1. **Initialization**:
   - Create an array `dp` of size `total + 1` where `dp[i]` will hold the minimum number of coins required to get the amount `i`.
   - Initialize `dp[0]` to 0 because zero coins are needed to make a total of 0.
   - Set all other entries in `dp` to `total + 1`, which is a value larger than any possible number of coins needed (serves as infinity).

2. **Dynamic Programming Update**:
   - For each coin in the `coins` list:
     - Iterate through all possible amounts from the coin value up to the total.
     - For each amount, update `dp[amount]` to be the minimum of its current value and `dp[amount - coin] + 1`.
     - This step ensures that we are considering the minimum coins needed by including the current coin.

3. **Final Check**:
   - If `dp[total]` is still `total + 1`, it means the total cannot be reached with the given coins, hence return -1.
   - Otherwise, return `dp[total]`, which represents the minimum number of coins needed.

### Time Complexity:
The time complexity of this algorithm is \(O(n \times m)\), where \(n\) is the total amount and \(m\) is the number of different coin denominations. This is efficient and suitable for this type of problem.
