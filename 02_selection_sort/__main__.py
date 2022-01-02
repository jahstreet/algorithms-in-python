import array
from collections import deque


def selection_sort(arr: array):
    sorted_arr = deque()
    while len(arr) > 0:
        min_value_index = _find_min_value_index(arr)
        sorted_arr.append(arr.pop(min_value_index))
    return sorted_arr


def _find_min_value_index(arr: array):
    min_value_index = 0
    min_value = arr[min_value_index]
    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
            min_value_index = i
    return min_value_index


if __name__ == '__main__':
    print(selection_sort([3, 5, 2, 2, 1, -1, 6, 10, 4]))
