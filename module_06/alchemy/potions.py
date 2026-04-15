from . import elements as e


def healing_potion() -> str:
    """
    Function to create healing potion
    """
    return (f"Healing potion brewed with "
            f"{e.create_fire()} and {e.create_water()}")


def strength_potion() -> str:
    """
    Function to create strength potion
    """
    return (f"Strength potion brewed with "
            f"{e.create_earth()} and {e.create_fire()}")


def invisibility_potion() -> str:
    """
    Function to create invisibility potion
    """
    return (f"Invisibility potion brewed with "
            f"{e.create_air()} and {e.create_water()}")


def wisdom_potion() -> str:
    """
    Function to create wisdom potion
    """
    return (f"Wisdom potion brewed with all elements: "
            f"{e.create_fire()}{e.create_water()}"
            f"{e.create_air()}{e.create_earth()}")
