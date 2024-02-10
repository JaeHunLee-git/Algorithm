import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append([x, y])
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if (
                0 <= nx < n
                and 0 <= ny < n
                and visited[nx][ny] == 0
                and arr[nx][ny] in tmp
            ):
                q.append([nx, ny])
                visited[nx][ny] = 1


cnt = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            tmp = [arr[i][j]]
            bfs(i, j)
            cnt += 1
print(cnt, end=" ")

ans = 0
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            if arr[i][j] == "R" or arr[i][j] == "G":
                tmp = ["R", "G"]
                bfs(i, j)
                ans += 1
            else:
                tmp = ["B"]
                bfs(i, j)
                ans += 1
print(ans)
