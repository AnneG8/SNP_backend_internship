class Dessert:
    def __init__(self, name: str | None = None, calories: int | None = None):
        self._name = name
        self._calories = calories

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        self._name = value

    @property
    def calories(self) -> int | None:
        return self._calories

    @calories.setter
    def calories(self, value: int | None) -> None:
        self._calories = value

    def is_healthy(self) -> bool:
        return self._calories is not None and self._calories < 200

    def is_delicious(self) -> bool:
        return True
