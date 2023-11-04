import sys
from collections import deque
from itertools import combinations

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
answer = float("inf")


def bfs(v):
    q = deque(v)
    visited = [[-1 for _ in range(N)] for _ in range(N)]
    m = 0
    for x, y in q:
        visited[x][y] = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            ax = x + dx[i]
            ay = y + dy[i]
            if 0 <= ax < N and 0 <= ay < N:
                if visited[ax][ay] == -1 and board[ax][ay] != 1:
                    q.append([ax, ay])
                    visited[ax][ay] = visited[x][y] + 1
                    m = max(m, visited[x][y] + 1)

    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1 and board[i][j] != 1:
                return float("inf")
    return m


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

for v in combinations(virus, M):
    answer = min(bfs(v), answer)

if answer == float("inf"):
    print(-1)
else:
    print(answer)
