import argparse
import json
import yaml
import os

from gendiff.differ import generate_diff
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.tojson import tojson


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


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    old, new = load_files(args.first_file, args.second_file)
    diff = generate_diff(old, new)

    if args.format == 'plain':
        print(plain(diff))
    elif args.format == 'json':
        print(tojson(diff))
    else:
        print(stylish(diff))


if __name__ == '__main__':
    main()
