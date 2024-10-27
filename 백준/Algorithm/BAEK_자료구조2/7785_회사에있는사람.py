import sys

input = sys.stdin.readline
n = int(input())
arr = dict()
for _ in range(n):
    a, b = map(str, input().strip().split())
    if b == "enter":
        arr[a] = b
    else:
        del arr[a]
arr = sorted(arr.keys(), reverse=True)
for i in arr:
    print(i)
