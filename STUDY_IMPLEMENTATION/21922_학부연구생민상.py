import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q = deque()
sit = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if arr[i][j] == 9:
            q.append([i, j])
            sit[i][j] = 1


def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            a, b, nx, ny = x + dx[i], y + dy[i], dx[i], dy[i]
            while 0 <= a < n and 0 <= b < m:
                sit[a][b] = 1
                if (arr[a][b] == 1 and nx == 0) or (arr[a][b] == 2 and ny == 0):
                    break
                elif arr[a][b] == 3:
                    nx, ny = -ny, -nx
                elif arr[a][b] == 4:
                    nx, ny = ny, nx
                elif arr[a][b] == 9:
                    break
                a += nx
                b += ny


bfs()
ans = 0
for tmp in sit:
    ans += tmp.count(1)

print(ans)
