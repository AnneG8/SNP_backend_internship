from decimal import Decimal
from typing import Any, Iterable


def coincidence(
        values: Iterable | None = None,
        interval: range | None = None,
) -> list:
    if values is None or interval is None:
        return []

    if not isinstance(values, Iterable) or not isinstance(interval, range):
        raise TypeError

    result = [
        value for value in values if _is_interval_number(value, interval)
    ]

    return result


def _is_interval_number(value: Any, interval: range) -> bool:
    if not _is_real_number(value):
        return False

    return interval.start <= value < interval.stop


def _is_real_number(value: Any) -> bool:
    if isinstance(value, bool):
        return False

    return isinstance(value, (int, float, Decimal))
