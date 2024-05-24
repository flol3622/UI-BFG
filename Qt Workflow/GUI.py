import os
import sys

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

base_dir = os.path.dirname(os.path.abspath(__file__))


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.join(base_dir, "GUI/layout.ui"), self)
        self.show()

        self.calcButton.clicked.connect(self.calc)

    def calc(self):
        num_pizzas = self.numPizza.value()
        hydra_rate = self.hydraRate.value() if self.hydraBool.isChecked() else 0.75

        flour = 220 / (1 + hydra_rate) * num_pizzas
        water = flour * hydra_rate

        self.resultDisp.setText(f"""Recipe: 
- {int(flour)}g flour
- {int(water)}g water
- {num_pizzas*5}g salt
- {round(num_pizzas*0.1,1)}g yeast
""")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("DEMO")
    sys.exit(app.exec())
