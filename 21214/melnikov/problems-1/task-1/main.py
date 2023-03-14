def cumulative_sum(sequence: list[int]) -> list[int]:
    accumulator: int = 0
    result: list[int] = []
    for element in sequence:
        result.append(accumulator)
        accumulator += element
    return result + [accumulator]
