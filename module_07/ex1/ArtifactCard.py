from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        if durability <= 0:
            print("Error: durability must be a "
                  "positive integer. Setting durability = 1")
            durability = 1

        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        available = game_state.get("available_mana", None)
        if available is not None and available < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        return {
            "artifact": self.name,
            "effect": self.effect,
            "durability_left": self.durability,
            "activated": True
        }
