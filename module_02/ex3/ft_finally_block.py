def water_plants(plant_list) -> None:
    """
    Docstring for water_plants
    This function tries watering plants or gets
    an exception back in case of error
    """
    print("Opening watering system")
    completed: int = True
    try:
        for plant in plant_list:
            if plant is None:
                plant[0]
            print(f"Watering {plant}")
    except TypeError:
        print("Error: Cannot water None - invalid plant!")
        completed = False
    finally:
        print("Closing watering system (cleanup)")
        if completed:
            print("Watering completed successfully!")


def test_watering_system() -> None:
    """
    Demonstrate normal watering, error handling, and guaranteed cleanup.
    """
    print("=== Garden Watering System ===\n")
    print("Testing normal watering...")
    water_plants(["tomatoe", "lettuce", "carrots"])
    print()
    print("Testing with error...")
    water_plants(["tomatoe", None, "carrots"])
    print()
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
