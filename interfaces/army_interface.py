from abc import ABC
from typing import List, Union
from .squard_interface import SquadABC
from .warring_interface import WarringABC


class ArmyABC(ABC):

    def __init__(self, squads: List[Union[WarringABC, SquadABC]]):
        self.squads = squads
