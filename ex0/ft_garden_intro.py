def ft_garden_intro():
    """Display a welcome message and detailed information about a plant."""

    name = "Rose"
    height = 25
    age = 30

    print("=== Welcome to My Garden ===")
    print("Plant :", name)
    print(f"Height: {height}cm")
    print("Age   :", age, "days", end="\n\n")
    print("=== End of Program ===")


if __name__ == "__main__":
    # Calling the intro function with example data
    ft_garden_intro()
