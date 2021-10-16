from gendiff.cli import process_args
from gendiff.loader import load_files
from gendiff.differ import generate_diff


def main():
    args = process_args()
    file1, file2 = load_files(args.first_file, args.second_file)
    print(generate_diff(file1, file2, args.format))


if __name__ == '__main__':
    main()
