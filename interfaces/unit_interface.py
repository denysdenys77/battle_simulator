from abc import ABC, abstractmethod


class UnitABC(ABC):

    def __init__(self):
        self._health: float = 100.0
        # self._is_killed: bool = False


