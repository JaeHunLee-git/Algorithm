import sys
from collections import deque

input = sys.stdin.readline


def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        target = q.popleft()

        for i in graph[target]:
            if not visited[i]:
                visited[i] = visited[target] + 1
                q.append(i)


n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = []

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    bfs(i)
    result.append(sum(visited))

print(result.index(min(result)) + 1)
