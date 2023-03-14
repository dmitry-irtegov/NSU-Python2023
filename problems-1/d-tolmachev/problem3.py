#!/usr/bin/env python3

# Returns Collatz conjecture sequence for the specified n
def collatz_conjecture(n: int) -> list[int]:
    if n == 1:    # Edge case, stop the recursion
        return [n]
    return [n] + collatz_conjecture(n // 2 if n % 2 == 0 else 3 * n + 1)    # O(n), where n -- length of sequence

# Used as entrypoint
if __name__ == '__main__':
    while True:
        try:
            print(collatz_conjecture(int(input())))
        except ValueError:
            break
