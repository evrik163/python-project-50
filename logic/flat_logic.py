def generate_diff(dicts):
    dict1, dict2 = dicts
    generator = []
    for item in dict1.items():
        key, value = item
        if key in dict2:
            if dict2.get(key) == value:
                generator.append(f"    {key}: {value}\n")
            else:
                new_value = dict2.get(key)
                generator.append(f'  - {key}: {value}\n')
                generator.append(f'  + {key}: {new_value}\n')
        else:
            generator.append(f'  - {key}: {value}\n')
    for item in dict2.items():
        key, value = item
        if key not in dict1:
            generator.append(f'  + {key}: {value}\n')
    generator.sort(key=lambda elem: elem[4])
    result = ''.join(generator)
    result = '{\n' + result + '}'
    result = result.lower()
    return result
