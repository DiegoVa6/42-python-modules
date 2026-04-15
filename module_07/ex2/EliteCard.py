from ex0.Card import Card
from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_value: int,
        health: int,
        combat_type: str,
        blocking_cap: int,
        mana: int = 0,
    ) -> None:

        super().__init__(name, cost, rarity)
        self.attack_value = attack_value
        self.health = health
        self.combat_type = combat_type
        self.blocking_cap = blocking_cap
        self.mana = mana

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana")

        if available_mana is not None and available_mana < self.cost:
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana",
            }

        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite summoned to battlefield",
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_value,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_blocked = self.blocking_cap
        if incoming_damage < damage_blocked:
            damage_blocked = incoming_damage

        damage_taken = incoming_damage - damage_blocked

        self.health -= damage_taken
        still_alive = self.health > 0

        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": still_alive
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_value,
            "health": self.health,
            "combat_type": self.combat_type,
            "blocking_cap": self.blocking_cap
        }

    def cast_spell(self, spell_name: str, targets: list[str]) -> dict:
        mana_used = self.cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_used
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana
        }
