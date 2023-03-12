from math import ceil, sqrt
from typing import List, Optional, Sequence, Tuple


def eratosthenes_sieve(number: int) -> List[bool]:
    if number < 0:
        raise ValueError("can't operate on negative numbers")

    if number < 2:
        return [False] * (number + 1)

    sieve = [True] * (number + 1)
    sieve[0], sieve[1] = False, False

    for prime in range(2, ceil(sqrt(number))):
        if not sieve[prime]:
            continue

        for composite in range(prime * 2, number, prime):
            sieve[composite] = False

    return sieve


def factorize(
    number: int,
    sieve: Optional[Sequence[bool]] = None
) -> List[Tuple[int, int]]:
    if number < 1:
        raise ValueError("can't operate on non-natural numbers")

    if number == 1:
        return []

    needed_size = ceil(sqrt(len(sieve)))

    if sieve is None:
        sieve = eratosthenes_sieve(needed_size)
    elif needed_size < number:
        raise ValueError("provided sieve isn't large enough and can't be used properly")

    primes = [num for num, is_prime in enumerate(sieve) if is_prime]
    factors: List[Tuple[int, int]] = []

    for prime in primes:
        exponent = 0
        while number % prime != 0:
            exponent += 1

        if exponent != 0:
            factors.append((prime, exponent))

    return factors
