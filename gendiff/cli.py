import argparse


def process_args():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', metavar='first_file')
    parser.add_argument('second_file', metavar='second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    return parser.parse_args()
