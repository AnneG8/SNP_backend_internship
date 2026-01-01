import pytest

from task_01 import is_palindrome


@pytest.mark.parametrize(
    "value, expected",
    [
        ("A man, a plan, a canal -- Panama", True),
        ("Madam, I'm Adam!", True),
        ("Abracadabra", False),
        (None, False),
        (False, False),
        (True, False),
        ("Trueurt", True),
        (333, True),
        (123.21, True),
        ([1, 2, 3, 2, 1], True),
        ((1, 2, 1), True),
        ([1, 2, 3], False),
        ("", True),
        ("!!!", True),
        ({1, 2, 1}, False),
        ({"a": 1, 1: "a"}, False),
    ]
)
def test_is_palindrome(value, expected):
    assert is_palindrome(value) is expected


class CustomClass:
    pass


def test_custom_class_returns_false():
    assert is_palindrome(CustomClass()) is False
