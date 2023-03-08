#!/usr/bin/env python3

import datetime
import math
import time
from bitarray import bitarray
from typing import Any, Callable

# Generates prime numbers less than the specified number using lists
def lprimes(n: int) -> list[int]:
    primes: list[boolean] = [True if i >= 2 else False for i in range(0, n + 1)]
    for k in range(2, math.ceil(math.sqrt(n))):    # O(NloglogN)
        if primes[k]:
            for i in range(k * 2, n, k):
                primes[i] = False
    return [i for i, _ in filter(lambda entry: entry[1], enumerate(primes))]

# Generates prime numbers less than the specified number using sets
def sprimes(n: int) -> list[int]:
    numbers: set(int) = {i for i in range(2, n)}
    not_primes: set[int] = {i for k in range(2, math.ceil(math.sqrt(n))) for i in range(k * 2, n, k)}    # O(NlogN)
    return list(numbers - not_primes)

# Generates prime numbers less than the specefied number using bitarray
def bprimes(n: int) -> list[int]:
    primes: bitarray = bitarray(n + 1)
    primes[2:] = 1
    for k in range(2, math.ceil(math.sqrt(n))):    # O(NloglogN)
        if primes[k] == 1:
            primes[k * 2 : n : k] = 0
    return primes.search(bitarray([1]))

# Measures the execution time of a given function
def timeit(function: Callable[[int], list[int]], *args: tuple[Any], number: int = 16) -> float:
    durations: list[float] = []
    for _ in range(number):    # Multiple cycles for more accurate results
        start: float = time.time()
        function(args[0])
        end: float = time.time()
        durations.append(1000 * datetime.timedelta(seconds = end - start).total_seconds())
    return sum(durations) / len(durations)

# Used as entrypoint
if __name__ == '__main__':
    n: int = 100000000
    print(f'List: {timeit(bprimes, n)}')
    print(f'Set: {timeit(bprimes, n)}')
    print(f'Bitarray: {timeit(bprimes, n)}')
