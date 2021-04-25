import os

from tests import load_file


def load_horizon_file(filename: str) -> dict:
    return load_file(os.path.join("model/horizon/", filename))
