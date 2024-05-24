# simple file selector dialog to select a file using PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QFileDialog

app = QApplication(sys.argv)
file_name, _ = QFileDialog.getOpenFileName()

#  you can even add filters for specific file types:
# file_name, _ = QFileDialog.getOpenFileName(None, "Select a file...", "", "Text files (*.txt);;Markdown files (*.md);;All Files (*)")

print("You selected: ", file_name)