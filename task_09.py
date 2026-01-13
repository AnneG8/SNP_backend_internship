from typing import Any


def connect_dicts(
        dict1: dict[Any, int],
        dict2: dict[Any, int]
) -> dict[Any, int]:
    sum1 = sum(dict1.values())
    sum2 = sum(dict2.values())

    if sum1 > sum2:
        primary, secondary = dict1, dict2
    else:
        primary, secondary = dict2, dict1

    merged: dict[Any, int] = {}

    merged.update(secondary)
    merged.update(primary)

    filtered = {
        key: value
        for key, value in merged.items()
        if value >= 10
    }

    sorted_items = sorted(filtered.items(), key=lambda item: item[1])

    return dict(sorted_items)
