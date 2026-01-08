class Plant:
    """Base class representing a general plant in the garden."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize basic plant attributes."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Represents a flower, inheriting from Plant."""

    def __init__(self, name: str, height: int, age: int, color: str):
        """Initialize flower with an additional color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        """Displays a message about the flower blooming."""
        print(f"{self.name} is blooming beautifully!")

    def display_info(self):
        """Prints detailed information about the flower."""
        print(f"{self.name} (Flower): {self.height}cm, "
              f"{self.age} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    """Represents a tree with shade calculation capabilities."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        """Initialize tree with trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_d = trunk_diameter

    def produce_shade(self):
        """Calculates and prints the shade area based on trunk diameter."""

        radius = self.trunk_d / 10
        area = (3.14 * (radius ** 2))
        # :.0f is used to display the float as an integer in the output
        print(f"{self.name} provides {area:.0f} square meters of shade")

    def display_info(self):
        """Prints tree-specific details and shade information."""
        print(f"{self.name} (Tree): {self.height}cm, "
              f"{self.age} days, {self.trunk_d}cm diameter")
        self.produce_shade()


class Vegetable(Plant):
    """Represents a vegetable with seasonal and nutritional info."""

    def __init__(self, name: str, height: int, age: int,
                 season: str, nutritional: str):
        """Initialize vegetable with season and nutritional value."""
        super().__init__(name, height, age)
        self.season = season
        self.nutritional = nutritional

    def display_info(self):
        """Prints vegetable-specific information."""
        print(f"{self.name} (Vegetable): {self.height}cm, "
              f"{self.age} days, {self.season} harvest")
        print(f"{self.name} is rich in {self.nutritional}")


def main():
    """Main execution point to showcase different plant types."""

    print("=== Garden Plant Types ===\n")

    # Creating a list of different plant objects (Polymorphism)
    garden = [
        Flower("Lycoris Radiata", 50, 30, "Red"),
        Flower("Blue Spider Lily", 45, 25, "Blue"),
        Tree("Oak", 500, 1825, 50),
        Tree("Spruce", 950, 1100, 5),
        Vegetable("Tomato", 80, 90, "Summer", "vitamin C"),
        Vegetable("Potato", 75, 100, "Summer", "Potassium")
    ]

    # Iterate through the garden and display information for each plant
    for plant in garden:
        plant.display_info()
        print()


if __name__ == "__main__":
    main()
