from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 attack: int,
                 health: int) -> None:
        super().__init__(name, cost, rarity)
        if attack <= 0:
            print("Error: attack must be a "
                  "positive integer. Setting attack = 1")
            attack = 1
        if health <= 0:
            print("Error: health must be a "
                  "positive integer. Setting health = 1")
            health = 1

        self.attack = attack
        self.health = health

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
            "effect": "Creature summoned to battlefield"
        }

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info["type"] = "Creature"
        card_info["attack"] = self.attack
        card_info["health"] = self.health
        return card_info

    def attack_target(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
