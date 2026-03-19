from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Literal, Dict, Any

# Only imported for type hints to avoid circular imports
if TYPE_CHECKING:
    from creatures.base_creature import Creature

EffectType = Literal["damage", "heal", "buff", "debuff", "special"]


@dataclass
class Ability:
    """
    Simple class for abilities that creatures can use in battle.
    This class only holds data and returns info – the actual effect
    (damage, heal, etc.) is handled later by the BattleCalculator.
    """

    name: str
    description: str
    ep_cost: int
    effect_type: EffectType
    power: int

    def execute(self, user: "Creature", target: "Creature") -> Dict[str, Any]:
        """
         Creates a dictionary that describes what this ability wants to do.
         No HP or stats are changed here – this is just data for the
         BattleCalculator.
        """
        return {
            "ability": self,
            "user": user,
            "target": target,
            "effect_type": self.effect_type,
            "power": self.power,
        }

    def __str__(self) -> str:
        return f"{self.name} ({self.ep_cost} EP) - {self.description}"


# ============= FIRE ABILITIES =============
FLAME_DASH = Ability("Flame Dash", "A quick fiery dash.", 15, "damage", 18)
BURNING_AURA = Ability("Burning Aura", "Boosts next attack.", 20, "buff", 12)
METEOR_STRIKE = Ability("Meteor Strike", "Massive meteor impact.", 28, "damage", 30)
VOLCANIC_RAGE = Ability("Volcanic Rage", "Power at cost of defense.", 22, "special", 18)
FIRE_FANG = Ability("Fire Fang", "A burning bite attack.", 16, "damage", 20)
PACK_HOWL = Ability("Pack Howl", "Increases attack.", 18, "buff", 14)

# ============= WATER ABILITIES =============
TIDAL_WAVE = Ability("Tidal Wave", "Large crushing wave.", 22, "damage", 24)
SHELL_SHIELD = Ability("Shell Shield", "Raises defense.", 18, "buff", 15)
AQUA_JET = Ability("Aqua Jet", "Fast water strike.", 15, "damage", 17)
HEALING_RAIN = Ability("Healing Rain", "Restores HP.", 20, "heal", 22)
ICE_SHARD = Ability("Ice Shard", "Ice projectile attack.", 18, "damage", 19)
FROZEN_TOUCH = Ability("Frozen Touch", "Slows the target.", 20, "debuff", 16)

# ============= EARTH ABILITIES =============
ROCK_THROW = Ability("Rock Throw", "Throws a heavy rock.", 14, "damage", 16)
FORTIFY = Ability("Fortify", "Greatly boosts defense.", 20, "buff", 20)
EARTHQUAKE = Ability("Earthquake", "Strong area attack.", 26, "damage", 28)
BURROW = Ability("Burrow", "Avoids damage next turn.", 18, "special", 14)
IRON_SLAM = Ability("Iron Slam", "Heavy body slam.", 20, "damage", 22)
METAL_COAT = Ability("Metal Coat", "Boosts defense temporarily.", 18, "buff", 16)

# ============= AIR ABILITIES =============
WIND_SLASH = Ability("Wind Slash", "Sharp wind strike.", 15, "damage", 17)
EVASION = Ability("Evasion", "Harder to hit.", 18, "buff", 16)
GUST_CANNON = Ability("Gust Cannon", "Wind blast attack.", 20, "damage", 21)
TAILWIND = Ability("Tailwind", "Increases speed.", 18, "buff", 15)
HURRICANE = Ability("Hurricane", "Chaotic storm attack.", 26, "damage", 27)
NIGHT_VISION = Ability("Night Vision", "Improves awareness.", 14, "buff", 12)

# ============= LIGHTNING ABILITIES =============
THUNDER_FANG = Ability("Thunder Fang", "Electric bite attack.", 18, "damage", 21)
STATIC_SHOCK = Ability("Static Shock", "Electric disruption.", 16, "debuff", 15)
LIGHTNING_BOLT = Ability("Lightning Bolt", "Focused lightning strike.", 24, "damage", 26)
CHARGE_UP = Ability("Charge Up", "Boosts future damage.", 18, "buff", 18)
STORM_STRIKE = Ability("Storm Strike", "Massive storm-powered hit.", 28, "damage", 29)
PARALYSIS = Ability("Paralysis", "Severely hinders the target.", 20, "debuff", 20)
