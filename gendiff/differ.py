def get_status(old, new, key):
    status = ''

    if key in new and key not in old:
        status = 'added'

    elif key in old and key not in new:
        status = 'deleted'

    elif isinstance(old[key], dict) and isinstance(new[key], dict):
        status = 'nested'

    elif old[key] != new[key]:
        status = 'changed'

    else:
        status = 'unchanged'

    return status


def get_diff(old, new, key):
    status = get_status(old, new, key)
    result = []

    if status == 'added':
        result = [(key, '+', new[key])]

    elif status == 'deleted':
        result = [(key, '-', old[key])]

    elif status == 'nested':
        result = [(key, ' ', generate_diff(old[key], new[key]))]

    elif status == 'changed':
        result = [(key, '-', old[key]), (key, '+', new[key])]

    else:
        result = [(key, ' ', new[key])]

    return result


def generate_diff(old, new):
    keys = sorted(set(list(old.keys()) + list(new.keys())))
    return [get_diff(old, new, key) for key in keys]
