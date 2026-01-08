from decimal import Decimal

import pytest

from task_08 import multiply_numbers


@pytest.mark.parametrize(
    "value, expected",
    [
        (None, None),
        ("ss", None),
        ("1234", 24),
        ("sssdd34", 12),
        (2.3, 6),
        ([5, 6, 4], 120),
        (Decimal("2.5"), 10),
        ([1, [2, "a3"], Decimal("4.5")], 120),
        ("0", 0),
        ([], None),
        ([[], []], None),
        (True, None),
        (False, None),
    ],
)
def test_multiply_numbers(value, expected):
    assert multiply_numbers(value) == expected
