from typing import Iterable, List, Union


def cumulative_sums(seq: Iterable[Union[int, float]]) -> List[float]:
    current_sum: float = 0.0
    return [current_sum := current_sum + num for num in seq]
