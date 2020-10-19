from interfaces.army_interface import ArmyABC
from interfaces.squard_interface import SquadABC
from interfaces.warring_interface import WarringABC
from typing import List


class Army(ArmyABC):

    def __init__(self, squads: List[WarringABC, SquadABC]):
        super().__init__(squads)
