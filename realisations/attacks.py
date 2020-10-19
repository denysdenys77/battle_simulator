from interfaces.attack_interface import AttackABC
from interfaces.army_interface import ArmyABC
from typing import Type
from random import choice


class RandomAttack(AttackABC):

    @staticmethod
    def attack(attacking_army: Type[ArmyABC], defending_army: Type[ArmyABC]) -> None:
        pass


class OnWeakestAttack(AttackABC):

    @staticmethod
    def attack(attacking_army: Type[ArmyABC], defending_army: Type[ArmyABC]) -> None:
        pass


class OnStrongestAttack(AttackABC):

    @staticmethod
    def attack(attacking_army: Type[ArmyABC], defending_army: Type[ArmyABC]) -> None:
        pass
