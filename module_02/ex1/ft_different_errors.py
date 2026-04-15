def garden_operations(option):
    """
    Function to produce errors needed
    """
    if option == 0:
        return int("abc")
    if option == 1:
        return 1/0
    if option == 2:
        f = open("missing.txt", "r")
        return f
    if option == 3:
        dictionary = {}
        return (dictionary["missing_plant"])


def test_error_types() -> None:
    """
    Function to handle exceptions when produced
    """
    print("=== Garden Error Types Demo ===\n")
    try:
        print("Testing ValueError...")
        garden_operations(0)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        garden_operations(1)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        garden_operations(2)
    except FileNotFoundError:
        print("Caught KeyError: No such file 'missing_plant'\n")

    try:
        print("Testing KeyError...")
        garden_operations(3)
    except KeyError:
        print("Caught KeyError: 'missing_plant'\n")

    print("Testing multiple errors together...")
    try:
        garden_operations(0)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
