import sys
from collections import deque

input = sys.stdin.readline
a = int(input())
b = int(input())
computer = [0] * (a + 1)
connect = [[False] * (a + 1) for _ in range(a + 1)]
visited = [[0] * (a + 1) for _ in range(a + 1)]
for i in range(b):
    x, y = map(int, input().split())
    connect[x][y] = True
    connect[y][x] = True


def bfs(x):
    q = deque()
    q.append(x)
    while q:
        nx = q.popleft()
        for i in range(1, a + 1):
            if (
                (connect[nx][i] == True or connect[i][nx] == True)
                and visited[nx][i] == 0
                and visited[i][nx] == 0
            ):
                q.append(i)
                visited[nx][i] = 1
                visited[i][nx] = 1
                computer[nx] = 1
                computer[i] = 1


bfs(1)
if sum(computer) == 0:
    print(0)
else:
    print(sum(computer) - 1)
