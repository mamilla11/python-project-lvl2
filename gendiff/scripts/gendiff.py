import argparse
import json


def generate_diff(file1, file2):
    old = json.load(open(file1))
    new = json.load(open(file2))

    keys = sorted(set(list(old.keys()) + list(new.keys())))
    diff = []
    for key in keys:
        if key in new and key not in old:
            diff.append(f'+ {key}: {new[key]}')
        elif key in old and key not in new:
            diff.append(f'- {key}: {old[key]}')
        else:
            if old[key] == new[key]:
                diff.append(f'  {key}: {new[key]}')
            else:
                diff.append(f'- {key}: {old[key]}')
                diff.append(f'+ {key}: {new[key]}')

    return '{\n  ' + '\n  '.join(diff) + '\n}'


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()
