import re


def count_words(string: str) -> dict[str, int]:
    if not isinstance(string, str):
        raise TypeError

    words = re.findall(r"[^\W\d_]+(?:-[^\W\d_]+)*", string.lower())

    result: dict[str, int] = {}
    for word in words:
        result[word] = result.get(word, 0) + 1

    return result
