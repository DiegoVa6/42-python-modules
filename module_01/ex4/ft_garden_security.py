class SecurePlant:
    """
    class Secure plant
    """
    def __init__(self, name, height=0, age=0) -> None:
        """
        Creation of secure plant
        """
        self.name: str = name
        self._height: int = 0
        self._age: int = 0
        self.set_height(height)
        self.set_age(age)
        print(f"Plant created: {self.name}\n")

    def get_info(self) -> None:
        """
        Actual values of secure plant
        """
        print(f"Current plant: {self.name} ({self._height}cm, "
              f"{self._age} days)")

    def set_height(self, new_height) -> None:
        """
        setter for the height
        """
        if (new_height < 0):
            print(f"Invalid operation attempted: height "
                  f"{new_height}cm [REJECTED]")
            print("Security: Negative height rejected\n")
        else:
            self._height = new_height
            print(f"Height updated: {self._height}cm [OK]")

    def get_height(self) -> int:
        """
        getter for the height
        """
        return self._height

    def set_age(self, new_age) -> None:
        """
        setter for the age
        """
        if (new_age < 0):
            print("New age can't be less than 0")
        else:
            self._age = new_age
            print(f"Age updated: {self._age} days [OK]")

    def get_age(self) -> int:
        """
        getter for the age
        """
        return self._age


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1: SecurePlant = SecurePlant("Rose")
    p1.set_age(15)
    p1.set_height(25)
    p1.get_info()
    print()
    p1.set_age(-12)
    p1.get_info()
    print()
    p1.set_height(-19)
    p1.get_info()
