class Plant:
    """Class representing a plant's life cycle."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a new plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


def main():
    """Create plant instances and print their initial registry status."""

    rose = Plant("Rose", 20, 40)
    orange = Plant("Orange", 12, 120)
    sunflower = Plant("Sunflower", 120, 40)

    print("=== Garden Plant Registry ===")
    print(f"{rose.name}: {rose.height}cm, {rose.age} days old")
    print(f"{orange.name}: {orange.height}cm, {orange.age} days old")
    print(f"{sunflower.name}: {sunflower.height}cm, {sunflower.age} days old")


if __name__ == "__main__":
    main()
