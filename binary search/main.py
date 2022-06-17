li = [2, 3, 3, 6 ,7, 7, 7, 7, 7, 7, 8, 9]


#eigene Implmentation
def binarysearch(li, num):
    found = False
    lenLi = len(li)
    searchSpace = [0, lenLi]
    while not found:
        searchMax = round(((searchSpace[1]-searchSpace[0])/2)+searchSpace[0])
        if li[searchMax] == num:
            found = True
            return searchMax
        elif li[searchMax] > num:
            searchSpace[1] = searchMax
        elif li[searchMax] < num:
            searchSpace[0] = searchMax


#aus einem Video (besser)
def bisect_left(arr: list, x, lo=0, hi=None) -> int:
    hi = hi if hi is not None else len(arr)
    assert 0 <= lo <= hi <= len(arr)
    while lo < hi:
        mid = (lo + hi)//2 # lo + (hi-lo)//2
        if arr[mid] < x:
            lo = mid+1
        else:
            hi = mid
    return lo
# gehört zusammen
def bisect_index_of(arr:list, x) -> int:
    i = bisect_left(arr, x)
    if i != len(arr) and arr[i] == x:
        return i
    raise ValueError



pc = binarysearch(li, 7)
print(pc)

pc = bisect_index_of(li, 7)
print(pc)