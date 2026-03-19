# ElementalClash

A turn-based combat game where you command elemental creatures against a computer opponent. Built as a team project to practice object-oriented programming in Python.

## How It Works

You start with 3 randomly assigned creatures, each belonging to one of five elements: Fire, Water, Earth, Air, or Lightning. Elements interact in a rock-paper-scissors style system, where some elements deal 1.5x damage against others and only 0.5x against their counters. Each turn, you select a creature and choose between a basic attack, one of two special abilities, or a defend action. The computer does the same. The goal is to reduce the opponent's HP to zero.

## Elemental System

| Element | Strong Against | Weak Against |
|---|---|---|
| Fire | Air, Earth | Water |
| Water | Fire, Earth | Lightning |
| Earth | Lightning, Air | Fire, Water |
| Air | Water, Lightning | Fire, Earth |
| Lightning | Water, Air | Earth |

## Built With

| Category | Details |
|---|---|
| Language | Python 3.8+ |
| Concepts | OOP, inheritance, polymorphism, factory pattern, abstract base classes |
| Architecture | Modular structure across creatures, abilities, core, and engine layers |

## Project Structure

- creatures/: Base creature class and 5 elemental subclasses with 15 unique creatures
- abilities/: Ability system with 30 unique abilities
- core/: Player management, creature factory, and battle calculator
- engine/: Game loop, turn manager, and display system
- main.py: Entry point

## Features

- 15 unique creatures across 5 elemental types, each with 2 special abilities
- Turn-based combat with speed-based action order
- Energy system for ability management
- Smart computer AI based on elemental matchups
- Status effects including burn, freeze, and paralysis
- Battle log with full game history
- Ability cooldown system

## How to Run

```
python main.py
```

Requires Python 3.8 or higher, no additional dependencies needed.

## Team

Developed by Lisa Windisch and two teammates
TU Berlin, M.Sc. Human Factors, 2025
