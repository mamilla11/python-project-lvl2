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
    pass


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
