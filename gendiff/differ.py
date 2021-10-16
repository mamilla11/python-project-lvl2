from gendiff.formatter.plain import plain
from gendiff.formatter.tojson import tojson
from gendiff.formatter.stylish import stylish


def formatter(diff, format):
    if format == 'plain':
        return plain(diff)
    if format == 'json':
        return tojson(diff)
    return stylish(diff)


def get_status(old, new, key):
    if key in new and key not in old:
        return 'added'

    if key in old and key not in new:
        return 'removed'

    if isinstance(old[key], dict) and isinstance(new[key], dict):
        return 'nested'

    if old[key] != new[key]:
        return 'updated'

    return 'unchanged'


def process(old, new, key, diff):
    status = get_status(old, new, key)

    if status == 'added':
        diff[key] = (status, new[key])

    elif status == 'removed':
        diff[key] = (status, old[key])

    elif status == 'nested':
        diff[key] = (status, differ(old[key], new[key]))

    elif status == 'updated':
        diff[key] = (status, old[key], new[key])

    else:
        diff[key] = (status, new[key])

    return diff


def differ(old, new):
    if isinstance(old, dict) and isinstance(new, dict):
        keys = sorted(set(list(old.keys()) + list(new.keys())))
        diff = {}
        for key in keys:
            process(old, new, key, diff)
        return diff


def generate_diff(old, new, format=None):
    diff = differ(old, new)
    return formatter(diff, format)
