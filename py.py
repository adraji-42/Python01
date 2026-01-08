def ft_garden_intro(plant_name: str, plant_height: int, plant_age: int):
    """Display a welcome message and detailed information about a plant."""

    name = plant_name
    height = plant_height
    age = plant_age

    print("=== Welcome to My Garden ===")
    print("Plant :", name)
    print(f"Height: {height}cm")
    print("Age   :", age, "days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    # Calling the intro function with example data
    ft_garden_intro("Rose", 25, 30)
class Plant:
    """Class representing a plant's life cycle."""

    def __init__(self, name: str, height: int, age: int):
        """Initialize a new plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


def main():
    """Create plant instances and print their initial registry status."""

    plants = [
        Plant("Rose", 20, 40),
        Plant("Orange", 12, 120),
        Plant("Sunflower", 120, 40)
    ]

    print("=== Garden Plant Registry ===")
    for plant in plants:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
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
    ft_simulat_week([rose])


if __name__ == "__main__":
    main()
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
        area = (3.14 * (radius ** 2)) // 1
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
        print(f"{self.name} is {self.nutritional}")


def main():
    """Main execution point to showcase different plant types."""

    print("=== Garden Plant Types ===\n")

    # Creating a list of different plant objects (Polymorphism)
    garden = [
        Flower("Lycoris Radiata", 50, 30, "Red"),
        Flower("Blue Spider Lily", 45, 25, "Blue"),
        Tree("Oak", 500, 1825, 50),
        Tree("Spruce", 950, 1100, 5),
        Vegetable("Tomato", 80, 90, "Summer", "rich in vitamin C"),
        Vegetable("Potato", 75, 100, "Summer", "rich in Potassium")
    ]

    # Iterate through the garden and display information for each plant
    for plant in garden:
        plant.display_info()
        print()


if __name__ == "__main__":
    main()
class Plant:
    """Base class representing a general plant."""

    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def grow(self, amount: int):
        """Increase the height of the plant."""
        self.height += amount

    def __str__(self):
        return f"{self.name}: {self.height}cm"


class FloweringPlant(Plant):
    """Represents a flower that can bloom."""

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def __str__(self):
        status = " (blooming)" if self.is_blooming else ""
        return f"{super().__str__()}, {self.color} flowers{status}"


class PrizeFlower(FloweringPlant):
    """A specialized flower that holds points."""

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.points}"


class Garden:
    """Represents a garden containing multiple plants."""

    def __init__(self, owner: str, plants: list[Plant] = None):
        self.owner = owner
        self.plants = plants if plants is not None else []
        self.n_plant = len(self.plants)
        self.total_growth = 0

    def add_plant(self, plant: Plant):
        """Add a plant and log the action."""
        self.plants.append(plant)
        self.n_plant += 1
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_growth(self, amount: int = 1):
        """Trigger growth for all plants in the garden."""
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount
            print(f"{plant.name} grew {amount}cm")

    @staticmethod
    def validate_height(height: int):
        """Utility function to validate height data."""
        return height > 0


class GardenManager:
    """Main system to manage gardens and analytics."""

    gardens = []
    total_gardens = 0

    class GardenStats:
        """Helper class for calculating analytics."""

        @staticmethod
        def calculate_score(plants: list[Plant]):
            """Calculate the total garden score."""
            score = 0
            for plant in plants:
                score += plant.height + 10
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            return score

    def __init__(self, garden: Garden):
        self.garden = garden
        GardenManager.gardens.append(garden)
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, gardens_data: dict[str, list[Plant]]):
        network = {}
        for owner, plants in gardens_data.items():
            network[owner] = cls(Garden(owner, plants))
        return network

    def generate_report(self):
        """Display detailed garden analytics."""
        print(f"=== {self.garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        p_types = {"regular": 0, "flowering": 0, "prize": 0}

        for plant in self.garden.plants:
            print(f"- {plant}")
            if isinstance(plant, PrizeFlower):
                p_types["prize"] += 1
            elif isinstance(plant, FloweringPlant):
                p_types["flowering"] += 1
            else:
                p_types["regular"] += 1

        score = self.GardenStats.calculate_score(self.garden.plants)
        print(f"\nPlants added: {self.garden.n_plant}, "
              f"Total growth: {self.garden.total_growth}cm")
        print(f"Plant types: {p_types['regular']} regular, "
              f"{p_types['flowering']} flowering, "
              f"{p_types['prize']} prize flowers")
        return score


def main():
    """Main execution flow to match desired output."""
    print("=== Garden Management System Demo ===", end="\n\n")

    gardens_data = {
        "Adam": None,
        "Hamid": [Plant("Small Cactus", 82)]
    }

    network = GardenManager.create_garden_network(gardens_data)

    network["Adam"].garden.add_plant(Plant("Oak Tree", 100))
    network["Adam"].garden.add_plant(FloweringPlant("Rose", 25, "red"))
    network["Adam"].garden.add_plant(
        PrizeFlower("Sunflower", 50, "yellow", 10)
    )
    print()

    network["Adam"].garden.help_growth(1)
    print()

    network["Adam"].generate_report()
    print()

    print(f"Height validation test: {Garden.validate_height(10)}")
    print("Garden scores -", end=" ")

    index = 1
    for owner in network:
        score = GardenManager.GardenStats.calculate_score(
            network[owner].garden.plants
        )
        last = ", " if index < GardenManager.total_gardens else ""
        print(f"{owner}: {score}", end=last)
        index += 1
    print(f"\nTotal gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
