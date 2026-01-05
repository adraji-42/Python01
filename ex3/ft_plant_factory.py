class Plant:
    """Class representing a plant's life cycle and growth behaviors."""

    plants = []
    totale = 0

    def __init__(self, name: str, height: int, p_age: int):
        """Initialize plant with its name, height in cm, and age in days."""
        self.name = name
        self.height = height
        self.p_age = p_age
        Plant.plants += [self]
        Plant.totale += 1

    def get_info(self):
        """Return a formatted string containing the plant's current status."""
        return f"{self.name}: {self.height}cm, {self.p_age} days old"


def main():
    """Entry point of the script."""

    Plant("Rose", 25, 30)
    Plant("Oak", 200, 365)
    Plant("Fern", 15, 120)
    Plant("Cactus", 5, 90)
    Plant("Sunflower", 80, 45)

    print("=== Plant Factory Output ===")

    for plant in Plant.plants:
        print(f"Created: {plant.get_info()}")

    print(f"\nTotal plants created: {Plant.totale}")


if __name__ == "__main__":
    main()
