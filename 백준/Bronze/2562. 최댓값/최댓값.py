import sys

input = sys.stdin.readline
a = [int(input()) for _ in range(9)]

b = sorted(a)

for i in range(9):
    if a[i] == b[-1]:
        print(a[i])
        print(i + 1)
