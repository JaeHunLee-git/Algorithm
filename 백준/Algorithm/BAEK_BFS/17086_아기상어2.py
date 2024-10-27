import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(i, j, cnt):
    q = deque()
    q.append([i, j, cnt])
    visited = [[False] * m for _ in range(n)]
    visited[i][j] = True
    while q:
        x, y, tmp = q.popleft()
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == 1:
                    return tmp
                if arr[nx][ny] == 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append([nx, ny, tmp + 1])


ans = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            ans = max(ans, bfs(i, j, 1))
print(ans)
