class Dessert:
    def __init__(
            self,
            name: str | None = None,
            calories: int | float | None = None
    ):
        self.name = name
        self.calories = calories

    @property
    def name(self) -> str | None:
        return self._name

    @name.setter
    def name(self, value: str | None) -> None:
        self._name: str | None = None
        if isinstance(value, str):
            self._name = value

    @property
    def calories(self) -> int | float | None:
        return self._calories

    @calories.setter
    def calories(self, value: int | float | None) -> None:
        self._calories: int | float | None = None
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            self._calories = value

    def is_healthy(self) -> bool:
        return self._calories is not None and self._calories < 200

    def is_delicious(self) -> bool:
        return True
