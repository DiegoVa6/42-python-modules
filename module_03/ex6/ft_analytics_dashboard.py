if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===\n")

    players = {"alice": {"score": 2300, "active": True, "region": "north"},
               "bob": {"score": 1800, "active": True, "region": "east"},
               "charlie": {"score": 2150, "active": True, "region": "central"},
               "diana": {"score": 2050, "active": False, "region": "west"}
               }
    achievements = {"alice": {'first_kill', 'level_10', 'boss_slayer',
                              'treasure_hunter', 'speed_demon'},
                    "bob": {'first_kill', 'level_10', 'collector'},
                    "charlie": {'level_10', 'treasure_hunter',
                                'speed_demon', 'perfectionist'},
                    "diana": {}
                    }

    print("=== Game Analytics Dashboard ===")
    high_scorers = [player for player, stats in players.items()
                    if stats["score"] > 2000]
    scores_doubled = [stats["score"]*2 for stats in players.values()]
    active_players = [player for player, stats in players.items()
                      if stats["active"] is True]
    print("High scorers (>2000): ", high_scorers)
    print("Scores doubled: ", scores_doubled)
    print("Active players: ", active_players)

    print("\n=== Dict Comprehension Examples ===")
    scores_d = {player: stats["score"] for player, stats in players.items()}
    scores_categories = {"high": len([1 for stats in players.values()
                                      if stats["score"] > 2000]),
                         "medium": len([1 for stats in players.values()
                                       if 2000 > stats["score"] > 1000]),
                         "low": len([1 for stats in players.values()
                                    if stats["score"] < 1000])
                         }
    achievements_count = {player: len(ach)
                          for player, ach in achievements.items()}
    print("Player scores: ", scores_d)
    print("Score categories: ", scores_categories)
    print("Achievement counts: ", achievements_count)

    print("\n=== Set Comprehension Examples ===")
    unique_players = set(player for player in achievements)
    unique_achievements = set(ach for achs in achievements.values()
                              for ach in achs)
    active_regions = set(stats["region"] for stats in players.values()
                         if stats["active"] is True)
    print("Unique players: ", unique_players)
    print("Unique achievements: ", unique_achievements)
    print("Active regions: ", active_regions)

    print("\n=== Combined Analysis ===")
    total_score = sum([stats["score"] for stats in players.values()])
    most_val_ply = ""
    score = -1
    for player, stats in players.items():
        if stats["score"] > score:
            most_val_ply = player
            score = stats["score"]
    print("Total players: ", len(players))
    print("Total unique achievements: ", len(unique_achievements))
    print(f"Average score: {total_score / len(players):.2f}")
    print(f"Top performer: {most_val_ply} ({players[most_val_ply]['score']} "
          f"points, {len(achievements[most_val_ply])} achievements)")
