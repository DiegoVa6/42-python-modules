from alchemy.elements import create_fire, create_earth


def lead_to_gold() -> str:
    """
    Docstring for lead_to_gold
    """
    return f"Lead transmuted to gold using {create_fire()}"


def stone_to_gem() -> str:
    """
    Docstring for stone_to_gem
    """
    return f"Stone transmuted to gem using {create_earth()}"
