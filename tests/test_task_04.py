import pytest

from task_04 import sort_list


@pytest.mark.parametrize(
    "values, expected",
    [
        ([], []),
        ([2, 4, 6, 8], [8, 4, 6, 2, 2]),
        ([1], [1, 1]),
        ([1, 2, 1, 3], [3, 2, 3, 1, 1]),
    ],
)
def test_sort_list(values, expected):
    assert sort_list(values) == expected
