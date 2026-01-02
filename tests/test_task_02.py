from decimal import Decimal

import pytest

from task_02 import coincidence


@pytest.mark.parametrize(
    "values, interval, expected",
    [
        ([1, 2, 3, 4, 5], range(3, 6), [3, 4, 5]),
        ([None, 1, "foo", 4, 2, 2.5], range(1, 4), [1, 2, 2.5]),
        ([Decimal("1.5")], range(1, 2), [Decimal("1.5")]),
        ([True, False, 1, 0, 2], range(0, 3), [1, 0, 2]),
        ([], range(1, 5), []),
    ],
)
def test_coincidence_valid_cases(values, interval, expected):
    assert coincidence(values, interval) == expected


def test_coincidence_without_argument():
    assert coincidence() == []
    assert coincidence([1, 2, 3]) == []
    assert coincidence(interval=range(1, 3)) == []


def test_coincidence_invalid_types():
    with pytest.raises(TypeError):
        coincidence(123, range(1, 3))

    with pytest.raises(TypeError):
        coincidence([1, 2, 3], "123")
