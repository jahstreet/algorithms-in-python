import array
import random


def factorial(n):
    return _factorial(n) if n >= 0 else _factorial(-n)


def _factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def sum_arr(arr: array):
    if len(arr) == 0:
        return 0
    return arr[0] + sum(arr[1:])


def len_arr(arr: array):
    if len(arr) == 0:
        return 0
    return 1 + len_arr(arr[1:])


def max_arr(arr: array):
    if len(arr) == 1:
        return arr[0]
    return max(arr[0], max_arr(arr[1:]))


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


def quick_sort(arr: array):
    if len(arr) < 2:
        return arr
    if len(arr) == 2:
        return arr if arr[0] < arr[1] else [arr[1], arr[0]]
    pivot = random.choice(arr)
    lower = []
    equal = []
    higher = []
    for e in arr:
        if e < pivot:
            lower.append(e)
        elif e == pivot:
            equal.append(e)
        else:
            higher.append(e)
    return quick_sort(lower) + equal + quick_sort(higher)


if __name__ == '__main__':
    print(factorial(-5))  # -120
    print(sum_arr([2, 5, 7, -1, 4]))  # 17
    print(len_arr([2, 5, 7, -1, 4]))  # 5
    print(max_arr([2, 5, 7, -1, 4]))  # 7
    print(binary_search_recursive(["a", "b", "c"], "b"))  # 1
    print(quick_sort(["c", "a", "z", "b", "e", "c", "z", "a"]))  # ['a', 'a', 'b', 'c', 'c', 'e', 'z', 'z']
