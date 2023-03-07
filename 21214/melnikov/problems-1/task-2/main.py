def cut(sequence: list[int], a: int, b: int) -> list[int]:
    """All numbers less than a will be replaced with a value;
    all numbers greater than b will be replaced with b value."""
    return [a if x < a else b if x > b else x for x in sequence]
