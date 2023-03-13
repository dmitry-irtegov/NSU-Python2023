import math
from typing import MutableSequence, Union


def bound(
    seq: MutableSequence[Union[int, float]],
    lower: Union[int, float] = -math.inf,
    upper: Union[int, float] = math.inf,
) -> None:
    if lower > upper:
        raise ValueError("lower bound can't be greater than upper bound")

    for idx, val in enumerate(seq):
        if seq[idx] < lower:
            seq[idx] = lower

        if seq[idx] > upper:
            seq[idx] = upper
