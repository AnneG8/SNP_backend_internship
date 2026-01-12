class EvenNumbers:
    def __init__(self, n: int):
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError("n must be an integer")

        if n < 0:
            raise ValueError("n must be non-negative")

        self._stop = n

    def __iter__(self):
        self._current = 0
        return self

    def __next__(self) -> int:
        if self._current >= self._stop:
            raise StopIteration

        value = self._current * 2
        self._current += 1
        return value
