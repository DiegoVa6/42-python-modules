from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, name: str,
                 cost: int,
                 rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        try:
            self.effect_type = EffectType(effect_type)
        except ValueError:
            print("Error: invalid effect_type. Setting to 'damage'")
            self.effect_type = EffectType.DAMAGE

    def play(self, game_state: dict) -> dict:
        available = game_state.get("available_mana", None)
        if available is not None and available < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana"
            }
        if self.effect_type.value == "damage":
            effect = f"Deal {self.cost} damage to target"
        elif self.effect_type.value == "heal":
            effect = f"Heal {self.cost} health to target"
        elif self.effect_type.value == "buff":
            effect = "Apply buff to target"
        else:
            effect = "Apply debuff to target"

        return {"card_played": self.name,
                "mana_used": self.cost, "effect": effect}

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type.value,
            "targets": targets,
            "resolved": True
        }
