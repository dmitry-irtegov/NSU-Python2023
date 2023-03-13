#!/usr/bin/env python3

# replaces all out of range sequence elements to it's boundaries
def replace_out_of_range(seq: list[int], a: int, b: int) -> list[int]:
    return list(map(lambda x: check_boundaries(x, a, b), seq))    # O(n)

# Returns input iff it belongs to the specified range, or one of it's boundaries otherwise
def check_boundaries(x: int, l: int, u: int) -> int:
    if x < l:
        return l
    if x > u:
        return u
    return x
