def get_status(diff_value):
    if isinstance(diff_value, tuple):
        return diff_value[0]
    return None


def convert(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'


def added(path, status, content):
    return 'Property \'{}\' was {} with value: {}'.format(
        path, status, convert(content)
    )


def removed(path, status):
    return 'Property \'{}\' was {}'.format(
        path, status
    )


def updated(path, status, old, new):
    return 'Property \'{}\' was {}. From {} to {}'.format(
        path, status, convert(old), convert(new)
    )


def process(path, status, result, data):
    if status == 'nested':
        render(data[1], path, result)
    if status == 'added':
        result.append(added('.'.join(path), status, data[1]))
    if status == 'removed':
        result.append(removed('.'.join(path), status))
    if status == 'updated':
        result.append(updated('.'.join(path), status, data[1], data[2]))


def render(diff, path=[], result=[]):
    for key, val in diff.items():
        status = get_status(val)
        path.append(key)
        process(path, status, result, val)
        path.pop()

    return '\n'.join(result)


def plain(diff):
    return render(diff)
