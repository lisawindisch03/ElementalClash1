from creatures.base_creature import Creature
from abilities.ability import (
    WIND_SLASH,
    EVASION,
    GUST_CANNON,
    TAILWIND,
    HURRICANE,
    NIGHT_VISION,
)


class AirCreature(Creature):
    STRONG_AGAINST = {"Water", "Lightning"}
    WEAK_AGAINST = {"Fire", "Earth"}

    def get_elemental_bonus(self, opponent_element: str) -> float:
        if opponent_element in self.STRONG_AGAINST:
            return 1.5
        if opponent_element in self.WEAK_AGAINST:
            return 0.5
        return 1.0


class Zephyrwing(AirCreature):
    def __init__(self):
        super().__init__("Zephyrwing", "Air", 25, 11, 4, 15, [WIND_SLASH, EVASION])


class Cloudstrider(AirCreature):
    def __init__(self):
        super().__init__("Cloudstrider", "Air", 30, 12, 5, 14, [GUST_CANNON, TAILWIND])


class Tempestowl(AirCreature):
    def __init__(self):
        super().__init__("Tempestowl", "Air", 33, 13, 6, 12, [HURRICANE, NIGHT_VISION])
