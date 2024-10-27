import sys
from collections import deque

input = sys.stdin.readline


def bfs(a, b, visited):
    q = deque()
    q.append([a, b])
    visited[a][b] = 1
    while q:
        px, py = q.popleft()
        for k in range(4):
            nx = px + dx[k]
            ny = py + dy[k]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and not visited[nx][ny]
                and safe[nx][ny] == 1
            ):
                q.append([nx, ny])
                visited[nx][ny] = 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

for water in range(0, 101):
    safe = [[1] * n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            if arr[x][y] <= water:
                safe[x][y] = 0
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if safe[x][y] == 1 and not visited[x][y]:
                bfs(x, y, visited)
                cnt += 1
    ans = max(ans, cnt)

print(ans)
