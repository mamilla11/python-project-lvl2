import argparse
import json
import yaml
import os

from gendiff.differ import generate_diff


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


def get_chunk(diff_value):
    index = 0
    while True:
        yield diff_value[index]
        index += 1


def convert(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value


def render_content(content, depth):
    if isinstance(content, dict):
        return stylish(content, depth + 1)
    return convert(content)


def stylish(diff, depth=0):
    result = []
    indent = '    ' * depth

    for key, val in diff.items():
        chunk = get_chunk(val)
        status, data = None, val
        if isinstance(val, tuple):
            status, data = next(chunk), next(chunk)

        content = render_content(data, depth)

        if status == 'changed':
            new_content = render_content(next(chunk), depth + 1)
            result.append('{} - {}: {}'.format(indent, key, content))
            result.append('{} + {}: {}'.format(indent, key, new_content))

        elif status == 'added':
            result.append('{} + {}: {}'.format(indent, key, content))

        elif status == 'deleted':
            result.append('{} - {}: {}'.format(indent, key, content))

        else:
            result.append('{}   {}: {}'.format(indent, key, content))

    return '{\n' + '\n'.join(result) + '\n{}}}'.format(indent)


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    old, new = load_files(args.first_file, args.second_file)
    diff = generate_diff(old, new)
    print(stylish(diff))


if __name__ == '__main__':
    main()
