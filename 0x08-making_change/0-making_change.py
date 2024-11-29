#!/usr/bin/python3
"""
Function that determines fewest number
of coins needed to meet total
"""


def makeChange(coins, total):
    """
    Determine fewest number of coins needed to meet
    given amount total
    """
    if total < 1:
        return 0

    change = -1

    if len(coins):
        coins = sorted(coins, reverse=True)
        noOfCoins = len(coins)
        change = 0

        for i in range(noOfCoins):
            while total:
                if total - coins[i] >= 0:
                    change += 1
                    total -= coins[i]
                else:
                    break

        if total != 0:
            change = -1
    return change
