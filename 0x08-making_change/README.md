# 0. Change Comes From Within

This project involves solving the classic coin change problem using dynamic programming or greedy algorithms. The goal is to determine the minimum number of coins needed to make up a given total amount, given a list of coin denominations.

## Problem Statement

Given a pile of coins of different values, the task is to determine the fewest number of coins needed to meet a given amount. 

Function Prototype:
```python
def makeChange(coins, total):
    """ Determine fewest number of coins needed to meet
    given amount total """
```

**Parameters:**
- `coins` (List[int]): A list of the values of the coins in your possession.
- `total` (int): The total amount to be made with the coins.

**Returns:**
- If `total` is 0 or less, return 0.
- If `total` cannot be met by any number of coins you have, return -1.
- Otherwise, return the fewest number of coins needed to make up the `total`.

## Approach

### Greedy Algorithm
- This approach sorts the coin denominations in descending order and uses the largest coin first to minimize the number of coins. This method may not always yield the optimal solution for every set of coin denominations.

### Dynamic Programming
- This approach uses a table to store the minimum number of coins needed for each amount from 0 up to `total`. It guarantees the optimal solution by solving smaller subproblems and combining their solutions.

## Requirements

- **Python Version:** 3.4.3
- **Allowed Editors:** vi, vim, emacs
- **Executable Files:** Ensure all files end with a new line and start with `#!/usr/bin/python3`.

## Files

- `0-making_change.py`: Contains the implementation of the `makeChange` function.
- `0-main.py`: Contains test cases to verify the functionality of the `makeChange` function.

## Examples

```python
# Example 1
print(makeChange([1, 2, 25], 37))
# Output: 7

# Example 2
print(makeChange([1256, 54, 48, 16, 102], 1453))
# Output: -1
```

## How to Run

1. Ensure that you have Python 3.4.3 installed.
2. Make the files executable with `chmod +x filename.py`.
3. Run the test script using `./0-main.py`.

## Author

Layla ABKARI - [My GitHub](https://github.com/Lelaabk)