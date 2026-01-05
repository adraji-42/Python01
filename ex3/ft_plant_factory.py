class Plant:
    """Class representing a plant's life cycle and growth behaviors."""

    def __init__(self, name: str, height: int, p_age: int):
        """Initialize plant with its name, height in cm, and age in days."""
        self.name = name
        self.height = height
        self.p_age = p_age

    def get_info(self):
        """Return a formatted string containing the plant's current status."""
        return f"{self.name}: {self.height}cm, {self.p_age} days old"


def main():
    """Entry point of the script."""
    # List of plant objects
    my_plants = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Fern", 15, 120),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45)
    ]

    print("=== Plant Factory Output ===")

    totale = 0
    for plant in my_plants:
        print(f"Created: {plant.get_info()}")
        totale += 1

    # Accessing the class attribute for total count
    print(f"\nTotal plants created: {totale}")


if __name__ == "__main__":
    main()
