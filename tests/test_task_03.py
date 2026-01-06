from decimal import Decimal

import pytest

from task_03 import max_odd


@pytest.mark.parametrize(
    "values, expected",
    [
        ([1, 2, 3, 4, 4], 3),
        ([21.0, 2, 3, 4, 4], 21),
        (["ololo", 2, 3, 4, [1, 2], None], 3),
        (["ololo", "fufufu"], None),
        ([2, 2, 4], None),
        ([Decimal("21.0"), 3], 21),
        ([Decimal("21.5"), 3], 3),
        ((-1, -2, -3), -1),
        ([True, False, 5], 5),
        ([], None),
    ],
)
def test_max_odd(values, expected):
    assert max_odd(values) == expected


def test_max_odd_invalid_types():
    with pytest.raises(TypeError):
        max_odd(123)

    with pytest.raises(TypeError):
        max_odd(None)
