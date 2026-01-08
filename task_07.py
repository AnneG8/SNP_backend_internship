def combine_anagrams(words_array: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = {}

    for word in words_array:
        key = "".join(sorted(word.lower()))

        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())
