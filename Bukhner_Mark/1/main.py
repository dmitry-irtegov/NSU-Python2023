from typing import List, Union


def cumulative_sum(lst: List[Union[int, float]]) -> List[Union[int, float]]:
    result = [0]
    for x in lst:
        result.append(result[-1] + x)
    return result
