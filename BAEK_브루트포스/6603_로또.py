import sys
from itertools import combinations

input = sys.stdin.readline
while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    n = a[0]
    del a[0]
    lst = list(combinations(a, 6))
    for i in lst:
        print(*i)
    print()
