"""Module to introduce garden plants and their status."""


def ft_garden_intro(plant_nam: str, height: int, age: int):
    """
    Display a welcome message and detailed information about a plant.

    Args:
        plant_nam (str): The name of the plant.
        height (int): The height of the plant in centimeters.
        age (int): The age of the plant in days.
    """
    print("=== Welcome to My Garden ===")
    print("Plant :", plant_nam)
    print(f"Height: {height}cm")
    print("Age   :", age, "days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    # Calling the intro function with example data
    ft_garden_intro("Rose", 25, 30)
