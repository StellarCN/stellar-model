import json
import os


def load_file(filename: str) -> dict:
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filepath = os.path.join(dir_path, "resources", filename)
    with open(filepath, "r") as f:
        return json.loads(f.read())
