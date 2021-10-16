from gendiff.cli import process_args
from gendiff.loader import load_files
from gendiff.differ import differ
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.tojson import tojson


def generate_diff(file1, file2, format=None):
    old, new = load_files(file1, file2)
    diff = differ(old, new)

    if format == 'plain':
        print(plain(diff))
    elif format == 'json':
        print(tojson(diff))
    else:
        print(stylish(diff))


def main():
    args = process_args()
    generate_diff(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
