import sys

input = sys.stdin.readline
n = int(input())
a = sorted(list(map(int, input().split())))
b = list(map(int, input().split()))
s = 0

for i in range(n):
    tmp = max(b)
    s += a[i] * tmp
    b.pop(b.index(tmp))

print(s)
