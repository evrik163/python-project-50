import sys
sys.path.insert(0, "/home/pavel/projects/python-project-50/logic/parsers")
from json_parser import parser_func
dicts = parser_func("./file11.json", "./file22.json")
dicts1 = parser_func("./file1.json", "./file2.json")

dic1, dic2 = dicts
dic3, dic4 = dicts1

def travel(dic1, dic2):
    result = list()
    keys = sorted(
        set(dic1) | set(dic2)
    )
    for key in keys:
        if key not in dic1:
            result.append({"name": key,
                           "status": "added",
                           "value": dic2[key]
                           })
        elif key not in dic2:
            result.append({"name": key,
                           "status": "deleted",
                           "value": dic1[key]
                           })
        elif isinstance(dic1[key], dict) and isinstance(dic2[key], dict):
            result.append({"name": key,
                           "status": "nested",
                           "value": travel(dic1[key], dic2[key])
                           })
        elif dic1[key] == dic2[key]:
            result.append({"name": key,
                           "status": "same",
                           "value": dic1[key]
                           })
        else:
            result.append({"name": key,
                           "status": "changed",
                           "old_value": dic2[key],
                           "new_value": dic1[key]
                           })
    return result


result = travel(dic1, dic2)
result1 = travel(dic3, dic3)


def nested_val(dic: dict, depth: int) -> str:
    lst2 = ["{"]
    if type(dic) == dict:
        for i, value in dic.items():
            if type(value) == dict:
                new_value = nested_val(value, depth + 4)
                lst2.append(f"{' ' * depth}  {i}: {new_value}")
            else:
                lst2.append(f"{' ' * depth}  {i}: {value}")
        lst2.append(f'{" " * depth}}}')
        return '\n'.join(lst2)
    if isinstance(dic, bool):
        return str(dic).lower()
    if dic is None:
        return 'null'
    return dic


def flat_formatter(lst, depth=2):  # noqa: C901
    result = ['{']
    for i in lst:
        if i['status'] == "same":
            result.append(f"""{depth * ' '}  {i['name']}: {nested_val(i['value'], depth + 4)}"""  # noqa: E501
                          )
        if i['status'] == "added":
            result.append(f"""{depth * ' '}- {i['name']}: {nested_val(i['value'], depth + 4)}"""  # noqa: E501
                          )
        if i['status'] == "deleted":
            result.append(f"""{depth * ' '}+ {i['name']}: {nested_val(i['value'], depth + 4)}"""  # noqa: E501
                          )
        if i['status'] == "changed":
            result.append(f"""{depth * ' '}- {i['name']}: {nested_val(i['old_value'], depth + 4)}"""  # noqa: E501
                          )
            result.append(f"""{depth * ' '}+ {i['name']}: {nested_val(i['new_value'], depth + 4)}"""  # noqa: E501
                          )
        if i["status"] == "nested":
            kvalue = flat_formatter(i['value'], depth + 4)
            result.append(f"""{" " * depth}  {i["name"]}: {kvalue}"""
                          )
    result.append(f'{" " * depth}}}')
    return '\n'.join(result)


print(flat_formatter(result))
