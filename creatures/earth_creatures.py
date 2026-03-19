from creatures.base_creature import Creature
from abilities.ability import (
    ROCK_THROW,
    FORTIFY,
    EARTHQUAKE,
    BURROW,
    IRON_SLAM,
    METAL_COAT,
)


class EarthCreature(Creature):
    STRONG_AGAINST = {"Lightning", "Air"}
    WEAK_AGAINST = {"Fire", "Water"}

    def get_elemental_bonus(self, opponent_element: str) -> float:
        if opponent_element in self.STRONG_AGAINST:
            return 1.5
        if opponent_element in self.WEAK_AGAINST:
            return 0.5
        return 1.0


class Stoneguard(EarthCreature):
    def __init__(self):
        super().__init__("Stoneguard", "Earth", 50, 8, 10, 5, [ROCK_THROW, FORTIFY])


class Terraclaw(EarthCreature):
    def __init__(self):
        super().__init__("Terraclaw", "Earth", 38, 14, 8, 8, [EARTHQUAKE, BURROW])


class Ironback(EarthCreature):
    def __init__(self):
        super().__init__("Ironback", "Earth", 42, 11, 9, 6, [IRON_SLAM, METAL_COAT])
