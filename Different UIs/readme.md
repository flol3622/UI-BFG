<!-- Different UIs ~ Philippe Soubrier ~ 24/05/2024 -->
# 📊 Comparison of Different Types of UIs

## 📝 Summary
This table presents a focused evaluation of user interfaces based on aspects critical to developers and users. For developers, it discusses implementation complexity, documentation, flexibility of UI layout, and cross-platform potential. For users, it focuses on ease of use. Each type of UI offers different advantages and challenges, catering to varied needs and expertise levels.

> [!TIP]
> For academic code, such as the ones written by the BFG group, the CLI and GUI UIs are highly recommended. Check out the [CLI example](CLI.py) and [GUI example](GUI.py) | [GUI workflow with Qt](../Qt%20Workflow).

| Feature / UI Type            | Command Line Interface (CLI) | Text-based User Interface (TUI) | Graphical User Interface (GUI) | Web User Interface (Web UI) |
| ---------------------------- | ---------------------------- | ------------------------------- | ------------------------------ | --------------------------- |
| **Developer Perspective**    |                              |                                 |                                |                             |
| Implementation Complexity    | ⭐                           | ⭐⭐⭐                          | ⭐⭐⭐                         | ⭐⭐⭐⭐⭐                  |
| Implementation Documentation | ⭐⭐⭐⭐⭐                   | ⭐                              | ⭐⭐⭐                         | ⭐⭐⭐⭐                    |
| Flexibility (UI Layout)      | ⭐                           | ⭐⭐                            | ⭐⭐⭐⭐⭐                     | ⭐⭐⭐⭐⭐                  |
| Cross-platform Potential     | ⭐⭐⭐⭐                     | ⭐⭐⭐⭐                        | ⭐⭐⭐                         | ⭐⭐⭐⭐⭐                  |
| **User Perspective**         |                              |                                 |                                |                             |
| Ease of Use (for User)       | ⭐⭐                         | ⭐⭐⭐                          | ⭐⭐⭐⭐                       | ⭐⭐⭐⭐⭐                  |

> [!NOTE]  
> Executable versions of the proposed scripts are available in the [releases]()

## 📖 Full Description

### 1. Command Line Interface (CLI)

- **Definition**: A text-based interface used to interact with software and operating systems.
- **Pros**:
  - Fast and efficient for experienced users.
  - Native to most programming languages.
  - Easy to implement.
- **Cons**:
  - Not user-friendly for beginners.
  - Not visually appealing.
  - Limited functionalities, only text-based input and output.
- **Libraries**: `argparse`, no libraries needed.
- **Examples**: Windows Command Prompt, Unix/Linux Terminal, Python IDLE.
  - See [CLI example](CLI.py).

### 2. Text-based User Interface (TUI)

- **Definition**: A text-based interface that uses text and symbols to represent the information and actions available to the user. A more advanced version of CLI, with an artistic touch.
- **Pros**:
  - More visually appealing than CLI.
  - Easier to navigate than CLI.
  - Can display more information than CLI.
- **Cons**:
  - Still limited in terms of user interactions.
  - Not as intuitive as GUI.
  - Few modern libraries or frameworks available.
- **Libraries**: `curses`, `urwid`, `npyscreen`, `PyTermGUI`
- **Examples**: Turbo Vision, ncurses, dialog.
  - See [TUI example](TUI.py).

### 3. Graphical User Interface (GUI)

- **Definition**: A visual interface that allows users to interact with electronic devices through graphical icons and visual indicators. Code is executed on the device itself.
- **Pros**:
  - User-friendly and intuitive.
  - Visually appealing.
  - Supports multimedia elements.
  - Can be very intuitive to design: see [Qt Workflow](../Qt%20Workflow).
- **Cons**:
  - More complex to implement than CLI.
  - Platform-dependent.
- **Libraries**: `Tkinter`, `PyQt`, `wxPython`, `Kivy`, `PyGTK`, `PySide`, `PyForms`, `PySimpleGUI`
- **Examples**: Windows, macOS, Linux desktop applications.
  - See [GUI example](GUI.py).

### 4. Web User Interface (Web UI)

- **Definition**: A user interface that is served by a web server and displayed in a web browser. Code is executed on the server.
- **Pros**:
  - Cross-platform compatibility.
  - Easy to update and maintain.
  - Can be accessed remotely.
- **Cons**:
  - Extra difficulty to implement server-side code.
  - Constant security follow-up, but safer to protect proprietary code.
- **Libraries**: `Flask`, `Django`, `React`, `Next.js`, `Angular`, `Vue.js`, `Svelte`, `streamlit`
- **Examples**: Websites, web applications, web services.
  - See [Web UI example](Web%20UI.py).
