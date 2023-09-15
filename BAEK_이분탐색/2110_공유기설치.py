import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))
arr.sort()

start, end = 0, arr[-1] - arr[0]
ans = 0

while start <= end:
    current = arr[0]
    tmp = 1
    mid = (start + end) // 2
    for i in range(1, n):
        if arr[i] - current >= mid:
            tmp += 1
            current = arr[i]
    if tmp >= c:
        start = mid + 1
    else:
        end = mid - 1
print(end)
