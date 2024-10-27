import sys

input = sys.stdin.readline
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visit = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        visit[i][j] = (
            max(visit[i - 1][j], visit[i][j - 1], visit[i - 1][j - 1])
            + arr[i - 1][j - 1]
        )

print(visit[n][m])
