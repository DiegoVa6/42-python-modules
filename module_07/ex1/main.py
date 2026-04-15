from ex0.CreatureCard import CreatureCard
from .ArtifactCard import ArtifactCard
from .SpellCard import SpellCard
from .Deck import Deck


def main() -> None:
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    card1 = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    card2 = SpellCard("Lightning Bolt", 3, "Common", "damage")
    card3 = ArtifactCard("Mana Crystal", 2,
                         "Common", 5, "Permanent: +1 mana per turn")

    mg = Deck()
    mg.add_card(card1)
    mg.add_card(card2)
    mg.add_card(card3)

    print(mg.get_deck_stats())
    print()

    print("Drawing and playing cards:\n")
    while len(mg.cards) > 0:
        actual = mg.draw_card()
        card_type = type(actual).__name__.replace("Card", "")
        print(f"Drew: {actual.name} ({card_type})")
        print("Play result:", actual.play({"available_mana": 999}))
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
