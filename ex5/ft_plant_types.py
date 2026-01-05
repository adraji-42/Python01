class Plant:
    """
    A class representing a plant with protected data.
    Ensures data integrity through validation.
    """

    def __init__(self, name: str):
        self.name = name
        self._height = 0
        self._age = 0

    def get_height(self):
        """Returns the current height."""
        return self._height

    def set_height(self, value):
        """Validates and sets the height."""
        if value < 0:
            print(f"Invalid operation attempted: height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = value

    def get_age(self):
        """Returns the current age."""
        return self._age

    def set_age(self, value):
        """Validates and sets the age."""
        if value < 0:
            print(f"Invalid operation attempted: age {value} days [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self._age = value


class Flower(Plant):
    """Specialized plant type: Flower."""

    def __init__(self, name: str, height: int, age: int, color: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.color = color

    def bloom(self):
        """Prints a blooming message."""
        print(f"{self.name} is blooming beautifully!\n")

    def display_info(self):
        """Prints flower specific info."""
        print(f"{self.name} (Flower): {self.get_height()}cm,",
              f"{self.get_age()} days, {self.color} color")
        self.bloom()


class Tree(Plant):
    """Specialized plant type for trees with strict logic."""

    def __init__(self, name: str, height: int, age: int, trunk_diameter: int):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.set_trunk_d(trunk_diameter)

        if self.get_height() > 0 and self._trunk_d == 0:
            print(f"NOTICE: {self.name} created with 0 diameter.",
                  "Please update trunk diameter later.")

    def set_trunk_d(self, value):
        """Strict validation for diameter."""
        if value < 0:
            print(f"Error: Negative diameter {value}cm [REJECTED]")
            self._trunk_d = 0
            return

        if value > 0 and self.get_height() == 0:
            print(f"Logic Error: Cannot set diameter {value}cm",
                  f"for {self.name} because height is 0.")
            self._trunk_d = 0
        else:
            self._trunk_d = value

    def produce_shade(self):
        """Calculates shade area."""
        if self.get_height() <= 0 or self._trunk_d <= 0:
            print(f"{self.name} is too small to provide shade.")
            return
        radius = self._trunk_d / 10
        area = 3.14 * (radius ** 2)
        print(f"{self.name} provides {area // 1} square meters of shade\n")

    def display_info(self):
        """Prints tree specific information."""
        print(f"{self.name} (Tree): {self.get_height()}cm, "
              f"{self.get_age()} days, {self._trunk_d}cm diameter")
        if self.get_height() > 0 and self._trunk_d == 0:
            print("Warning: Tree has height but trunk diameter is zero!")
            return
        self.produce_shade()


class Vegetable(Plant):

    def __init__(self, name: str, height: int, age: int,
                 season: str, nutritional: str):
        super().__init__(name)
        self.set_height(height)
        self.set_age(age)
        self.season = season
        self.nutritional = nutritional

    def display_info(self):
        """Prints flower specific info."""
        print(f"{self.name} (Vegetable): {self.get_height()}cm,",
              f"{self.get_age()} days, {self.season} harvest")
        print(f"{self.name} is {self.nutritional}\n")


def main():
    """Main function to demonstrate the security system."""
    print("=== Garden Security System ===\n")

    flower1 = Flower("Lycoris Radiata", 50, 30, "Red")
    flower1.display_info()
    flower2 = Flower("Blue Spider Lily", 45, 25, "Red")
    flower2.display_info()

    tree1 = Tree("Oak", 500, 1825, 50)
    tree1.display_info()
    tree2 = Tree("spruce", 950, 1100, 5)
    tree2.display_info()

    vegetable1 = Vegetable("Tomato", 80, 90, "summer", "rich in vitamin C")
    vegetable1.display_info()
    vegetable1 = Vegetable("Potato", 75, 100, "summer", "rich in Potassium")
    vegetable1.display_info()


if __name__ == "__main__":
    main()
