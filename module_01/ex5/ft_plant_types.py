class Plant:
    """
    class Plant
    """
    def __init__(self, name, height, age) -> None:
        """
        creation of Plant
        """
        self.name: str = name
        self.height: int = height
        self.days_old: int = age


class Flower(Plant):
    """
    class Flower -> Plant child
    """
    def __init__(self, name, height, age, color) -> None:
        """
        creation of Flower
        """
        super().__init__(name, height, age)
        self.color: str = color

    def bloom(self) -> None:
        """
        method to show blooming
        """
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    class Tree -> Plant child
    """
    def __init__(self, name, height, age, trunk_diameter) -> None:
        """
        creation of Tree
        """
        super().__init__(name, height, age)
        self.trunk_diameter: int = trunk_diameter

    def produce_shade(self) -> None:
        """
        Shade produced by tree
        """
        print(f"{self.name} provides {self.trunk_diameter * self.height} "
              f"square meters of shade")


class Vegetable(Plant):
    """
    class vegetable -> Plant child
    """
    def __init__(self, name, height, age,
                 harvest_season, nutritional_value) -> None:
        """
        creation of vegetable
        """
        super().__init__(name, height, age)
        self.harvest_season: str = harvest_season
        self.nutritional_value: str = nutritional_value


if __name__ == "__main__":
    rose: Flower = Flower("Rose", 25, 30, "red")
    oak: Tree = Tree("oak", 500, 1825, 50)
    tomatoe: Vegetable = Vegetable("tomatoe", 80, 90, "summer", "vitamin C")
    print("=== Garden Plant Types ===\n")

    print(rose.name, type(rose).__name__, f": {rose.height}cm, "
          f"{rose.days_old} days, {rose.color} color")
    rose.bloom()
    print()

    print(oak.name, type(oak).__name__, f": {oak.height}cm, {oak.days_old}"
          f" days, {oak.trunk_diameter} diameter")
    oak.produce_shade()
    print()

    print(tomatoe.name, type(tomatoe).__name__, f": {tomatoe.height}cm, "
          f"{tomatoe.days_old}, {tomatoe.harvest_season} harvest")
    print(tomatoe.name, "is rich in", tomatoe.nutritional_value)
