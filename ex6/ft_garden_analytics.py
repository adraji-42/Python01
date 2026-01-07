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

    def type(self):
        return "regular"


class FloweringPlant(Plant):
    """Represents a flower that can bloom."""

    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = True

    def __str__(self):
        status = " (blooming)" if self.is_blooming else ""
        return f"{super().__str__()}, {self.color} flowers{status}"

    def type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    """A specialized flower that holds points."""

    def __init__(self, name: str, height: int, color: str, points: int):
        super().__init__(name, height, color)
        self.points = points

    def __str__(self):
        return f"{super().__str__()}, Prize points: {self.points}"

    def type(self):
        return "prize"


class Garden:
    """Represents a garden containing multiple plants."""

    def __init__(self, owner: str, plants: list[Plant] = None):
        self.owner = owner
        self.plants = plants if plants is not None else []
        self.n_plant = len(plants) if plants is not None else 0
        self.total_growth = 0

    def add_plant(self, plant: Plant):
        """Add a plant and log the action."""
        self.plants += [plant]
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
                if plant.type() == "prize":
                    score += plant.points
            return score

    def __init__(self, garden: Garden):
        self.garden = garden
        GardenManager.gardens += [garden]
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, gardens: dict[str, list[Plant]]):
        network = {}
        for owner in gardens:
            network[owner] = cls(Garden(owner, gardens[owner]))
        return network

    def generate_report(self):
        """Display detailed garden analytics."""
        print(f"=== {self.garden.owner}'s Garden Report ===")
        print("Plants in garden:")
        p_types = {"regular": 0, "flowering": 0, "prize": 0}

        for plant in self.garden.plants:
            print(f"- {plant}")
            p_types[plant.type()] += 1

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

    gardens = {
        "Adam": None,
        "Hamid": [Plant("Small Cactus", 82)]
    }

    network = GardenManager.create_garden_network(gardens)

    network["Adam"].garden.add_plant(Plant("Oak Tree", 100))
    network["Adam"].garden.add_plant(FloweringPlant("Rose", 25, "red"))
    network["Adam"].garden.\
        add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    network["Adam"].garden.help_growth(1)
    print()

    network["Adam"].generate_report()
    print()

    print(f"Height validation test: {Garden.validate_height(10)}")
    print("Garden scores -", end=" ")

    index = 1
    for owner in network:
        score = GardenManager.GardenStats.\
            calculate_score(network[owner].garden.plants)
        last = ", "if index < GardenManager.total_gardens else ""
        print(f"{owner}: {score}", end=last)
        index += 1
    print(f"\nTotal gardens managed: {GardenManager.total_gardens}")


if __name__ == "__main__":
    main()
