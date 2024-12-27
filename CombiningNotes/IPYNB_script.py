import os
import json

directory = "path/to/your/notebooks"
# directory = "C:/Users/andre/Downloads"
output_file = "name.ipynb"
# output_file = "StatTheoryNotes.ipynb"

# notebook format
combined_notebook = {
    "cells": [],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

# sort files by name and append cells
for file in sorted(os.listdir(directory)):
    if file.endswith(".ipynb"):
        file = os.path.join(directory, file)
        
        with open(file, "r", encoding="utf-8") as f:
            notebook = json.load(f)
            combined_notebook["cells"].extend(notebook.get("cells", []))

# write to output_file
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(combined_notebook, f, indent=2)
