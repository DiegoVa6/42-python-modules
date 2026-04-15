import math


def create_position(x, y, z):
    """
    Creates a position based on 3 vales x, y, z
    """
    return (int(x), int(y), int(z))


def parsing_coordinates(string):
    """
    Function to parse a string with 3 values x, y, z
    """
    list_parts = string.split(",")
    if len(list_parts) != 3:
        raise ValueError("Coordinates must be in format 'x,y,z'")
    return create_position(list_parts[0], list_parts[1], list_parts[2])


def euclidean_distance(p1, p2):
    """
    Calculates de euclidean distance between 2 points
    """
    return math.sqrt(
        (p2[0] - p1[0])**2 +
        (p2[1] - p1[1])**2 +
        (p2[2] - p1[2])**2
    )


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    center = create_position(0, 0, 0)
    try:
        a = create_position(10, 20, 5)
        print(f"Position created: {a}")
        print(f"Distance between {center} and {a}: "
              f"{euclidean_distance(a, center):.2f}")
    except ValueError as e:
        print(f"Parsing invalid coordinates: {e}")

    b = None
    try:
        print("\nParsing coordinates: '3,4,0'")
        b = parsing_coordinates("3,4,0")
        print(f"Parsed position: {b}")
        print(f"Distance between {center} and {b}:",
              euclidean_distance(b, center))
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    try:
        print("\nParsing invalid coordinates: 'abc,def,ghi'")
        c = parsing_coordinates("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    if b is not None:
        print("\nUnpacking demonstration:")
        print(f"Player at x={b[0]}, y={b[1]}, z={b[2]}")
        print("Coordinates: X=3, Y=4, Z=0")
