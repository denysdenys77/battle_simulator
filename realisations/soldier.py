from interfaces.unit_interface import UnitABC
from random import randint


class Soldier(UnitABC):

    def __init__(self):
        self._experience: int = 0
        super().__init__()

    def attack(self) -> float:
        """Returns attack success probability of a soldier."""
        return 0.5 * (1 + self._health/100) * randint(50 + self._experience, 100 + 1) / 100

    def damage(self) -> float:
        """Returns amount of damage a soldier can afflict."""
        return 0.05 + self._experience / 100

    def injure(self, health_points: float) -> None:
        """Reduces the number of health points."""
        self._health -= health_points

    @property
    def experience(self) -> int:
        return self._experience
