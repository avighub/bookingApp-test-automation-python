import json
from pathlib import Path

BASE_PATH = Path.cwd()


def read_json_file(file_name):
    path = BASE_PATH.joinpath(file_name)

    with path.open(mode='r') as f:
        return json.load(f)
