import sys

input = sys.stdin.readline
from collections import deque


def bfs(a, b):
    q = deque()
    q.append((a, b))
    tmp=board[a][b]
    visited[a][b] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and board[nx][ny]==tmp:
                visited[nx][ny] = 1
                q.append((nx, ny))


n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[0] * n for _ in range(n)]
ans1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans1 += 1
visited = [[0] * n for _ in range(n)]
ans2 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == "G":
            board[i][j] = "R"
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j)
            ans2 += 1
print(ans1, ans2)
