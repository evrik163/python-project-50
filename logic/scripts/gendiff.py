import argparse
from logic.flat_logic import generate_diff
from logic.parser_logic import parser_func

def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    dicts = parser_func(args.first_file, args.second_file)
    print(generate_diff(dicts))


if __name__ == '__main__':
    main()
