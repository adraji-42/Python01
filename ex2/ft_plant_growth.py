"""Module to simulate plant growth over a week."""


class Plant:
    """Class representing a plant's life cycle and growth behaviors."""

    def __init__(self, name: str, height: int, p_age: int):
        """Initialize plant with its name, height in cm, and age in days."""
        self.name = name
        self.height = height
        self.p_age = p_age

    def grow(self, cm: int):
        """Increase the plant's height by a specified amount."""
        self.height += cm

    def age(self):
        """Increment the plant's age by one day."""
        self.p_age += 1

    def get_info(self):
        """Return a formatted string containing the plant's current status."""
        return f"{self.name}: {self.height}cm, {self.p_age} days old"


def ft_simulat_week(plants: list):
    """
    Simulate the growth and aging of a list of plants over 7 days.

    Args:
        plants (list): A list of Plant objects to simulate.
    """

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
    Rose = Plant("Rose", 25, 30)
    ft_simulat_week([Rose])


if __name__ == "__main__":
    main()
