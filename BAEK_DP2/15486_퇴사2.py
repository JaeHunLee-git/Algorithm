import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
profit = [0] * (n + 1)

for i in range(n - 1, -1, -1):
    if arr[i][0] + i <= n:
        profit[i] = max(profit[i + 1], profit[arr[i][0] + i] + arr[i][1])
    else:
        profit[i] = profit[i + 1]
print(profit[0])
