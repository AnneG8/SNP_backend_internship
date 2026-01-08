import pytest

from task_07 import combine_anagrams


def _normalize_result(result: list[list[str]]) -> list[list[str]]:
    return sorted([group for group in result])


@pytest.mark.parametrize(
    "words, expected",
    [
        (
            [
                "cars",
                "for",
                "potatoes",
                "racs",
                "four",
                "scar",
                "creams",
                "scream",
            ],
            [
                ["cars", "racs", "scar"],
                ["four"],
                ["for"],
                ["potatoes"],
                ["creams", "scream"],
            ],
        ),
        (
            ["Cars", "cars", "scar"],
            [["Cars", "cars", "scar"]],
        ),
        (
            ["cars", "cars", "scar"],
            [["cars", "cars", "scar"]],
        ),
        ([], []),
    ],
)
def test_combine_anagrams(words, expected):
    result = combine_anagrams(words)

    assert _normalize_result(result) == _normalize_result(expected)
