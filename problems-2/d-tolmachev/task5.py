#!/usr/bin/env python3

import math

# Generates prime numbers less than the specified number
def primes(n: int) -> list[int]:
    return list({i for i in range(2, n)} - {i for k in range(2, math.ceil(math.sqrt(n))) for i in range(k * 2, n, k)})    # O(NlogN)
