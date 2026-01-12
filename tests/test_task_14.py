import pytest

from task_14 import EvenNumbers


@pytest.mark.parametrize(
    "n, expected",
    [
        (0, []),
        (1, [0]),
        (3, [0, 2, 4]),
        (5, [0, 2, 4, 6, 8]),
    ],
)
def test_even_numbers_generation(n, expected):
    evens = EvenNumbers(n)
    assert list(evens) == expected


def test_even_numbers_iterated_twice():
    evens = EvenNumbers(5)

    first = list(evens)
    second = list(evens)

    assert first == [0, 2, 4, 6, 8]
    assert second == [0, 2, 4, 6, 8]


@pytest.mark.parametrize(
    "bad_value",
    [
        1.5,
        "5",
        None,
        True,
        [0, 2, 4, 6, 8],
    ],
)
def test_even_numbers_invalid_type(bad_value):
    with pytest.raises(TypeError):
        EvenNumbers(bad_value)


@pytest.mark.parametrize("negative_n", [-1, -10, -100])
def test_even_numbers_negative_value(negative_n):
    with pytest.raises(ValueError):
        EvenNumbers(negative_n)
