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


def get_diff(old, new, key, diff):
    status = get_status(old, new, key)

    if status == 'added':
        diff[key] = (status, new[key])

    elif status == 'deleted':
        diff[key] = (status, old[key])

    elif status == 'nested':
        diff[key] = (status, generate_diff(old[key], new[key]))

    elif status == 'changed':
        diff[key] = (status, old[key], new[key])

    else:
        diff[key] = (status, new[key])

    return diff


def generate_diff(old, new):
    keys = sorted(set(list(old.keys()) + list(new.keys())))
    diff = {}
    for key in keys:
        get_diff(old, new, key, diff)
    return diff
