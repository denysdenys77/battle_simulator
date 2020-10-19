from interfaces.unit_interface import UnitABC
from interfaces.soldier_interface import SoldierABC
from interfaces.warring_interface import WarringABC
from random import randint


class Soldier(UnitABC, SoldierABC, WarringABC):

    def __init__(self):
        self._experience: int = 0
        super().__init__()

    def attack(self) -> float:
        """Returns attack success probability of a soldier."""
        return 0.5 * (1 + self._health/100) * randint(50 + self._experience, 100 + 1) / 100

    def damage(self) -> float:
        """Returns amount of damage a soldier can afflict."""
        return 0.05 + self._experience / 100

    def injure(self, total_damage: float) -> bool:
        """Reduces the number of health points."""
        if not self._health - total_damage < 0:
            self._health -= total_damage
        else:
            # removing soldier
            return False
        return True

    def attack_status(self, success: bool) -> None:
        """Reduces the number of experience points."""
        if success:
            self._experience += 1

    @property
    def experience(self) -> int:
        """Returning soldier experience."""
        return self._experience
