from gendiff.diff import travel
from gendiff.parsers.flat_parser import flat_formatter
from gendiff.parsers.json_parser import parser_func
from gendiff.parsers.plain_parser import plain_formatter
from gendiff.parsers.json_dump import json_formatter


def generate_diff(file_path1, file_path2, format_name):
    dic1, dic2 = parser_func(file_path1, file_path2)
    lst = travel(dic1, dic2)
    if format_name == 'stylish':
        return flat_formatter(lst)
    elif format_name == 'plain':
        return plain_formatter(lst)
    elif format_name == "json":
        return json_formatter(lst)
    else:
        return "No such format"
