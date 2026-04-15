def check_plant_health(plant_name, water_level, sunlight_hours):
    """
    Check plant inputs and raise ValueError if something is wrong.
    """
    if plant_name == "":
        raise ValueError("Error: Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Error: Water level {water_level} "
                         f"is too low (min 0)")
    if sunlight_hours > 12:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """
    Run several tests and show that errors are raised and handled.
    """
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    try:
        print(check_plant_health("tomato", 5, 8), "\n")
    except ValueError as e:
        print(e)

    print("Testing empty plant name...")
    try:
        print(check_plant_health("", 5, 8), "\n")
    except ValueError as e:
        print(e, "\n")

    print("Testing bad water level...")
    try:
        print(check_plant_health("tomato", 15, 8), "\n")
    except ValueError as e:
        print(e, "\n")

    print("Testing bad sunlight hours...")
    try:
        print(check_plant_health("tomato", 5, 0), "\n")
    except ValueError as e:
        print(e, "\n")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
