import re


class UnsupportedTypeError(TypeError):
    pass


def is_palindrome(value) -> bool:
    try:
        validate_value(value)
    except UnsupportedTypeError:
        return False

    normalized_value = normalize_string(value)
    return normalized_value == normalized_value[::-1]


def validate_value(value) -> None:
    if isinstance(value, (set, frozenset, dict)):
        raise UnsupportedTypeError(
            f"{type(value).__name__} не имеет определённого порядка элементов"
        )

    if value.__class__.__module__ != "builtins":
        raise UnsupportedTypeError(
            f"{type(value).__name__} не поддерживается для проверки"
        )


def normalize_string(value) -> str:
    readable_value = to_readable_string(value)
    lowercased_value = readable_value.lower()
    normalized_value = re.sub(r"[^a-z0-9]", "", lowercased_value)
    return normalized_value


def to_readable_string(value) -> str:
    if isinstance(value, (list, tuple)):
        return "".join(str(item) for item in value)
    return str(value)
