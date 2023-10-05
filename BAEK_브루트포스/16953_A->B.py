import sys
from collections import deque

input = sys.stdin.readline
a, b = map(int, input().split())


def bfs(x, cnt):
    q = deque()
    q.append((x, cnt))
    while q:
        y, ans = q.popleft()
        if y == b:
            print(ans + 1)
            return
        elif y > b:
            continue
        q.append((y * 2, ans + 1))
        q.append((10 * y + 1, ans + 1))
    print(-1)
    return


bfs(a, 0)
