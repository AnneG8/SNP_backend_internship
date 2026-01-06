from datetime import datetime, timedelta
from typing import Any


def date_in_future(days: Any) -> str:
    if not _is_valid_days(days):
        return format_datetime(datetime.now())

    future_date = datetime.now() + timedelta(days=days)
    return format_datetime(future_date)


def _is_valid_days(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)


def format_datetime(dt: datetime) -> str:
    date_format = "%d-%m-%Y %H:%M:%S"
    return dt.strftime(date_format)
