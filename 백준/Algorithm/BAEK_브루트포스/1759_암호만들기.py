import sys
from itertools import combinations

input = sys.stdin.readline
l, c = map(int, input().split())
lst = sorted(list(input().split()))
ans = list(combinations(lst, l))
for i in ans:
    a = 0
    b = 0
    tmp = "".join(map(str, i))
    for k in range(len(tmp)):
        if (
            tmp[k] == "a"
            or tmp[k] == "e"
            or tmp[k] == "i"
            or tmp[k] == "o"
            or tmp[k] == "u"
        ):
            a += 1
        else:
            b += 1

    if a > 0 and b > 1:
        print(tmp)
