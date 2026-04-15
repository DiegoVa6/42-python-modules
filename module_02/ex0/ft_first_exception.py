def check_temperature(temp_str):
    """
    function that checks if the temperature is too high or too low,
    handling errors in the input.
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if (temp > 40):
            print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
            return None
        elif (temp < 0):
            print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
            return None
        print(f"Temperature {temp}°C is perfect for plants!\n")
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")


def test_temperature_input() -> None:
    """
    Function to test temperature errors
    """
    print("=== Garden Temperature Checker ===\n")
    check_temperature("12")
    check_temperature("45")
    check_temperature("-4")
    check_temperature("abc")
    check_temperature("23")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
