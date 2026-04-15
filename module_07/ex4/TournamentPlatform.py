from .TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: dict[str, TournamentCard] = {}
        self.matches_played: int = 0
        self._type_counters: dict[str, int] = {}
        self.platform_status: str = "active"

    def register_card(self, card: TournamentCard) -> str:
        parts = card.name.split()
        name = ""
        for p in parts:
            name += p
            name += "_"
        name += f"{len(self.cards)}"
        self.cards[name] = card
        return name

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards.get(card1_id)
        card2 = self.cards.get(card2_id)

        if card1 is None or card2 is None:
            return {"error": "Invalid card id(s)"}

        r1 = card1.calculate_rating()
        r2 = card2.calculate_rating()

        if r1 >= r2:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = card1, card2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = card2, card1

        winner.update_wins(1)
        loser.update_losses(1)
        """winner.base_rating += 16
        loser.base_rating -= 16"""

        self.matches_played += 1

        return {
            "winner": winner_id,
            "loser": loser_id,
            "winner_rating": winner.calculate_rating(),
            "loser_rating": loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list:
        ids = []
        for cid in self.cards:
            ids.append(cid)

        leaderboard = []
        temp = ids[:]  # copia

        while len(temp) > 0:
            best_idx = 0
            best_id = temp[0]
            best_card = self.cards[best_id]

            for i in range(1, len(temp)):
                cid = temp[i]
                c = self.cards[cid]

                if c.calculate_rating() > best_card.calculate_rating():
                    best_idx = i
                    best_id = cid
                    best_card = c
                elif (c.calculate_rating() == best_card.calculate_rating()
                      and c.wins > best_card.wins):
                    best_idx = i
                    best_id = cid
                    best_card = c

            info = best_card.get_rank_info()
            leaderboard.append({
                "id": best_id,
                "name": best_card.name,
                "rating": info["rating"],
                "wins": info["wins"],
                "losses": info["losses"],
            })

            temp.pop(best_idx)

        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        total_rating = 0
        for c in self.cards.values():
            total_rating += c.calculate_rating()

        avg_rating = int(total_rating / total_cards) if total_cards > 0 else 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": self.platform_status,
        }
