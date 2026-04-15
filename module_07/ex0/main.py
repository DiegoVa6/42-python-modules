from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    creature = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(creature.get_card_info())
    print()

    available_mana = 6
    print("Playing Fire Dragon with 6 mana available:")
    print("Playable:", creature.is_playable(available_mana))

    game_state = {"available_mana": available_mana}
    result = creature.play(game_state)
    print("Play result:", result)
    print()

    print("Fire Dragon attacks Goblin Warrior:")
    combat = creature.attack_target("Goblin Warrior")
    print("Attack result:", combat)
    print()

    print("Testing insufficient mana (3 available):")
    available_mana = 3
    print("Playing Fire Dragon with 3 mana available:")
    print("Playable:", creature.is_playable(available_mana))
    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
