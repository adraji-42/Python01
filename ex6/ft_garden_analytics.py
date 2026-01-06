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
        status = ""
        if self.is_blooming:
            status = " (blooming)"
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

    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []
        self.n_plant = 0
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
                score += plant.height
                if isinstance(plant, PrizeFlower):
                    score += plant.points
            return score

    def __init__(self, garden: Garden):
        self.garden = garden
        GardenManager.gardens += [garden]
        GardenManager.total_gardens += 1

    @classmethod
    def create_garden_network(cls, owners: list[str]):
        """Class method to create multiple managers for Garden objects."""
        return [cls(Garden(owner)) for owner in owners]

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
        print()

        score = self.GardenStats.calculate_score(self.garden.plants)
        print(f"Plants added: {self.garden.n_plant}, "
              f"Total growth: {self.garden.total_growth}cm")
        print(f"Plant types: {p_types['regular']} regular, "
              f"{p_types['flowering']} flowering, "
              f"{p_types['prize']} prize flowers")
        return score


def main():
    """Main entry point of the script."""
    print("=== Garden Management System Demo ===", end="\n\n")

    chaos_garden = Garden("Chaos")
    chaos_manager = GardenManager(chaos_garden)

    chaos_garden.add_plant(Plant("Oak tree", 100))
    chaos_garden.add_plant(FloweringPlant("Rose", 25, "red"))
    chaos_garden.add_plant(PrizeFlower("Sunflower", 50, "yellow", 10))
    print()

    chaos_garden.help_growth()
    print()

    chaos_score = chaos_manager.generate_report()
    print()

    print(f"Total Garden Score: {chaos_score}")


if __name__ == "__main__":
    main()
