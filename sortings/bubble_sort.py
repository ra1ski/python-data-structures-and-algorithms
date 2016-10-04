# Linear search algorithm
# @ra1ski


def bubble_sort(_list):
    nbList = len(_list)
    finished = False

    while not finished:
        finished = True
        for i in range(len(_list) - 1):
            if _list[i] > _list[i+1]:
                sort = False
                tmp = _list[i]
                _list[i] = _list[i+1]
                _list[i+1] = tmp
    return _list


if __name__ == '__main__':
    unsorted_list = [1, 2, 7, 13, 4]
    sorted_list = bubble_sort(unsorted_list)

    print(sorted_list)
