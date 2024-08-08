# practice
import sys

sys.setrecursionlimit(10000000)

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

areas = []
cnt = 0


def dfs(x, y):
    global cnt
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
    return False


for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            areas.append(cnt)

if len(areas) == 0:
    print(0)
    print(0)
else:
    print(len(areas))
    print(max(areas))
