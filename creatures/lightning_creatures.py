from creatures.base_creature import Creature
from abilities.ability import (
    THUNDER_FANG,
    STATIC_SHOCK,
    LIGHTNING_BOLT,
    CHARGE_UP,
    STORM_STRIKE,
    PARALYSIS,
)


class LightningCreature(Creature):
    STRONG_AGAINST = {"Water", "Air"}
    WEAK_AGAINST = {"Earth"}

    def get_elemental_bonus(self, opponent_element: str) -> float:
        if opponent_element in self.STRONG_AGAINST:
            return 1.5
        if opponent_element in self.WEAK_AGAINST:
            return 0.5
        return 1.0


class Sparkfang(LightningCreature):
    def __init__(self):
        super().__init__("Sparkfang", "Lightning", 27, 16, 4, 14, [THUNDER_FANG, STATIC_SHOCK])


class Thundermane(LightningCreature):
    def __init__(self):
        super().__init__("Thundermane", "Lightning", 36, 17, 5, 11, [LIGHTNING_BOLT, CHARGE_UP])


class Voltwing(LightningCreature):
    def __init__(self):
        super().__init__("Voltwing", "Lightning", 24, 15, 3, 15, [STORM_STRIKE, PARALYSIS])
