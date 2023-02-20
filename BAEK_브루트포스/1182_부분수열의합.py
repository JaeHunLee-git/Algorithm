import sys
from itertools import combinations

input = sys.stdin.readline
n, s = map(int, input().strip().split())
lst = list(map(int, input().strip().split()))
cnt = 0
for i in range(1, n + 1):
    tmp = list(combinations(lst, i))
    for k in tmp:
        if sum(k) == s:
            cnt += 1
print(cnt)
