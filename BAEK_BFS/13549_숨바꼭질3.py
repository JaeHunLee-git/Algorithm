import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * (200001)
visited[n] = 1


def bfs(p):
    q = deque()
    time = 0
    q.append([p, time])
    while q:
        x, cnt = q.popleft()
        if x == k:
            return cnt
        if 0 < x * 2 < 100001 and visited[x * 2] == 0:  ## **부호문제**
            visited[x * 2] = 1
            q.appendleft([x * 2, cnt])
        if 0 <= x - 1 < 100001 and visited[x - 1] == 0:
            visited[x - 1] = 1
            q.append([x - 1, cnt + 1])
        if 0 <= x + 1 < 100001 and visited[x + 1] == 0:
            visited[x + 1] = 1
            q.append([x + 1, cnt + 1])


print(bfs(n))
