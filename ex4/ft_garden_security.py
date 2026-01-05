class SecurePlant:
    """A class representing a plant with protected data."""

    def __init__(self, name: str, height: int, p_age: int):
        self.name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self.name}")

        self.set_height(height)
        self.set_age(p_age)

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
            print(f"Height updated: {value}cm [OK]")

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
            print(f"Age updated: {value} days [OK]")


def main():
    """Main function to demonstrate the security system."""

    print("=== Garden Security System ===")

    plant = SecurePlant("Rose", 25, 30)

    plant.set_age(-1)

    print(f"Current plant: {plant.name} "
          f"({plant.get_height()}cm, {plant.get_age()} days)")


if __name__ == "__main__":
    main()
