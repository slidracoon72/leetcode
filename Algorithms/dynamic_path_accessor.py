def get_dict_value(dct, path):
    keys = path.split('.')
    print(keys)
    current = dct

    for key in keys:
        if key in current:
            current = current[key]
        else:
            return None
    return current


obj = {"car": {"wheels": 2, "gears": 5}}
path = "car.gears"
result = get_dict_value(obj, path)
print(result)
