import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
## s=현재위치, g=도달할 위치


visited = [0] * (f + 1)
visited[s] = 1


def bfs(x, cnt):
    q = deque()
    q.append([x, cnt])
    while q:
        nx, ans = q.popleft()
        if nx == g:
            print(ans)
            return
        for i in range(2):
            if i == 0:
                nx += u
                if 0 < nx <= f and visited[nx] == 0:
                    visited[nx] = 1
                    q.append([nx, ans + 1])
                nx -= u
            else:
                nx -= d
                if 0 < nx <= f and visited[nx] == 0:
                    visited[nx] = 1
                    q.append([nx, ans + 1])
                nx += d
    print("use the stairs")
    return


bfs(s, 0)
