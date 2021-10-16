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


def render(diff, path=[], result=[]):
    for key, val in diff.items():
        status = get_status(val)
        path.append(key)

        if status == 'nested':
            render(val[1], path, result)
        elif status == 'added':
            result.append(added('.'.join(path), status, val[1]))
        elif status == 'removed':
            result.append(removed('.'.join(path), status))
        elif status == 'updated':
            result.append(updated('.'.join(path), status, val[1], val[2]))

        path.pop()
    return '\n'.join(result)


def plain(diff):
    return render(diff)
