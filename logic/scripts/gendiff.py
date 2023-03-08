import argparse
from logic.diff import travel
from logic.parsers.flat_parser import flat_formatter
from logic.parsers.json_parser import parser_func
from logic.parsers.plain_parser import plain_formatter


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default="stylish",
                        help='set format of output'
                        )
    args = parser.parse_args()
    dic1, dic2 = parser_func(args.first_file, args.second_file)
    lst = travel(dic1, dic2)
    if args.format == 'stylish':
        print(flat_formatter(lst))
    elif args.format == 'plain':
        print(plain_formatter(lst))
    else:
        print("No such format")


if __name__ == '__main__':
    main()
