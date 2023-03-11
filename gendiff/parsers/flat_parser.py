def nested_val(dic: dict, depth: int) -> str:
    lst2 = ["{"]
    if type(dic) == dict:
        for i, value in dic.items():
            if type(value) == dict:
                new_value = nested_val(value, depth + 4)
                lst2.append(f"{' ' * depth}  {i}: {new_value}")
            else:
                lst2.append(f"{' ' * depth}  {i}: {value}")
        lst2.append(f'{" " * (depth - 2)}}}')
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
            result.append(f"""{depth * ' '}+ {i['name']}: {nested_val(i['value'], depth + 4)}"""  # noqa: E501
                          )
        if i['status'] == "deleted":
            result.append(f"""{depth * ' '}- {i['name']}: {nested_val(i['value'], depth + 4)}"""  # noqa: E501
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
    result.append(f'{" " * (depth - 2)}}}')
    return '\n'.join(result)
