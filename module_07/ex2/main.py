from .EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    print("Playing Arcane Warrior (Elite Card):\n")

    elite = EliteCard(
        name="Arcane Warrior",
        cost=4,
        rarity="Legendary",
        attack_value=5,
        health=10,
        combat_type="melee",
        blocking_cap=3,
        mana=4
    )

    print("Combat phase:")
    attack_result = elite.attack("Enemy")
    print("Attack result:", attack_result)

    defense_result = elite.defend(5)
    print("Defense result:", defense_result)
    print()

    print("Magic phase:")
    spell_cast = elite.cast_spell("Fireball", ["Enemy1", "Enemy2"])
    print("Spell cast:", spell_cast)

    mana_channel = elite.channel_mana(3)
    print("Mana channel:", mana_channel)
    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
