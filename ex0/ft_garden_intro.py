def ft_garden_intro(plant_nam: str, height: int, age: int):
    """Display a welcome message and detailed information about a plant."""

    print("=== Welcome to My Garden ===")
    print("Plant :", plant_nam)
    print(f"Height: {height}cm")
    print("Age   :", age, "days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    # Calling the intro function with example data
    ft_garden_intro("Rose", 25, 30)
