def value_check(value):
    if type(value) == dict:
        return "[complex value]"
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if type(value) is int:
        return value
    return f"'{value}'"


def plain_formatter(lst, path=''):
    result = []
    for i in lst:
        prop = f"{path}{i['name']}"
        if i['status'] == "added":
            result.append(f"Property '{prop}' was added with value: {value_check(i['value'])}")  # noqa: E501
        if i['status'] == "deleted":
            result.append(f"Property '{prop}' was removed")
        if i['status'] == "changed":
            result.append(f"Property '{prop}' was updated. From {value_check(i['old_value'])} to {value_check(i['new_value'])}")  # noqa: E501
        if i['status'] == "nested":
            result.append(plain_formatter(i['value'], f"{prop}."))
    return '\n'.join(result)
