def main():
    print("Welcome to the Pizza Calculator!")

    num_pizzas = int(input("How many pizzas? "))

    hydration_input = input("Hydration rate (default is 0.7): ")
    hydration_rate = float(hydration_input) if hydration_input else 0.7

    # flour + water per pizza = 220g
    flour = 220 / (1 + hydration_rate) * num_pizzas
    water = flour * hydration_rate

    print("Recipe:")
    print(f"{int(flour)}g flour")
    print(f"{int(water)}g water")
    print(f"{num_pizzas * 5}g salt")
    print(f"{num_pizzas * 0.1}g yeast")

    # wait for user input before closing
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
