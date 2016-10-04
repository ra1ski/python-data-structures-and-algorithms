# Binary search algorithm
# @ra1ski


def binary_search(item, _list):
    bottom = 0
    top = len(_list) - 1
    iteration = 1
    result = None

    while bottom <= top:
        middle = (bottom + top) // 2

        if _list[middle] == item:
            result = {
                'index': middle,
                'nbIterations': iteration
            }

            break
        elif _list[middle] < item:
            bottom = middle + 1
        else:
            top = middle - 1

        iteration += 1

    return result


if __name__ == '__main__':
    item = int(input('Type an item to search:'))
    _list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = binary_search(item, _list)

    if result is not None:
        print('Item is in the list. Index: %d. Iterations: %d' % (result['index'], result['nbIterations']))
    else:
        _list.append(item)
        print('Item is not in the list')
