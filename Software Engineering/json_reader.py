import json


def read_json(file_path):
    """
    Read JSON data from the specified file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Parsed JSON data.
    """
    # Reads and returns JSON data from the specified file.
    with open(file_path, 'r') as file:
        return json.load(file)
