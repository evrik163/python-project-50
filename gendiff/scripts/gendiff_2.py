from gendiff.final_diff import generate_diff
from gendiff.parse_args import parse


def main():
    args = parse()
    print(generate_diff(args.second_file, args.first_file, args.format))


if __name__ == '__main__':
    main()
