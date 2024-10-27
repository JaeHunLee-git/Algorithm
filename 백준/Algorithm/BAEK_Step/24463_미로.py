# 시간초과 코드
from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
parent = [[[] for _ in range(M)] for _ in range(N)]
visited = [[False] * M for _ in range(N)]
hole = []
for i in range(N):
    graph.append(list(input().rstrip().replace(".", "@")))
    for j in range(M):
        if graph[i][j] == "@":
            if i == 0 or i == N - 1 or j == 0 or j == M - 1:
                hole.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and graph[nx][ny] == "@":
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    parent[nx][ny] = (x, y)
    return


bfs(hole[0][0], hole[0][1])
now = hole[1]
while now != hole[0]:
    x, y = now
    graph[x][y] = "."
    now = parent[x][y]
graph[hole[0][0]][hole[0][1]] = "."

for i in range(N):
    print("".join(graph[i]))

