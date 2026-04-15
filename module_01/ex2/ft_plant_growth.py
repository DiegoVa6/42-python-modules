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
        print(f"{self.name}: {self.height}cm, {self.days_old} days old")

    def grow(self) -> None:
        """
        Method to grow the plant +2cm
        """
        self.height += 2

    def age(self) -> None:
        """
        Method to make plant 1 day older
        """
        self.days_old += 1


if __name__ == "__main__":
    p1 = Plant("Rose", 25, 30)
    inheight = 25
    for i in range(7):
        print(f"=== Day {i} ===")
        p1.get_info()
        p1.grow()
        p1.age()
    print(f"Growth this week +{p1.height - inheight}")
