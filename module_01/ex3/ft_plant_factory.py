class Plant:
    """
    class Plant
    """
    def __init__(self, name, height, age) -> None:
        """
        Creation of Plant
        """
        self.name: str = name
        self.height: int = height
        self.days_old: int = age

    def get_info(self) -> None:
        """
        Actual values of the plant
        """
        print(f"{self.name} ({self.height}cm, {self.days_old} days)")


if __name__ == "__main__":
    plants: dict = {}
    i: int = 0
    creation_plants: list = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    for name, height, days_old in creation_plants:
        plants[i] = Plant(name, height, days_old)
        i += 1
    print("=== Plant Factory Output ===")
    for i in plants:
        print("Created:", end=' ')
        plants[i].get_info()
    i += 1
    print(f"\nTotal plants created: {i}")
