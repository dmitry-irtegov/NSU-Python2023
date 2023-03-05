#!/usr/bin/env python3

import math

# Finds prime factorization for a given number
def factorize(x: int) -> list[tuple[int, int]]:
    factors: list[list[int, int]] = []
    while (x & 1) == 0:    # O(k), where k -- power of 2
        if not factors:
            factors.append([2, 0])
        factors[-1][1] += 1
        x >>= 1
    for i in range(3, math.floor(math.sqrt(x)) + 1, 2):    # O(sqrt(x))
        while x % i == 0:    # O(k), where k -- power of i
            if not factors or factors[-1][0] != i:
                factors.append([i, 0])
            factors[-1][1] += 1
            x //= i
    if x > 2:
        factors.append([x, 1])
    return list(map(lambda factor: tuple(factor), factors))
