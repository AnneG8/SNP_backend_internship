from decimal import Decimal
from typing import Any, Iterable


def multiply_numbers(inputs: Any = None) -> int | None:
    digits = _extract_digits(inputs)

    if not digits:
        return None

    result = 1
    for digit in digits:
        result *= digit

    return result


def _extract_digits(value: Any) -> list[int]:
    if value is None or isinstance(value, bool):
        return []

    if isinstance(value, (int, float, Decimal)):
        return _digits_from_string(str(value))

    if isinstance(value, str):
        return _digits_from_string(value)

    if isinstance(value, Iterable):
        digits: list[int] = []
        for item in value:
            digits.extend(_extract_digits(item))
        return digits

    return []


def _digits_from_string(value: str) -> list[int]:
    return [int(char) for char in value if char.isdigit()]
