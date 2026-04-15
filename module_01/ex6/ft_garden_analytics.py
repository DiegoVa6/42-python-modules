class Plant:
    """
    class Plant.
    """
    def __init__(self, name, height) -> None:
        """
        creation of Pant
        """
        self.name: str = name
        self.height: int = height

    def grow(self, cm=1) -> int:
        """
        method to grow plant, 1cm default
        """
        self.height += cm
        print(f"{self.name} grew {cm}cm")
        return cm

    def info(self) -> str:
        """
        basic information of plant name and height
        """
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """
    class FloweringPlant -> Plant child
    """
    def __init__(self, name, height, color) -> None:
        """
        creation of FloweringPlant -> Plant child
        """
        super().__init__(name, height)
        self.color: str = color

    def info(self) -> str:
        """
        Basic information of FloweringPlant
        """
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"


class PrizeFlower(FloweringPlant):
    """
    class PrizeFlower -> FloweringPlant child -> Plant child
    """
    def __init__(self, name, height, color, points) -> None:
        """
        creation of PrizeFlower -> FloweringPlant child -> Plant child
        """
        super().__init__(name, height, color)
        self.points: int = points

    def info(self) -> str:
        return (
            f"{self.name}: {self.height}cm, "
            f"{self.color} flowers (blooming), "
            f"Prize points: {self.points}"
            )


class GardenManager:
    """
    class GardenManager
    """
    class GardenStats:
        def __init__(self) -> None:
            """
            creation of GardenStats, inside GardenManager
            """
            self.total_plants: int = 0
            self.total_growth: int = 0

        def register_plant(self) -> None:
            """
            new plant registered
            """
            self.total_plants += 1

        def register_growth(self, cm) -> None:
            """
            register the growth
            """
            self.total_growth += cm

        def plant_types_summary(self, plants) -> str:
            """
            get summary of all your plants
            """
            regular = flowering = prize = 0
            for p in plants:
                if isinstance(p, PrizeFlower):
                    prize += 1
                elif isinstance(p, FloweringPlant):
                    flowering += 1
                else:
                    regular += 1
            return (f"Plant types: {regular} regular, "
                    f"{flowering} flowering, {prize} prize flowers"
                    )

        def summary(self) -> str:
            """
            summary of stats
            """
            return (f"Plants added: {self.total_plants}, "
                    f"Total growth: {self.total_growth}cm"
                    )

    def __init__(self) -> None:
        """
        creation of GardenManager
        """
        self.gardens = {}

    def add_garden(self, owner) -> None:
        """
        add garden to actual gardens
        """
        if owner not in self.gardens:
            self.gardens[owner] = {
                "plants": [],
                "stats": GardenManager.GardenStats()
                }

    def add_plant(self, owner, plant) -> None:
        """
        add plant to owner's garden
        """
        self.gardens[owner]["plants"].append(plant)
        self.gardens[owner]["stats"].register_plant()
        print(f"Added {plant.name} to {owner}'s garden")

    def help_grow(self, owner, cm=1) -> None:
        """
        helps grow every plant in owner's garden
        """
        if owner not in self.gardens:
            print(f"Garden '{owner}' not found")
            return
        for plant in self.gardens[owner]["plants"]:
            grown = plant.grow(cm)
            self.gardens[owner]["stats"].register_growth(grown)

    def garden_report(self, owner) -> None:
        """
        report of garden's information
        """
        if owner not in self.gardens:
            print(f"Garden '{owner}' not found")
            return
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.gardens[owner]["plants"]:
            print(f"- {plant.info()}")
        print(self.gardens[owner]["stats"].summary())
        stats = self.gardens[owner]["stats"]
        plants = self.gardens[owner]["plants"]
        print(stats.plant_types_summary(plants))

    @staticmethod
    def is_valid_height(h) -> bool:
        """
        method to check if height is valid
        """
        return h >= 0

    @classmethod
    def create_garden_network(cls):
        """
        create a basic garden network with to people, Alice and bob
        """
        gm = cls()
        gm.add_garden("Alice")
        gm.add_garden("Bob")
        return gm


if __name__ == "__main__":
    print("=== Garden Management System Demo ===\n")
    gm = GardenManager.create_garden_network()

    oak: Plant = Plant("Oak Tree", 100)
    rose: FloweringPlant = FloweringPlant("Rose", 25, "red")
    sunflower: PrizeFlower = PrizeFlower("Sunflower", 50, "yellow", 10)

    gm.add_plant("Alice", oak)
    gm.add_plant("Alice", rose)
    gm.add_plant("Alice", sunflower)

    print("\nAlice is helping all plants grow...")
    gm.help_grow("Alice", 1)
    gm.garden_report("Alice")

    print(f"\nHeight validation test: {GardenManager.is_valid_height(10)}")

    alice_score = gm.gardens["Alice"]["stats"].total_growth + 200
    bob_score = 92
    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")

    print(f"Total gardens managed: {len(gm.gardens)}")
