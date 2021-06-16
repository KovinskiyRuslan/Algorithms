def binary_search(alist, item):
    first = 0
    last = len(alist)-1

    while first <= last:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            return midpoint
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return -1
