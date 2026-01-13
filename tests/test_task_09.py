import pytest

from task_09 import connect_dicts


@pytest.mark.parametrize(
    "dict1, dict2, expected",
    [
        (
            {"a": 2, "b": 12},
            {"c": 11, "e": 5},
            {"c": 11, "b": 12},
        ),
        (
            {"a": 13, "b": 9, "d": 11},
            {"c": 12, "a": 15},
            {"d": 11, "c": 12, "a": 13},
        ),
        (
            {"a": 14, "b": 12},
            {"c": 11, "a": 15},
            {"c": 11, "b": 12, "a": 15},
        ),
        (
            {},
            {"a": 10, "b": 5},
            {"a": 10},
        ),
        (
            {"a": 1, "b": 2},
            {"c": 3},
            {},
        ),
    ],
)
def test_connect_dicts(dict1, dict2, expected):
    assert connect_dicts(dict1, dict2) == expected
