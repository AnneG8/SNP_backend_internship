from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(
        self,
        name: str | None = None,
        calories: int | float | None = None,
        flavor: str | None = None,
    ):
        super().__init__(name=name, calories=calories)
        self.flavor = flavor

    @property
    def flavor(self) -> str | None:
        return self._flavor

    @flavor.setter
    def flavor(self, value: str | None) -> None:
        if value is None:
            self._flavor = None
            return

        if not isinstance(value, str):
            raise TypeError("Flavor must be a string")

        self._flavor = value

    def is_delicious(self) -> bool:
        if self._flavor is None:
            return True

        return self._flavor.lower() != "black licorice"
