from abc import ABC, abstractmethod


class UnitABC(ABC):

    def __init__(self):
        self._health: float = 100.0
        self._killed: bool = False

    @abstractmethod
    def attack(self) -> float:
        pass

    @abstractmethod
    def damage(self) -> float:
        pass

    @abstractmethod
    def injure(self, health_points: float) -> None:
        pass
