from prompt_toolkit.application import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import Label, Button, Dialog, TextArea


def main():
    def get_pizza_details():
        try:
            num_pizzas = int(num_pizzas_input.text)
            hydration_rate = float(hydration_input.text) if hydration_input.text else 0.7

            flour = 220 / (1 + hydration_rate) * num_pizzas
            water = flour * hydration_rate

            recipe = (
                f"Recipe:\n"
                f"{int(flour)}g flour\n"
                f"{int(water)}g water\n"
                f"{num_pizzas * 5}g salt\n"
                f"{num_pizzas * 0.1}g yeast"
            )
            result_area.text = recipe
        except ValueError:
            result_area.text = "Invalid input. Please enter numeric values."

    # Create widgets
    welcome_label = Label(text="Welcome to the Pizza Calculator!", dont_extend_height=True)
    num_pizzas_input = TextArea(height=1, prompt="How many pizzas? ")
    hydration_input = TextArea(height=1, prompt="Hydration rate (default is 0.7): ")
    result_area = TextArea(focusable=False, read_only=True, dont_extend_height=True)

    calculate_button = Button(text="Calculate", handler=get_pizza_details)
    exit_button = Button(text="Exit", handler=lambda: app.exit())

    # Layout
    dialog = Dialog(
        title="Pizza Calculator",
        body=HSplit([
            welcome_label,
            num_pizzas_input,
            hydration_input,
            result_area,
        ]),
        buttons=[calculate_button, exit_button]
    )

    # Application
    layout = Layout(dialog)
    app = Application(layout=layout, full_screen=True)

    app.run()


if __name__ == "__main__":
    main()
