import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox

class PizzaCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Pizza Calculator")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.num_pizzas_label = QLabel("How many pizzas?")
        self.num_pizzas_input = QLineEdit()

        self.hydration_rate_label = QLabel("Hydration rate (default is 0.7):")
        self.hydration_rate_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        layout.addWidget(self.num_pizzas_label)
        layout.addWidget(self.num_pizzas_input)
        layout.addWidget(self.hydration_rate_label)
        layout.addWidget(self.hydration_rate_input)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate(self):
        try:
            num_pizzas = int(self.num_pizzas_input.text())

            hydration_input = self.hydration_rate_input.text()
            hydration_rate = float(hydration_input) if hydration_input else 0.7

            # flour + water per pizza = 220g
            flour = 220 / (1 + hydration_rate) * num_pizzas
            water = flour * hydration_rate

            recipe = f"Recipe:\n{int(flour)}g flour\n{int(water)}g water\n{num_pizzas * 5}g salt\n{num_pizzas * 0.1}g yeast"

            QMessageBox.information(self, "Pizza Recipe", recipe)

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PizzaCalculator()
    window.show()
    sys.exit(app.exec())
