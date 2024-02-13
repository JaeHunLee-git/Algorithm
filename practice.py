## test
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
h = 0
visited = [[0] * n for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(a, b):
    global h
    x, y = a, b
    if x == m - 1 and y == n - 1:
        h += 1
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
            if arr[x][y] > arr[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny)
                visited[nx][ny] = 0


visited[0][0] = 1
dfs(0, 0)
print(h)
