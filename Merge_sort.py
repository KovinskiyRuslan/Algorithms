import math
k = int(input())
nl = list(map(int, input().split()))


def merge_sort(a):
    n = len(a)
    if n <= 1:
        print(*a)
        return a
    return merge(merge_sort(a[:math.ceil(n / 2)]), merge_sort(a[math.ceil(n / 2):]))


def merge(a, b):

    c = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            c.append(a[0])
            a = a[1:]
        else:
            c.append(b[0])
            b = b[1:]
    c += a
    c += b
    print(*c)
    return c


merge_sort(nl)
