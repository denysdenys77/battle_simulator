from abc import ABC, abstractmethod
from .army_interface import ArmyABC
from typing import Type


class GameABC(ABC):

    def __init__(self,
                 armies_count: int,
                 attack_strategy: str,
                 squads_per_army: int,
                 units_per_squad: int):
        self._armies_count = armies_count
        self._attack_strategy = attack_strategy
        self._squads_per_army = squads_per_army
        self._units_per_squad = units_per_squad

    @abstractmethod
    def play(self) -> Type[ArmyABC]:
        pass

    @abstractmethod
    def get_armies(self):
        pass
