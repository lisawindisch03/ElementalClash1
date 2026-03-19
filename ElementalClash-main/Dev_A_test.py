from creatures.fire_creatures import Emberfox
from creatures.water_creatures import Aquashell
from abilities.ability import FLAME_DASH


def main():
    fox = Emberfox()
    shell = Aquashell()

    print("=== Creatures ===")
    print(fox)
    print(shell)

    print("\n=== Elemental bonus ===")
    print("Fire vs Water:", fox.get_elemental_bonus(shell.element))

    print("\n=== Ability execution ===")
    effect = FLAME_DASH.execute(fox, shell)
    print(effect)


if __name__ == "__main__":
    main()
