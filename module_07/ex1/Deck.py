import random
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i in self.cards:
            if i.name == card_name:
                self.cards.pop(self.cards.index(i))
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        for c in self.cards:
            total_cost += c.cost
            t = type(c).__name__
            if t == "CreatureCard":
                creatures += 1
            elif t == "SpellCard":
                spells += 1
            elif t == "ArtifactCard":
                artifacts += 1

        avg_cost = (total_cost / total) if total > 0 else 0.0

        return {
            "total_cards": total,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": float(avg_cost)
        }
