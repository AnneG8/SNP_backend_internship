import pytest

from task_11 import Dessert


@pytest.mark.parametrize(
    "calories, expected",
    [
        (None, False),
        (0, True),
        (199, True),
        (200, False),
        (300, False),
    ],
)
def test_is_healthy(calories, expected):
    dessert = Dessert("Test", calories)
    assert dessert.is_healthy() is expected


@pytest.mark.parametrize(
    "name, calories, expected",
    [
        ("Cake", 300, True),
        ("", 0, True),
        (None, None, True),
    ],
)
def test_is_delicious_always_true(name, calories, expected):
    dessert = Dessert(name, calories)
    assert dessert.is_delicious() is expected


@pytest.mark.parametrize(
    "calories",
    [
        "many",
        [],
        True,
    ],
)
def test_invalid_calories_type(calories):
    with pytest.raises(TypeError):
        Dessert("Cake", calories)
