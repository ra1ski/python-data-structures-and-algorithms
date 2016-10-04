# Linear search algorithm
# @ra1ski


def insertion_sort(_list):
    first = _list[0]

    for i in range(1, len(_list)):
        current_value = _list[i]
        pointer = i

        while pointer > 0 and _list[pointer-1] > current_value:
            _list[pointer] = _list[pointer - 1]
            pointer -= 1

        _list[pointer] = current_value

    return _list

if __name__ == '__main__':
    unsorted_list = [1, 2, 7, 13, 4]
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)
