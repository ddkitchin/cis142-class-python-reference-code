#@copyright Deborah Kitchin
class Treasure:

    def __init__(self, name: str = "", value: int = 0) -> None:
        self._name = name
        self._value = value

    def getName(self) -> str:
        return self._name

    def setName(self, name: str) -> None:
        self._name = name

    def getValue(self) -> int:
        return self._value

    def setValue(self, value: int) -> None:
        self._value = value

    def __str__(self) -> str:
        return f'Treasure Item {self._name} is worth {self._value}'

    def __repr__(self) -> str:
        return self.__str__()