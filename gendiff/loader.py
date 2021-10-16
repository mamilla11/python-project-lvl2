import json
import yaml
import os


def load_files(file1, file2):
    _, extension = os.path.splitext(file1)

    if extension == '.json':
        return (
            json.load(open(file1)),
            json.load(open(file2))
        )

    if extension in ['.yml', '.yaml']:
        return (
            yaml.safe_load(open(file1)),
            yaml.safe_load(open(file2))
        )
