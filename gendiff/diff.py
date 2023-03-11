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
                           "old_value": dic1[key],
                           "new_value": dic2[key]
                           })
    return result
