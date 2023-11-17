import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
jump = [n + 1] * n
jump[0] = 0

for i in range(n):
    for j in range(1, arr[i] + 1):
        if i + j < n:
            jump[i + j] = min(jump[i + j], jump[i] + 1)

if jump[n - 1] == n + 1:
    print(-1)
else:
    print(jump[n - 1])
