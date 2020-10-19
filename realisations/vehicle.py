from interfaces.unit_interface import UnitABC
from interfaces.soldier_interface import SoldierABC
from interfaces.vehicle_interface import VehicleABC
from interfaces.warring_interface import WarringABC
from random import randint, choice
from typing import List, Union, Type
from helpers.geometric_average_helper import GeometricHelper


class Vehicle(UnitABC, VehicleABC, WarringABC):

    def __init__(self, soldier_class: Type[Union[UnitABC, SoldierABC, WarringABC]]):
        self._soldier_class = soldier_class
        self._operators: list = self._set_operators()
        super().__init__()
        self._health = self._health + 100 * len(self._operators)

    def attack(self) -> float:
        """Returns attack success probability of a vehicle."""
        operators_attack_success = [float(operator.attack()) for operator in self._operators]
        return 0.5 * (1 + self._health / 100) * GeometricHelper.get_geometric_average(operators_attack_success)

    def damage(self) -> float:
        """Returns amount of damage a vehicle can afflict."""
        operators_experience = sum([operator.experience for operator in self._operators])
        return 0.1 + sum(operators_experience / 100)

    def injure(self, total_damage: float) -> bool:
        """Reduces the number of health points."""

        # calculating damage for each unit
        vehicle_damage = total_damage / 100 * 60
        sed_operator_damage = total_damage / 100 * 20
        rest_operators_damage = total_damage / 100 * 10

        # damaging vehicle
        if self._health - vehicle_damage < 0:
            self._health = 0
        else:
            # destroying vehicle
            return False

        # damaging random operator
        sed_operator = choice(self._operators)
        self._injure_operator(sed_operator, sed_operator_damage)

        # damaging rest operators
        for operator in self._operators:
            if operator != sed_operator:
                self._injure_operator(operator, rest_operators_damage)
        return True

    def attack_status(self, success: bool) -> None:
        """Reduces the number of experience points for each operator."""
        for operator in self._operators:
            operator.attack_status(success)

    def _set_operators(self) -> List[Union[UnitABC, SoldierABC]]:
        """Generate random number of vehicle operators."""
        return [self._soldier_class() for _ in list(range(randint(1, 3)))]

    def _injure_operator(self, operator: Union[UnitABC, SoldierABC, WarringABC], damage: float) -> None:
        """
        Dealing damage to a vehicle operator.
        Removing operator from operators list if killed.
        """
        operator_survived = operator.injure(damage)
        if not operator_survived:
            self._operators.remove(operator)
