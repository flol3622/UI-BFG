```shell
# setup
conda create -n UIcomp python=3.8
conda activate UIcomp

# extremely fast package installer
pip install uv 
uv pip install prompt_toolkit streamlit auto-py-to-exe pyqt6-tools PySide6
```

```shell
# start streamlit app
.venv\Scripts\activate  
streamlit run .\webUI.py
```
6