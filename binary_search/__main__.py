def binary_search(names, name):
    lower_bound = 0
    upper_bound = len(names) - 1
    while lower_bound <= upper_bound:
        target = int((upper_bound - lower_bound) / 2)
        target_name = names[target]
        if target_name == name:
            return target
        if target_name > name:
            upper_bound = target - 1
        else:
            lower_bound = target + 1
    return None


def binary_search_recursive(names, name):
    return _binary_search_recursive(names, name, 0, len(names) - 1)


def _binary_search_recursive(names, name, lower, upper):
    if lower > upper:
        return None
    target = int((upper - lower) / 2)
    target_name = names[target]
    if target_name == name:
        return target
    if target_name > name:
        return _binary_search_recursive(names, name, lower, target - 1)
    else:
        return _binary_search_recursive(names, name, lower, target + 1)


if __name__ == '__main__':
    print(binary_search_recursive(["a", "b", "c"], "b"))
