import yaml
import os,sys
from housing.exception import HousingException


" The fun in this file are helper function they are not in the main code"


# create a function to read yaml file.
def read_yaml_file(file_path:str)->dict:
    """
    Reads a YAML file and returns the contents as a dictionary.
    file_path: str
    """
    try:
        with open(file_path, 'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
            raise (e,sys) from e