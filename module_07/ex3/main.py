from .GameEngine import GameEngine
from .FantasyCardFactory import FantasyCardFactory
from .AggressiveStrategy import AggressiveStrategy


def fmt_hand(hand: list) -> str:
    parts = []
    for c in hand:
        parts.append(f"{c.name} ({c.cost})")
    return "[" + ", ".join(parts) + "]"


def main() -> None:
    print("=== DataDeck Game Engine ===\n")

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game...")
    engine.configure_engine(factory, strategy)

    print(f"Factory: {type(factory).__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}\n")

    print("Simulating aggressive turn...")
    sim = engine.simulate_turn()

    hand = sim["hand"]
    print(f"Hand: {fmt_hand(hand)}\n")

    print("Turn execution:")
    turn_exec = sim["turn_execution"]
    print(f"Strategy: {turn_exec['strategy']}")
    print(f"Actions: {turn_exec['actions']}\n")

    print("Game Report:")
    print(engine.get_engine_status(), "\n")

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
