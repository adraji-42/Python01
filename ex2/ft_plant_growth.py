class Plant:
    """Class representing a plant's life cycle and growth behaviors."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize plant with its name, height in cm, and age in days."""
        self.name = name
        self.height = height
        self.ro_age = age

    def grow(self, cm: int):
        """Increase the plant's height by a specified amount."""
        self.height += cm

    def age(self):
        """Increment the plant's age by one day."""
        self.ro_age += 1

    def get_info(self):
        """Return a formatted string containing the plant's current status."""
        return f"{self.name}: {self.height}cm, {self.ro_age} days old"


def ft_simulat_week(plants: list[Plant]):
    """Simulate the growth and aging of a list of plants over 7 days."""

    height_day1 = {}

    print("=== Day 1 ===")
    for plant in plants:
        # Store the initial height to calculate growth later
        height_day1[plant.name] = plant.height
        print(plant.get_info())

    # Counter for the while loop to simulate 6 additional days
    i = 0
    while i < 6:
        for plant in plants:
            plant.grow(1)
            plant.age()
        i += 1

    print("=== Day 7 ===")
    for plant in plants:
        print(plant.get_info())
        # Calculate the difference between Day 7 and Day 1 heights
        growth = plant.height - height_day1[plant.name]
        print(f"Growth this week: +{growth}cm")


def main():
    """Entry point of the script to initialize and run the simulation."""

    rose = Plant("Rose", 25, 30)
    sunflower = Plant("Sunflower", 50, 45)
    ft_simulat_week([rose, sunflower])


if __name__ == "__main__":
    main()
