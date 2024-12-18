import sys
from itertools import permutations

input = sys.stdin.readline
n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
ans = list(permutations(s, m))
for i in ans:
    print(" ".join(map(str, i)))
