import time
from collections import OrderedDict
from functools import wraps
from typing import Any, Callable


def cached(max_size: int | None = None, seconds: int | None = None):
    if not isinstance(max_size, int):
        max_size = None

    if not isinstance(seconds, int):
        seconds = None

    def decorator(func: Callable):
        cache: OrderedDict[Any, tuple[Any, float]] = OrderedDict()

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()

            if key in cache:
                result, timestamp = cache[key]

                if seconds is None or now - timestamp <= seconds:
                    cache.move_to_end(key)
                    return result
                else:
                    del cache[key]

            result = func(*args, **kwargs)
            cache[key] = (result, now)

            if max_size is not None:
                while len(cache) > max_size:
                    cache.popitem(last=False)

            return result

        return wrapper

    return decorator
