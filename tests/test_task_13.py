import time
from unittest.mock import patch

from task_13 import cached


def test_cached_basic():
    calls = []

    @cached()
    def func(x):
        calls.append(x)
        return x * 2

    assert func(2) == 4
    assert func(2) == 4
    assert calls == [2]


def test_cached_with_kwargs():
    calls = []

    @cached()
    def func(x, y=1):
        calls.append((x, y))
        return x + y

    assert func(1) == 2
    assert func(1) == 2
    assert func(1, y=3) == 4

    assert calls == [(1, 1), (1, 3)]


def test_cached_max_size():
    calls = []

    @cached(max_size=2)
    def func(x):
        calls.append(x)
        return x

    func(1)
    func(2)
    func(3)
    func(1)

    assert calls == [1, 2, 3, 1]


def test_cached_seconds_expiration():
    calls = []

    @cached(seconds=1)
    def func(x):
        calls.append(x)
        return x

    func(1)
    time.sleep(1.1)
    func(1)

    assert calls == [1, 1]


def test_cached_unlimited():
    calls = []

    @cached()
    def func(x):
        calls.append(x)
        return x

    for _ in range(10):
        assert func(1) == 1

    with patch("time.time", return_value=1000000):
        func(1)

    assert calls == [1]


def test_invalid_parameters_treated_as_none():
    calls = []

    @cached(max_size="bad", seconds="bad")
    def func(x):
        calls.append(x)
        return x

    func(1)
    func(1)

    assert calls == [1]
