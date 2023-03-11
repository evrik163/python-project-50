import argparse
from gendiff.diff import travel
from gendiff.parsers.flat_parser import flat_formatter
from gendiff.parsers.json_parser import parser_func
from gendiff.parsers.plain_parser import plain_formatter
from gendiff.parsers.json_dump import json_formatter


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default="stylish",
                        help='set format of output'
                        )
    args = parser.parse_args()
    return args
