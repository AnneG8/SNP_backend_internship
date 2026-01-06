def sort_list(values: list[int]) -> list[int]:
    if not values:
        return []

    min_value = min(values)
    max_value = max(values)
    result = []

    for value in values:
        if value == min_value:
            result.append(max_value)
        elif value == max_value:
            result.append(min_value)
        else:
            result.append(value)

    result.append(min_value)
    return result
