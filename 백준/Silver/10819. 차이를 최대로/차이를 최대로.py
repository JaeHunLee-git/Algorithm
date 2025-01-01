import sys
from itertools import permutations

input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
lst = list(permutations(a, n))
sum = []
for i in lst:
    tmp = 0
    for k in range(len(i) - 1):
        tmp += abs(i[k] - i[k + 1])
    sum.append(tmp)
print(max(sum))

