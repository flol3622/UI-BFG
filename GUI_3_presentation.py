import os
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

base_dir = os.getcwd()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.join(base_dir, "GUI/layout.ui"), self)
        self.show()

        # self.calcButton.clicked.connect(self.calculate)

    # def calculate(self):
        num_pizzas = int(self.numPizza.value())
        hydration_rate = float(self.hydraRate.value()) if self.hydraBool.isChecked() else 0.7

        flour = 220 / (1 + hydration_rate) * num_pizzas
        water = flour * hydration_rate

        self.resultDisp.setText(f"""Recipe:
{int(flour)}g flour
{int(water)}g water
{num_pizzas * 5}g salt
{round(num_pizzas * 0.1, 1)}g yeast
        """)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("EROB gui")
    sys.exit(app.exec())
