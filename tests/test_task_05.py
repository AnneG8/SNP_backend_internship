from datetime import datetime

import pytest

import task_05


FIXED_NOW = datetime(2001, 3, 24, 22, 33, 44)


class FixedDatetime(datetime):
    @classmethod
    def now(cls):
        return FIXED_NOW


@pytest.mark.parametrize(
    "value, expected",
    [
        ([], "24-03-2001 22:33:44"),
        (2, "26-03-2001 22:33:44"),
        (0, "24-03-2001 22:33:44"),
        (-1, "23-03-2001 22:33:44"),
        ("2", "24-03-2001 22:33:44"),
        (None, "24-03-2001 22:33:44"),
        (True, "24-03-2001 22:33:44"),
    ],
)
def test_date_in_future(monkeypatch, value, expected):
    monkeypatch.setattr(task_05, "datetime", FixedDatetime)

    assert task_05.date_in_future(value) == expected
