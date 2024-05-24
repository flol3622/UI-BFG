<!-- Qt workflow ~ Philippe Soubrier ~ 24/05/2024 -->
# Qt workflow
Output / executable can be previewed in the [releases]()

If you cloned this repository, make sure the commands in the following sections are executed in this folder. Command to navigate to this folder:
```shell
cd '.\Qt Workflow\'

# terminal shoul look like:
# PS C:\Users\...\UI-BFG\Qt Workflow> 
```

## 1. Setup
This Python code requires the installation of the `auto-py-to-exe` and `pyqt6-tools` packages. You can install them using your own workflow or by using the following setup:

```shell
# Setup
conda create -n UIdemo python=3.8
conda activate UIdemo 

# Extremely fast package installer
pip install uv 
uv pip install auto-py-to-exe pyqt6-tools 
```

## 2. Design
The next step is to create a `.ui` file using the Qt Designer. This file will contain all the UI data to initialize the GUI. You will then be able to change it and interact with it using the Python code (next step).

To open the Qt Designer, you can use the following command in the environment you installed the `pyqt6-tools` package:
```shell
# to enter the conda environment (not needed if you are already in it)
conda activate UIdemo

# to open the Qt Designer
pyqt6-tools designer

# to open the .ui file directly
pyqt6-tools designer .\GUI\layout.ui
```

You can now make your design using the user interface of the Qt Designer. Things you can do in it:
- Start a `main window` project
- Add widgets, layouts, text, input fields, buttons, etc.
- Change the properties of the widgets (size, color, font, etc.) even add custom CSS (or equivalent in Qt (complex))
- Add basic UI interactions (like enabling/disabling widgets with checkboxes)
- Preview your design with `Ctrl + R`
- Save your design as a `.ui` file in the `GUI` folder

## 3. Code
Using Python, you can now control interactions with the UI. The [GUI_base.py](GUI_base.py) file contains the basic code to load the `.ui` file and build your code around it. [GUI.py](GUI.py) is an example of how to use the `GUI_base.py` file to create a simple application such as the Pizza calculator.
> [!NOTE]
> At this stage, you already have a working application. You can run just like you would execute any Python script `python GUI.py`. This means that this stage can keep existing in your development workflow, if for example you want to add little UIs to your scripts to enter complex inputs from the user. Think about a simple file selector in a script, look at [this example](file_selector.py).

## 4. Packaging
The final step is to convert your Python script into an executable. This to send distribute your application to people who do not have Python installed on their computer. The idea is to create a package that contains all the necessary files to run the application, this includes Python itself that is converted to machine code.

To convert your script, you can use the `auto-py-to-exe` package. This package has a user interface that allows you to select the script you want to convert, the options you want to include, and the output folder, the files you need to add, ...

To open the `auto-py-to-exe` interface, you can use the following command in the environment you installed the `auto-py-to-exe` package:
```shell
auto-py-to-exe.exe
```
I recommend using the following options:
- Script location: select the `GUI.py` file
- One File: to create a single executable file
- Console Window: to see the output of the script + potential errors
- Additional Files: to add the `GUI` folder containing the `.ui` file
  - looks like: C:/Users/.../Qt Workflow/GUI | GUI/
- Advanced > name: choose a name for the executable (e.g., `GUI`)

You can also save the command it proposes to you to run it in the terminal. This command will look like:
```shell
pyinstaller --noconfirm --onefile --console --name "GUI" --add-data "./GUI;GUI/"  "./GUI.py"
