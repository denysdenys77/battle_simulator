from abc import ABC, abstractmethod
from typing import List, Union, Type

from interfaces.unit_interface import UnitABC
from interfaces.soldier_interface import SoldierABC


class VehicleABC(ABC):

    def __init__(self):
        self._soldier_class: Type[Union[UnitABC, SoldierABC]]
        self._operators: List[Union[UnitABC, SoldierABC]]

    @abstractmethod
    def _set_operators(self) -> List[Union[UnitABC, SoldierABC]]:
        pass
