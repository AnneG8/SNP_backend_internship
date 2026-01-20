import pytest

from task_12 import JellyBean


@pytest.mark.parametrize(
    "flavor, expected",
    [
        (None, True),
        (5, True),
        ("strawberry", True),
        ("vanilla", True),
        ("BLACK LICORICE", False),
    ],
)
def test_is_delicious(flavor, expected):
    jellybean = JellyBean(flavor=flavor)
    assert jellybean.is_delicious() is expected


@pytest.mark.parametrize(
    "calories, expected",
    [
        (None, False),
        (0, True),
        (199, True),
        (200, False),
        (300, False),
        ("test_calories", False),
    ],
)
def test_is_healthy(calories, expected):
    jellybean = JellyBean(calories=calories)
    assert jellybean.is_healthy() is expected
