import PySimpleGUI as sg

def calculate_pizza(num_pizzas, hydration_rate):
    flour = 220 / (1 + hydration_rate) * num_pizzas
    water = flour * hydration_rate
    salt = num_pizzas * 5
    yeast = num_pizzas * 0.1
    
    return int(flour), int(water), salt, yeast

def main():
    layout = [
        [sg.Text("Welcome to the Pizza Calculator!")],
        [sg.Text("How many pizzas?"), sg.InputText(key='-NUM_PIZZAS-')],
        [sg.Text("Hydration rate (default is 0.7):"), sg.InputText(key='-HYDRATION_RATE-')],
        [sg.Button("Calculate"), sg.Button("Exit")],
        [sg.Text("Recipe:"), sg.Text("", size=(40, 1), key='-RECIPE-')]
    ]

    window = sg.Window("Pizza Calculator", layout)

    while True:
        event, values = window.read()
        
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        
        if event == "Calculate":
            try:
                num_pizzas = int(values['-NUM_PIZZAS-'])
                hydration_input = values['-HYDRATION_RATE-']
                hydration_rate = float(hydration_input) if hydration_input else 0.7
                
                flour, water, salt, yeast = calculate_pizza(num_pizzas, hydration_rate)
                
                recipe = f"{flour}g flour | {water}g water | {salt}g salt | {yeast}g yeast"
                window['-RECIPE-'].update(recipe)
            except ValueError:
                window['-RECIPE-'].update("Invalid input. Please enter valid numbers.")

    window.close()

if __name__ == "__main__":
    main()
