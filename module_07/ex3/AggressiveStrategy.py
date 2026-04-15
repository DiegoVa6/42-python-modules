from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage_dealt = 0

        creatures = [c for c in hand if type(c).__name__ == "CreatureCard"]
        spells = [c for c in hand if type(c).__name__ == "SpellCard"]
        artifacts = [c for c in hand if type(c).__name__ == "ArtifactCard"]

        for card in creatures:
            if len(cards_played) >= 2:
                break
            cards_played.append(card.name)
            mana_used += card.cost

        if len(cards_played) < 2:
            for card in spells:
                if len(cards_played) >= 2:
                    break
                cards_played.append(card.name)
                mana_used += card.cost

        if len(cards_played) < 2:
            for card in artifacts:
                if len(cards_played) >= 2:
                    break
                cards_played.append(card.name)
                mana_used += card.cost

        for unit in battlefield:
            if type(unit).__name__ == "CreatureCard":
                damage_dealt += unit.attack

        targets = self.prioritize_targets(["Enemy Player"])

        return {
            "strategy": self.get_strategy_name(),
            "actions": {
                "cards_played": cards_played,
                "mana_used": mana_used,
                "targets_attacked": targets,
                "damage_dealt": damage_dealt
            }
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        if "Enemy Player" in available_targets:
            return ["Enemy Player"]
        return available_targets
