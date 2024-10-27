import sys
from collections import deque


def bfs():
    visited = [-1] * 100001
    visited[n] = 0
    q = deque([n])

    while q:
        x = q.popleft()

        if x == k:
            return visited[x]

        for i in (x + 1, x - 1, x * 2):

            if 0 <= i <= 100000 and visited[i] == -1:

                if i == x * 2:
                    visited[i] = visited[x]
                    q.appendleft(i)

                else:
                    visited[i] = visited[x] + 1
                    q.append(i)


n, k = map(int, sys.stdin.readline().split())
print(bfs())
