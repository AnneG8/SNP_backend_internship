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
    if isinstance(value, bool):
        return False

    if not isinstance(value, (int, float, Decimal)):
        return False

    return interval.start <= value < interval.stop
