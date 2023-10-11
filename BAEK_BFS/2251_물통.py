import sys
from collections import deque

input = sys.stdin.readline
a, b, c = map(int, input().split())
visited = [[False] * (b + 1) for _ in range(a + 1)]
ans = []
q = deque()
q.append([0, 0])


def pour(x, y):
    global q
    if visited[x][y] == False:
        visited[x][y] = True
        q.append([x, y])


def bfs():
    while q:
        x, y = q.popleft()
        z = c - x - y

        if x == 0:
            ans.append(z)

        # a->b
        water = min(x, b - y)
        pour(x - water, y + water)
        # a->c
        water = min(x, c - z)
        pour(x - water, y)
        # b->a
        water = min(y, a - x)
        pour(x + water, y - water)
        # b->c
        water = min(y, c - z)
        pour(x, y - water)
        # c->a
        water = min(z, a - x)
        pour(x + water, y)
        # c->b
        water = min(z, b - y)
        pour(x, y + water)


bfs()
ans.sort()
ans = set(ans)
print(*ans)
