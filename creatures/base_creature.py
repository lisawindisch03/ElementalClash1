from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Tuple

from abilities.ability import Ability


class Creature(ABC):
    """
    Base class for all creatures.
    Developer B & C rely on this consistent API.
    """

    def __init__(
        self,
        name: str,
        element: str,
        max_hp: int,
        attack: int,
        defense: int,
        speed: int,
        abilities: List[Ability],
    ) -> None:
        self.name = name
        self.element = element
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack = attack
        self.defense = defense
        self.speed = speed

        if len(abilities) != 2:
            raise ValueError("Each creature must have exactly 2 abilities.")
        self.abilities = abilities

    def is_alive(self) -> bool:
        return self.current_hp > 0

    def take_damage(self, amount: int) -> Tuple[int, bool]:
        if amount < 0:
            amount = 0

        old_hp = self.current_hp
        self.current_hp -= amount

        if self.current_hp <= 0:
            self.current_hp = 0
            return old_hp, True

        return amount, False

    def heal(self, amount: int) -> int:
        if amount <= 0:
            return 0
        old = self.current_hp
        self.current_hp = min(self.max_hp, self.current_hp + amount)
        return self.current_hp - old

    @abstractmethod
    def get_elemental_bonus(self, opponent_element: str) -> float:
        """
        Must return 1.5, 1.0, or 0.5 depending on matchup.
        """
        pass

    def __str__(self) -> str:
        return (
            f"{self.name} ({self.element}) - "
            f"HP: {self.current_hp}/{self.max_hp} | "
            f"ATK: {self.attack} | DEF: {self.defense} | SPD: {self.speed}"
        )
