# Arranging Coins

from math import sqrt


def arrangeCoins(n):
    return int((-1 + sqrt(8 * n + 1)) // 2)

n = 5

print(arrangeCoins(n))