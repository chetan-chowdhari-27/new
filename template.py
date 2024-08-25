import os 
from pathlib import Path
import logging


logging.basicConfig(level=logging.INFO)

project_name = "mlproject"
list_of_files = [
    # ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/componenets/__init__.py",
    f"src/{project_name}/componenets/data_ingestion.py",
    f"src/{project_name}/componenets/data_transformation.py",
    f"src/{project_name}/componenets/model_trainer.py",
    f"src/{project_name}/componenets/model_trainer.py",
    f"src/{project_name}/pipelines/__init__.py",
    f"src/{project_name}/pipelines/training_pipeline.py",
    f"src/{project_name}/pipelines/prediction_pipeline.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/execption.py",
    f"src/{project_name}/utlis.py",
    "app.py",
    "Dockerfile",
]


for file in list_of_files:
    filepath = Path(file)
    filedir , file_name = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directing: {filedir} for the file {filepath}")

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filepath} is already exists")