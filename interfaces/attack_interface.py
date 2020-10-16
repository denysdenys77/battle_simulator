from abc import ABC, abstractmethod
from .army_interface import ArmyABC
from typing import Type


class AttackABC(ABC):

    @staticmethod
    @abstractmethod
    def attack(attacking_army: Type[ArmyABC], defending_army: Type[ArmyABC]) -> None:
        pass

