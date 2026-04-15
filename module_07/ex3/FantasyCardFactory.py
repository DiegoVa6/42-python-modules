from ex0.CreatureCard import CreatureCard, Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from .CardFactory import CardFactory
import random


class FantasyCardFactory(CardFactory):
    def create_creature(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "dragon":
            return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
        if name_or_power == "troll":
            return CreatureCard("Resistant Troll", 3, "Common", 1, 4)
        if name_or_power == "orc":
            return CreatureCard("Hard orc", 4, "Uncommon", 3, 3)

        return CreatureCard("Goblin Warrior", 2, "Common", 2, 1)

    def create_spell(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "fireball":
            return SpellCard("Fireball", 4, "Uncommon", "damage")
        if name_or_power == "poison_cloud":
            return SpellCard("Poison Cloud", 2, "Special", "debuff")

        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power: str | int | None = None) -> Card:
        if name_or_power == "mana_ring":
            return ArtifactCard("Mana Ring", 2, "Common", 3,
                                "Permanent: +1 mana per turn")
        return ArtifactCard("Sword of Power", 1, "Legendary", 3,
                            "Permanent: +1 attack damage in every card")

    def create_themed_deck(self, size: int) -> dict:
        supported = self.get_supported_types()

        hand = []
        battlefield = []

        for _ in range(size):
            category = random.choice(["creatures", "spells", "artifacts"])
            keyword = random.choice(supported[category])

            if category == "creatures":
                card = self.create_creature(keyword)
                battlefield.append(card)
            elif category == "spells":
                card = self.create_spell(keyword)
            else:
                card = self.create_artifact(keyword)

            hand.append(card)

        return {"hand": hand, "battlefield": battlefield}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin", "orc", "troll"],
            "spells": ["fireball", "lightning_bolt", "poison_cloud"],
            "artifacts": ["mana_ring", "sword_of_power"]
        }
