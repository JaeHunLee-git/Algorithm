import sys

input = sys.stdin.readline
from collections import deque


def bfs(weight):
    q = deque()
    q.append(one)
    visited = [False] * (n + 1)
    visited[one] = True

    while q:
        x = q.popleft()

        for i, w in bridges[x]:
            if not visited[i] and w >= weight:
                visited[i] = True
                q.append(i)

    if visited[two]:
        return True
    else:
        return False


n, m = map(int, input().split())
bridges = [[] for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    bridges[a].append([b, c])
    bridges[b].append([a, c])

one, two = map(int, input().split())

start = 1
end = 1000000000

while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        start = mid + 1

    else:
        end = mid - 1

print(end)
