import json


def tojson(diff):
    if isinstance(diff, dict):
        return json.dumps(diff, indent=4)
