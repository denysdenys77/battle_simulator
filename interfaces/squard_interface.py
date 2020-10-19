from abc import ABC
from typing import List, Union
from .unit_interface import UnitABC
from .warring_interface import WarringABC


class SquadABC(ABC):

    def __init__(self, units: List[Union[WarringABC, UnitABC]]):
        self.units = units
