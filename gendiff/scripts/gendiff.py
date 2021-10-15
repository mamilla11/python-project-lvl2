import argparse
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


def stylish(items):
    def inner(items, ident, diffstr):
        diffstr += '{\n'

        for key in items:
            diffstr += ' ' * (ident + 1)
            if isinstance(items[key], dict):
                diffstr += f'{key}: '
                diffstr += inner(items[key], ident + 2, '')
            else:
                for val in items[key]:
                    diffstr += f'{val[0]} {key}: {val[1]}\n'
        diffstr += ' ' * (ident) + '}\n'
        return diffstr

    return inner(items, 0, '')


def get_status(old, new, key):
    if key in new and key not in old:
        return 'added'

    if key in old and key not in new:
        return 'deleted'

    if isinstance(old[key], dict) and isinstance(new[key], dict):
        return 'nested'

    if old[key] != new[key]:
        return 'changed'

    return 'unchanged'


def get_diff(old, new, key):
    status = get_status(old, new, key)

    if status == 'added':
        return [(key, '+', new[key])]

    if status == 'deleted':
        return [(key, '-', old[key])]

    if status == 'nested':
        return [(key, ' ', generate_diff(old[key], new[key]))]

    if status == 'changed':
        return [(key, '-', old[key]), (key, '+', new[key])]

    return [(key, ' ', new[key])]


def generate_diff(old, new):
    keys = sorted(set(list(old.keys()) + list(new.keys())))
    return [get_diff(old, new, key) for key in keys]


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    old, new = load_files(args.first_file, args.second_file)
    diff = generate_diff(old, new)

    for i in diff:
        print(i)


if __name__ == '__main__':
    main()
