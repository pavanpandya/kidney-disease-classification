import os
from pathlib import Path
import logging

# Setting Up Logging String
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Project Name
project_name = "KidneyDiseaseClassification"

# List of Directories
list_of_files = [
    ".github/workflows/main.yml",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trails.ipyng",
    "templates/index.html",
]

# Creating Directories and Files
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created Directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created Empty File: {filename}")

    else:
        logging.info(f"{filename} already exists.")