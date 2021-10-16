from gendiff.cli import process_args
from gendiff.differ import generate_diff


def main():
    args = process_args()

    print(generate_diff(
        args.first_file,
        args.second_file,
        args.format
    ))


if __name__ == '__main__':
    main()
