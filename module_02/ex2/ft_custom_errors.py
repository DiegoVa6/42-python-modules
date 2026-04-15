class GardenError(Exception):
    """
    class GardenError -> Exception's child
    """
    pass


class PlantError(GardenError):
    """
    class PlantError -> GardenError's child
    """
    pass


class WaterError(GardenError):
    """
    class WaterError -> GardenError's child
    """
    pass


def trigger_plant_problem():
    """
    Simulate a plant problem by raising PlantError.
    """
    raise PlantError("The tomato plant is wilting!")


def trigger_water_problem():
    """
    Simulate a watering problem by raising WaterError.
    """
    raise WaterError("Not enough water in the tank!")


def demo_specific_catches():
    """
    Show how to catch specific garden errors.
    """
    print("Testing PlantError...")
    try:
        trigger_plant_problem()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        trigger_water_problem()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")


def demo_base_catch():
    """
    Show that catching GardenError catches all garden errors.
    """
    print("Testing catching all garden errors...")

    try:
        trigger_plant_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    try:
        trigger_water_problem()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")


if __name__ == "__main__":
    print("=== Custom Garden Errors Demo ===\n")
    demo_specific_catches()
    demo_base_catch()
    print("All custom error types work correctly!")
