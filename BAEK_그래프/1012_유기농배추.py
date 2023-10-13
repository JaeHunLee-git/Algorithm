import sys
from collections import deque

input = sys.stdin.readline
t = int(input())


def bfs(i, j):
    q = deque()
    q.append([i, j])
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                q.append([nx, ny])


for _ in range(t):
    ans = 0
    m, n, k = map(int, input().split())
    arr = [[0] * m for i in range(n)]
    visited = [[False] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                ans += 1
    print(ans)
