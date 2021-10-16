def get_chunk(diff_value):
    if isinstance(diff_value, tuple):
        return diff_value[:2]
    return None, diff_value


def get_rest(diff_value):
    return diff_value[2]


def convert(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def render(content, depth):
    if isinstance(content, dict):
        return stylish(content, depth + 1)
    return convert(content)


def process(key, content, status, result, data, indent, depth):
    if status == 'updated':
        new_content = render(data[2], depth)
        result.append('{}  - {}: {}'.format(indent, key, content))
        result.append('{}  + {}: {}'.format(indent, key, new_content))

    elif status == 'added':
        result.append('{}  + {}: {}'.format(indent, key, content))

    elif status == 'removed':
        result.append('{}  - {}: {}'.format(indent, key, content))

    else:
        result.append('{}    {}: {}'.format(indent, key, content))


def stylish(diff, depth=0):
    result = []
    indent = '    ' * depth

    for key, val in diff.items():
        status, data = get_chunk(val)
        content = render(data, depth)
        process(key, content, status, result, val, indent, depth)

    return '{\n' + '\n'.join(result) + '\n{}}}'.format(indent)
