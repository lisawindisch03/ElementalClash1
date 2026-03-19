from __future__ import annotations

from creatures.base_creature import Creature
from abilities.ability import (
    FLAME_DASH,
    BURNING_AURA,
    METEOR_STRIKE,
    VOLCANIC_RAGE,
    FIRE_FANG,
    PACK_HOWL,
)


class FireCreature(Creature):
    STRONG_AGAINST = {"Air", "Earth"}
    WEAK_AGAINST = {"Water"}

    def get_elemental_bonus(self, opponent_element: str) -> float:
        if opponent_element in self.STRONG_AGAINST:
            return 1.5
        if opponent_element in self.WEAK_AGAINST:
            return 0.5
        return 1.0


class Emberfox(FireCreature):
    def __init__(self):
        super().__init__("Emberfox", "Fire", 28, 14, 4, 13, [FLAME_DASH, BURNING_AURA])


class Infernosaur(FireCreature):
    def __init__(self):
        super().__init__("Infernosaur", "Fire", 45, 18, 3, 6, [METEOR_STRIKE, VOLCANIC_RAGE])


class Blazewolf(FireCreature):
    def __init__(self):
        super().__init__("Blazewolf", "Fire", 32, 15, 5, 11, [FIRE_FANG, PACK_HOWL])
