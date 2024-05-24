from prompt_toolkit.shortcuts import message_dialog, input_dialog

def main():
    # Display a welcome message
    message_dialog(title="Pizza Calculator", text="Welcome to the Pizza Calculator!").run()

    # Get number of pizzas
    num_pizzas_input = input_dialog(title="Number of Pizzas", text="How many pizzas? ").run()
    if num_pizzas_input is None:
        return
    num_pizzas = int(num_pizzas_input)

    # Get hydration rate, default to 0.7 if not provided
    hydration_input = input_dialog(title="Hydration Rate", text="Hydration rate (default is 0.7): ").run()
    if hydration_input is None:
        return
    hydration_rate = float(hydration_input) if hydration_input else 0.7

    # Calculate flour and water
    flour = 220 / (1 + hydration_rate) * num_pizzas
    water = flour * hydration_rate

    # Display the recipe
    recipe_message = (
        f"Recipe:\n"
        f"{int(flour)}g flour\n"
        f"{int(water)}g water\n"
        f"{num_pizzas * 5}g salt\n"
        f"{num_pizzas * 0.1}g yeast"
    )
    message_dialog(title="Pizza Recipe", text=recipe_message).run()

if __name__ == "__main__":
    main()
