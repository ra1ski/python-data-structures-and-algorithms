# Linear search algorithm
# @ra1ski

def linear_search(item, _list):
    index = None

    for idx, val in enumerate(_list):
        if val == item:
            index = idx
            break

    return index


if __name__ == '__main__':
    _list = ['chrome', 'firefox', 'opera', 'ie', 'netscape']
    item = input('Type browser name:')
    foundIndex = linear_search(item, _list)

    if foundIndex is not None:
        print('Item is in the list. Index: %s' % (foundIndex))
    else:
        _list.append(item)
        print('Item is not in the list, but we appened it for you', _list)
