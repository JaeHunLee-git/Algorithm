# dfs는 재귀함수를 많이 사용
# bfs는 queue를 많이 사용

import sys

input = sys.stdin.readline
n, m, v = map(int, input().strip().split())
lst = [[0] * (n + 1) for i in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().strip().split())
    lst[a][b] = lst[b][a] = 1

    visited = [0] * (n + 1)


def dfs(v):
    print(v, end=" ")
    visited[v] = 1

    for i in range(1, n + 1):
        if visited[i] == 0 and lst[v][i] == 1:
            dfs(i)


def bfs(v):
    visited[v] = 0
    queue = [v]

    while queue:
        v = queue.pop(0)
        print(v, end=" ")
        for i in range(1, n + 1):
            if visited[i] == 1 and lst[v][i] == 1:
                queue.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)
