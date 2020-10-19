from interfaces.unit_interface import UnitABC
from interfaces.squard_interface import SquadABC
from interfaces.warring_interface import WarringABC
from helpers.geometric_average_helper import GeometricHelper
from typing import Union


class Squad(SquadABC, WarringABC):

    def __init__(self, units):
        super().__init__(units)

    def attack(self) -> float:
        """Returns attack success probability of a squad."""
        units_attack_success = [unit.attack() for unit in self.units]
        return GeometricHelper.get_geometric_average(units_attack_success)

    def damage(self) -> float:
        """Returns amount of damage a squad can afflict."""
        return sum([unit.damage() for unit in self.units])

    def injure(self, total_damage: float) -> bool:
        """Reduces the number of units health points."""
        unit_damage = total_damage / len(self.units)
        for unit in self.units:
            self._injure_unit(unit, unit_damage)

        # destroying squad
        if not len(self.units):
            return False
        return True

    def attack_status(self, success: bool) -> None:
        """Reduces the number of experience points for each unit."""
        for unit in self.units:
            unit.attack_status(success)

    def _injure_unit(self, unit: Union[UnitABC, WarringABC], damage: float) -> None:
        """
        Dealing damage to a squad unit.
        Removing unit from units list if killed.
        """
        unit_survived = unit.injure(damage)
        if not unit_survived:
            self.units.remove(unit)
