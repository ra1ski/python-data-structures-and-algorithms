from typing import Union

def interpolationSearch(arr:list, offset:int, limit:int, searchValue:int) -> Union[None, int]:
    """
    formula \n
    pos = lo + [ (x-arr[lo])*(hi-lo) / (arr[hi]-arr[Lo]) ]

    :param  arr:         Sorted multitude
    :param  offset:      start index
    :param  limit:       End index
    :param  searchValue: Value to search

    :return:             arr index of searched value, if found, in other case is - None
    """

    arrLen = len(arr)

    if arrLen > 0:
        if searchValue is None:
            raise Exception('please provide value to search')

        if arrLen < limit or arrLen < offset or offset >= limit or offset < 0:
            raise Exception('search range must be in arr range')

        while offset <= limit:
            try :
                pos = offset + (searchValue - arr[offset]) * ((limit - offset) / (arr[limit] - arr[offset]))
                pos = int(round(pos))

                if (limit < pos) :
                    raise Exception

                if arr[pos] == searchValue:
                    return pos

                if arr[pos] < searchValue:
                    offset = pos+1

                if arr[pos] > searchValue:
                    limit = pos
            except:
                return None

    return None

if __name__ == '__main__':
    searchData  = [12, 15, 28, 35, 57, 68, 87, 95, 158, 198, 257]
    offset      = 0
    limit       = int((len(searchData))-1)
    searchValue = 300

    index = interpolationSearch(searchData, offset, limit, searchValue)

    if index:
        print("value {0} found in searchData[{1}]".format(searchValue, index))
    else:
        print("value not found")
