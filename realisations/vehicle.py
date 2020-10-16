from interfaces.unit_interface import UnitABC
from .soldier import Soldier
from random import randint
from typing import List
from helpers.geometric_average_helper import GeometricHelper


class Vehicles(UnitABC):

    def __init__(self):
        self._operators: list = self._set_operators()
        super().__init__()
        self._health = self._health + 100 * len(self._operators)

    def attack(self) -> float:
        """Returns attack success probability of a vehicle."""
        operators_attack_success = [operator.attack for operator in self._operators]
        return 0.5 * (1 + self._health / 100) * GeometricHelper.get_geometric_average(operators_attack_success)

    def damage(self) -> float:
        """Returns amount of damage a vehicle can afflict."""
        operators_experience = sum([operator.experience for operator in self._operators])
        return 0.1 + sum(operators_experience / 100)

    def injure(self, health_points: float) -> None:
        """Reduces the number of health points."""
        # The total damage inflicted on the vehicle is distributed to the
        # operators as follows: 60% of the total damage is inflicted
        # on the vehicle 20% of the total damage is inflicted on a
        # random vehicle operator The rest of the damage is inflicted
        # evenly to the other operators (10% each)
        pass

    @staticmethod
    def _set_operators() -> List[Soldier]:
        """Generate random number of vehicle operators."""
        return [Soldier() for _ in list(range(randint(1, 3)))]
