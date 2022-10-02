#This basic template can be used for all the projects for creating folder structures.
import os
from pathlib import Path #OS agnostic in terms of how path is defined.
import logging

logging.basicConfig(level= logging.INFO, format= '[%(asctime)s]: %(message)s: ')

package_name= "deepclassifier"

list_of_files= [
                ".github/workflows/ .gitkeep",  #for CI-CD and keeping even empty folders
                f"src/{package_name}/__init__.py",
                f"src/{package_name}/components/__init__.py",
                f"src/{package_name}/utils/__init__.py",
                f"src/{package_name}/config/__init__.py",
                f"src/{package_name}/pipeline/__init__.py",
                f"src/{package_name}/entity/__init__.py",
                f"src/{package_name}/constants/__init__.py",
                "configs/config.yaml",
                "dvc.yaml",                 #data version control pipeline
                "params.yaml",
                "init_setup.sh",             #shell script to automate and help create the environment
                "requirements.txt",         
                "requirements_dev.txt",      #requirements only for development
                "setup.py",
                "setup.cfg",                  #required if creating a python package only
                "pyproject.toml",              #required if creating a python package only  
                "tox.ini",                      #for testing locally
                "research/trials.ipynb"         #for testing in jupyter environment
                                          
                
              ]

for filepath in list_of_files:
    filepath= Path(filepath)
    filedir, filename= os.path.split(filepath)              #splits into a list of file directory and file name
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"creating directory {filedir} for filename: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)== 0):       #create files only if the filepath doesn't exist or if it's empty. 
        with open(filepath, "w") as f:                                          #This way we can run template.py again without worrying about files being overwritten
            pass                        #create an empty file
            logging.info(f"creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")


