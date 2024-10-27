import sys
from itertools import permutations

input = sys.stdin.readline

a, b = input().split()
b = int("".join(b))
len_a = len(a)
arr = list(permutations(a, len(a)))
ans = -1
for i in arr:
    tmp = int("".join(i))
    if tmp >= 10 ** (len_a - 1):
        if ans < tmp < b:
            ans = tmp
print(ans)
