import yaml
import json


def parser_func(path1, path2):
    compare = path1.split('/')[-1].split('.')[-1]
    if compare == 'yml' or 'yaml':
        yaml1 = open(path1)
        dict1 = yaml.load(yaml1, Loader=yaml.FullLoader)
        yaml2 = open(path2)
        dict2 = yaml.load(yaml2, Loader=yaml.FullLoader)
        return dict1, dict2
    elif compare == 'json':
        dict1 = json.load(open(path1))
        dict2 = json.load(open(path2))
        return dict1, dict2
