import os
import sys

# import the necessary modules
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication

# get the base directory of the file, important for the packaging,
#  so that the program can find files in its package,
#  such as the layout.ui file
base_dir = os.path.dirname(os.path.abspath(__file__))

class Ui(QtWidgets.QMainWindow): 
    # initialize the GUI, load the layout and do the necessary setup
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi(os.path.join(base_dir, "GUI/layout.ui"), self)
        self.show()

        # implement your code here

    def example_function(self):
        # implement functions that happen after initial load here
        pass

def example_function():
    # implement functions do not require access to the GUI here
    #  ! NOT code related to your algorithm !
    #  ! keep your algorithm in a separate file / folder !
    pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Ui()
    window.setWindowTitle("DEMO") # set the window title
    sys.exit(app.exec())
