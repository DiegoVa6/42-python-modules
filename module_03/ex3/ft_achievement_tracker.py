if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter",
                   "boss_slayer", "speed_demon", "perfectionist"])

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}\n")

    print("=== Achievement Analytics ===")

    all_unique = alice.union(bob).union(charlie)
    common_all = alice.intersection(bob).intersection(charlie)

    rare = (
        alice.difference(bob).difference(charlie)
        .union(bob.difference(alice).difference(charlie))
        .union(charlie.difference(alice).difference(bob))
    )

    print(f"All unique achievements: {all_unique}")
    print(f"Total unique achievements: {len(all_unique)}\n")
    print(f"Common to all players: {common_all}")
    print(f"Rare achievements (1 player): {rare}\n")

    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    print(f"Alice unique: {alice.difference(bob)}")
    print(f"Bob unique: {bob.difference(alice)}")
