# python은 재귀제한이 걸려있기 때문에 재귀 허용치가 넘어가면 런타임에러를 일으킨다.
# 따라서 허용 범위를 넓혀준다.
import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().strip().split())
lst = [[0] * (n + 1) for i in range(n + 1)]
visited = [0] * (n + 1)
visited[0] = 1
cnt = 0

for _ in range(m):
    a, b = map(int, input().strip().split())
    lst[a][b] = lst[b][a] = 1


def dfs(v):
    visited[v] = 1
    for i in range(1, n + 1):
        if visited[i] == 0 and lst[v][i] == 1:
            dfs(i)


while visited.count(0) != 0:
    dfs(visited.index(0))
    cnt += 1

print(cnt)
