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
        self._name = value

    @property
    def calories(self) -> int | float | None:
        return self._calories

    @calories.setter
    def calories(self, value: int | float | None) -> None:
        self._calories = value

    def is_healthy(self) -> bool:
        if self._calories is None or not self._check_calories():
            return False
        return self._calories < 200

    def is_delicious(self) -> bool:
        return True

    def _check_calories(self) -> bool:
        if not isinstance(self._calories, (int, float)):
            return False
        if isinstance(self._calories, bool):
            return False
        return True
