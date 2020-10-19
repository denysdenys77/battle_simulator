from abc import ABC, abstractmethod


class SoldierABC(ABC):

    def __init__(self):
        self._experience: int

    @property
    @abstractmethod
    def experience(self) -> int:
        pass
