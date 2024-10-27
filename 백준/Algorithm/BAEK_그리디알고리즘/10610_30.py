import sys

input = sys.stdin.readline
from itertools import permutations

n = list(map(int, input().strip()))
n.sort(reverse=True)
if (sum(n) % 3 != 0) or (0 not in n):
    print(-1)
else:
    result = "".join(map(str, n))
    print(result)
