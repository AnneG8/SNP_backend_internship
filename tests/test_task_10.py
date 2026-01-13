import pytest

from task_10 import count_words


@pytest.mark.parametrize(
    "text, expected",
    [
        (
            "A man, a plan, a canal -- Panama",
            {
                "a": 3,
                "man": 1,
                "plan": 1,
                "canal": 1,
                "panama": 1,
            },
        ),
        (
            "Doo bee doo bee doo",
            {
                "doo": 3,
                "bee": 2,
            },
        ),
        (
            "Well-known well-known WELL-KNOWN",
            {
                "well-known": 3,
            },
        ),
        (
            "123 456 !!!",
            {},
        ),
        (
            "",
            {},
        ),
    ],
)
def test_count_words(text, expected):
    assert count_words(text) == expected


def test_invalid_input():
    with pytest.raises(TypeError):
        count_words(123)
