#!/usr/bin/env python3

# Returns list of cumulative sums for given sequence
def cumulative_sums(seq: list[int]) -> list[int]:
    res: list[int] = [0]    # Cumulative sum for empty list is [0]
    for x in seq:    # O(n)
        res.append(res[-1] + x)
    return res
