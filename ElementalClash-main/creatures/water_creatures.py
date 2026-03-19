from creatures.base_creature import Creature
from abilities.ability import (
    TIDAL_WAVE,
    SHELL_SHIELD,
    AQUA_JET,
    HEALING_RAIN,
    ICE_SHARD,
    FROZEN_TOUCH,
)


class WaterCreature(Creature):
    STRONG_AGAINST = {"Fire", "Earth"}
    WEAK_AGAINST = {"Lightning"}

    def get_elemental_bonus(self, opponent_element: str) -> float:
        if opponent_element in self.STRONG_AGAINST:
            return 1.5
        if opponent_element in self.WEAK_AGAINST:
            return 0.5
        return 1.0


class Aquashell(WaterCreature):
    def __init__(self):
        super().__init__("Aquashell", "Water", 40, 10, 9, 7, [TIDAL_WAVE, SHELL_SHIELD])


class Tidalfin(WaterCreature):
    def __init__(self):
        super().__init__("Tidalfin", "Water", 30, 13, 6, 12, [AQUA_JET, HEALING_RAIN])


class Frostbite(WaterCreature):
    def __init__(self):
        super().__init__("Frostbite", "Water", 35, 12, 7, 9, [ICE_SHARD, FROZEN_TOUCH])
