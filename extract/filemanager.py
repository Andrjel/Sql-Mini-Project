import simplejson as json
import os
from datetime import datetime


def check_directory(func):
    """
    A decorator function that creates a directory based on the current date and passes it as an argument to the decorated function.

    Args:
        func (function): The function to be decorated.

    Returns:
        function: The decorated function.

    Raises:
        Exception: If there is an error during file operation.

    """
    def wrapper(*args, **kwargs):
        try:
            date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            dest_folder = args[0].pop(0).get("name")
            directory = f"data/{dest_folder}/"
            os.makedirs(directory, exist_ok=True)
            dest_file = f"{directory}{date}.json"
            return func(dest_file, *args, **kwargs)
        except Exception as e:
            print(f"Exception during file operation:\n{e}")
    return wrapper


@check_directory
def write_json(dest_file: str, data: dict) -> None:
    """
    Write data to a JSON file.

    Args:
        dest_file (str): The path to the JSON file.
        data (dict): The data to be written to the JSON file.
    
    Returns:
        None
    """
    if not data:
        return
    with open(dest_file, "w") as file:
        file.write(json.dumps(data, indent=4, sort_keys=True))


def read_json(file_path: str) -> dict:
    """
    Read data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except Exception as e:
        print(f"Exception during loading json file:\n{e}")
        return {}