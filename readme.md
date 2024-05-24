<!-- readme ~ Philippe Soubrier ~ 24/05/2024 -->
# 🎓 Introduction to Academia UIs in Python

Welcome to the repository of the BFG-meeting held on 24/05/2024, focused on converting code to GUIs within an academic context. The aim of this presentation was to demonstrate that software development (not only in Python) can be easy and enjoyable. The emphasis was on using and distributing code developed within our research group to coworkers, students, and non-coders.

## 📚 Overview

- 📁 [Different UIs](Different%20UIs): Contains a comparison of different user interfaces (UIs) that can be used for your applications, along with a **comparative overview**.
- 📁 [Qt Workflow](Qt%20Worflow): Includes a simple example of the Pizza calculator created during the workshop, explaining the entire workflow from UI design to application packaging.

## ⚙️ Setup

To experiment with this repository on your own computer, I suggest using the following environment with [Anaconda](https://anaconda.org/):

```shell
# Setup
conda create -n UIdemo python=3.8
conda activate UIdemo 

# Extremely fast package installer
pip install uv 
uv pip install prompt_toolkit streamlit auto-py-to-exe pyqt6-tools PySide6
```

For other Python setups, the packages used are:
- `prompt_toolkit` for the text-based UI (TUI)
- `streamlit` for the web-based UI (WUI)
- `PyQt6` for the graphical user interface (GUI)
  - `PySide6` to fully code in Qt6
  - `pyqt6-tools` for the Qt Designer **→ What I used**
- `auto-py-to-exe` for converting scripts into executables

> [!NOTE] 
> Do not hesitate to contact me for any questions, suggestions, or help!
>
> ~ [Philippe Soubrier](https://flupke.dev/)