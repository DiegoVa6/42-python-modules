class GardenError(Exception):
    """
    Base exception for all garden-related errors.
    """
    pass


class PlantError(GardenError):
    """
    Raised for plant-related input/management errors.
    """
    pass


class InputError(GardenError):
    """
    Raised when user input is invalid.
    """
    pass


class WaterError(GardenError):
    """
    Raised when watering cannot be performed.
    """
    pass


class HealthError(GardenError):
    """
    class HealthError -> GardenError's child
    """
    def __init__(self, plant_name, message) -> None:
        """
        Store plant name plus a useful error message.
        """
        super().__init__(message)
        self.plant_name = plant_name


class TankError(GardenError):
    """
    class TankError -> GardenError's child
    """
    pass


class Plant:
    """
    Docstring for Plant, class with name, water_level and sunlight_hours
    """
    def __init__(self, name, water_level, sunlight_hours):
        """
        Create a plant and validate its attributes.
        """
        if name is None or name == "":
            raise InputError("Plant name cannot be empty!")
        if water_level < 1 or water_level > 10:
            raise InputError(f"Error: Water level {water_level} not in (0-10)")
        if sunlight_hours < 2 or sunlight_hours > 12:
            raise InputError(f"Error: Sunlight hours "
                             f"{sunlight_hours} not in (2-12)")
        self.name: str = name
        self.water_level: int = water_level
        self.sunlight_hours: int = sunlight_hours

    def water(self, amount=1):
        """
        Docstring for water
        Method to water plants if needed
        """
        if self.water_level >= 10:
            raise WaterError("No need to water plant")
        if self.water_level + amount > 10:
            self.water_level = 10
        else:
            self.water_level += amount
        print(f"Watering {self.name} - success")

    def force_bad_water_level(self):
        """
        Force an invalid water level to demonstrate HealthError.
        """
        self.water_level = 15

    def health(self):
        """
        Docstring for health
        Checks plant health
        """
        if self.water_level < 1:
            raise HealthError(self.name, f"Water level {self.water_level} "
                              f"is too low (min 0)")
        if self.water_level > 10:
            raise HealthError(self.name, f"Water level {self.water_level} "
                              f"is too high (max 10)")
        if self.sunlight_hours < 2:
            raise HealthError(self.name, f"sunlight_hours "
                              f"{self.sunlight_hours} is too low (min 2)")
        if self.sunlight_hours > 12:
            raise HealthError(self.name, f"sunlight_hours "
                              f"{self.sunlight_hours} is too high (max 12)")
        print(f"{self.name}: healthy (water: "
              f"{self.water_level}, sun {self.sunlight_hours})")


class GardenManager:
    """
    Manages gardens (owners), plants, and a water tank.
    """
    def __init__(self):
        """
        Initialize the manager with empty gardens and an empty tank.
        """
        self.gardens = {}
        self.tank_water = 0

    def add_garden(self, owner):
        """
        Docstring for add_garden
        to add a new garden
        """
        if owner is None or owner == "":
            raise InputError("Owner name can not be empty")
        if owner not in self.gardens:
            self.gardens[owner] = {"plants": []}

    def add_plant(self, owner, plant):
        """
        Docstring for add_plant
        To add a new plant to a owner's garden
        """
        if owner is None or owner == "":
            raise InputError("Owner name cannot be empty!")
        if owner not in self.gardens:
            raise InputError("Garden owner not found")
        if plant is None:
            raise PlantError("Plant cannot be None")

        self.gardens[owner]["plants"].append(plant)
        print(f"Added {plant.name} successfully")

    def open_watering_system(self):
        """
        Open watering system or raise TankError if tank is empty.
        """
        if self.tank_water <= 0:
            raise TankError("Not enough water in tank")
        print("Opening watering system")

    def water_plants(self, owner, plant_name, amount=1):
        """
        Docstring for watering_plant
        To water a plant with an amount of water
        """
        if owner not in self.gardens:
            raise InputError("Garden owner not found")
        try:
            self.open_watering_system()
            for p in self.gardens[owner]["plants"]:
                if self.tank_water < amount:
                    raise TankError("Not enough water in tank")
                self.tank_water = self.tank_water - amount
                p.water(amount)
        except GardenError:
            raise
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, owner):
        """
        Check health for all plants of an owner (may raise HealthError)
        """
        if owner not in self.gardens:
            raise InputError("Garden owner not found")
        for p in self.gardens[owner]["plants"]:
            p.health()

    def force_bad_health(self, owner, plant_name):
        """
        Force a specific plant into an unhealthy state (demo helper)
        """
        if owner not in self.gardens:
            raise InputError("Garden owner not found")
        for p in self.gardens[owner]["plants"]:
            if p.name == plant_name:
                p.force_bad_water_level()
                return
        raise PlantError("Plant not found")


def test_garden_management():
    print("=== Garden Management System ===\n")
    print("Adding plants to garden...")
    gm = GardenManager()
    gm.add_garden("Alice")
    try:
        gm.add_plant("Alice", Plant("tomatoe", 5, 10))
        gm.add_plant("Alice", Plant("lettuce", 4, 8))
        gm.add_plant("Alice", Plant(None, 2, 9))
    except GardenError as e:
        print(f"Error adding plant: {e}")

    print()
    print("Watering plants...")
    gm.tank_water = 10
    try:
        gm.water_plants("Alice", 1)
    except GardenError as e:
        print(f"Watering error: {e}")

    print("\nChecking plant health...")
    gm.force_bad_health("Alice", "lettuce")
    try:
        gm.check_plant_health("Alice")
    except HealthError as e:
        print(f"Error checking {e.plant_name}: {e}")

    print("\nTesting error recovery...")
    gm.tank_water = 0
    try:
        gm.open_watering_system()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
