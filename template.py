import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = 'textSentiments'

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_loader.py",
    f"src/{project_name}/components/model.py",
    f"src/{project_name}/components/predict.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/logger.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/train_pipeline.py",
    f"src/{project_name}/pipeline/predict_pipeline.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/data_classes.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/constants/constants.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.py",
]

for path in list_of_files:
    filepath = Path(path)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir}")
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Created file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")
