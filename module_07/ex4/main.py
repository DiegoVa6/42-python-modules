from .TournamentPlatform import TournamentPlatform
from .TournamentCard import TournamentCard


def main() -> None:
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()
    print("Registering tournament cards...\n")

    # Ratings to match the example
    fire_dragon = TournamentCard("Fire Dragon", 5, "Legendary",
                                 attack=7, health=5, base_rating=1200)
    ice_wizard = TournamentCard("Ice Wizard", 4, "Rare",
                                attack=3, health=4, base_rating=1150)

    dragon_id = platform.register_card(fire_dragon)
    wizard_id = platform.register_card(ice_wizard)

    print(f"{fire_dragon.name} (ID: {dragon_id}):\n"
          f"- Interfaces: [Card, Combatable, Rankable]\n"
          f"- Rating: {fire_dragon.calculate_rating()}\n"
          f"- Record: {fire_dragon.wins}-{fire_dragon.losses}\n")
    print(f"{ice_wizard.name} (ID: {wizard_id}):\n"
          f"- Interfaces: [Card, Combatable, Rankable\n"
          f"- Rating: {ice_wizard.calculate_rating()}\n"
          f"- Record: {ice_wizard.wins}-{ice_wizard.losses}\n")

    print("Creating match...")
    match = platform.create_match(dragon_id, wizard_id)
    print("Match result:", match, "\n")

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    pos = 1
    for entry in leaderboard:
        print(f"{pos}. {entry['name']} - Rating: {entry['rating']}"
              f" ({entry['wins']}-{entry['losses']})")
        pos += 1
    print()

    print("Tournament Report:")
    report = platform.generate_tournament_report()
    print(report, "\n")

    print("Tournament platform successfully demonstrated!")


if __name__ == "__main__":
    main()
