from typing import Iterator


def collatz_conjecture(num: int) -> Iterator[int]:
    yield num
    while num != 1:
        num = num // 2 if num % 2 == 0 else 3 * num + 1
        yield num


def pretty_format(conj: Iterator[int]) -> str:
    return " -> ".join(str(num) for num in conj)
