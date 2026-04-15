from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    """
    Una carta "competitiva" que:
    - Es Card (playable)
    - Es Combatable (puede atacar/defender)
    - Es Rankable (tiene wins/losses/rating)
    """

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
        base_rating: int = 1200
    ) -> None:
        super().__init__(name, cost, rarity)

        if attack <= 0:
            print("Error: attack must be positive. Setting attack = 1")
            attack = 1
        if health <= 0:
            print("Error: health must be positive. Setting health = 1")
            health = 1

        self.attack_value = attack
        self.health = health

        self.base_rating = base_rating
        self.wins = 0
        self.losses = 0

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
            "effect": "Tournament card entered the arena",
        }

    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_value
        }

    def defend(self, incoming_damage: int) -> dict:
        if incoming_damage < 0:
            incoming_damage = 0

        self.health -= incoming_damage
        if self.health < 0:
            self.health = 0

        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "health_left": self.health,
            "still_alive": self.health > 0
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_value,
            "health": self.health
        }

    # ===== Rankable =====
    def calculate_rating(self) -> int:
        return self.base_rating + (self.wins - self.losses) * 16

    def update_wins(self, wins: int) -> None:
        if wins < 0:
            wins = 0
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        if losses < 0:
            losses = 0
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.calculate_rating(),
            "wins": self.wins,
            "losses": self.losses
        }

    # ===== Extra de ex4 =====
    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "rarity": self.rarity,
            "cost": self.cost,
            "combat": self.get_combat_stats(),
            "rank": self.get_rank_info()
        }
