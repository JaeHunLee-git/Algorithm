import sys
from collections import deque

input = sys.stdin.readline
m, n, h = map(int, input().split())
dx = [0, 0, 1, -1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 3차원 배열
arr = [[list(map(int, input().split())) for _ in range(n)] for __ in range(h)]
day = 0


def bfs():
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nz, nx, ny = z + dz[i], x + dx[i], y + dy[i]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m and arr[nz][nx][ny] == 0:
                q.append([nz, nx, ny])
                arr[nz][nx][ny] = arr[z][x][y] + 1


q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 1:
                q.append([i, j, k])
bfs()

tmp = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if arr[i][j][k] == 0:
                tmp = False
                break
            day = max(day, arr[i][j][k])
if tmp:
    print(day - 1)
else:
    print(-1)
