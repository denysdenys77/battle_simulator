from abc import ABC
from typing import List
from .unit_interface import UnitABC


class SquadABC(ABC):

    def __init__(self):
        self.units: List[UnitABC]
