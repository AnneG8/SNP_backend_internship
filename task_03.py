from typing import Any, Iterable

from task_02 import _is_real_number


def max_odd(values: Iterable) -> int | None:
    if not isinstance(values, Iterable):
        raise TypeError

    odd_values = [value for value in values if _is_odd_integer(value)]

    if not odd_values:
        return None

    return max(odd_values)


def _is_odd_integer(value: Any) -> bool:
    if not _is_real_number(value):
        return False

    if not isinstance(value, int) and value % 1 != 0:
        return False

    return int(value) % 2 != 0
