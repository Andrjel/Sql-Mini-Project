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
            date = datetime.now().strftime("%Y-%m-%d")
            directory = f"data/{date}"
            os.makedirs(directory, exist_ok=True)
            return func(directory, *args, **kwargs)
        except Exception as e:
            print(f"Exception during file operation:\n{e}")
    return wrapper


@check_directory
def write_json(directory: str, data: dict) -> None:
    """
    Write data to a JSON file in the specified directory.

    Args:
        directory (str): The directory where the JSON file will be saved.
        data (dict): The data to be written to the JSON file.

    Returns:
        None
    """
    if not data:
        return
    timestemp = datetime.now().strftime("%H-%M-%S")
    target_file = f"{directory}/{timestemp}.json"
    with open(target_file, "w") as file:
        file.write(json.dumps(data, indent=4, sort_keys=True))


def read_json(file_path: str) -> dict:
    """
    Read data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data read from the JSON file.
    """
    with open(file_path, "r") as file:
        return json.load(file)