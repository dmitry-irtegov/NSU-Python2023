#!/usr/bin/env python3

# Finds all occurrences of a given substring
def find_occurrences(string: str, substring: str) -> list[int]:
    occurrences: list[int] = []
    index: int = string.find(substring, 2)
    while index != -1:    # O(k) where k -- number of occurrences
        occurrences.append(index)
        index = string.find(substring, index + 1)    # O(n)
    return occurrences

# Used as entrypoint
if __name__ == '__main__':
    with open('pi.txt', 'r') as file:
        pi: str = file.read()
    while True:
        print('Enter sequence to search for.')
        occurrences: list[int] = find_occurrences(pi, input())
        print(f'Found {len(occurrences)} results.')
        print(f'Positions: {" ".join([str(occurrence) for occurrence in occurrences[:5]])} ...')
