from .basic import lead_to_gold
from ..potions import healing_potion


def philosophers_stone() -> str:
    """
    Docstring for philosophers_stone
    """
    return (f"Philosopher’s stone created using "
            f"{lead_to_gold()} and {healing_potion()}")


def elixir_of_life() -> str:
    """
    Docstring for elixir_of_life
    """
    return "Elixir of life: eternal youth achieved!"
