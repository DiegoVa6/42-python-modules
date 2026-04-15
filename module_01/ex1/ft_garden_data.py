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
        self.age: int = age

    def get_info(self) -> None:
        """
        print of actual values in plant
        """
        print(f"{self.name}: {self.height}cm, {self.age} days old")


if __name__ == "__main__":
    plant1 = Plant("Rose", 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    plant1.get_info()
    plant2.get_info()
    plant3.get_info()
