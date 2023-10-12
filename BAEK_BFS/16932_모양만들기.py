import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0


def bfs(i, j):
    cnt = 1
    q = deque()
    q.append([i, j])
    visited[i][j] = num
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = num
                cnt += 1
                q.append([nx, ny])
    return cnt


num = 2
group = [0] * (n * m)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not visited[i][j]:
            cnt = bfs(i, j)
            group[num] = cnt
            num += 1

result = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            s = []
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if (
                    0 <= nx < n
                    and 0 <= ny < m
                    and arr[nx][ny] == 1
                    and visited[nx][ny] not in s
                ):
                    s.append(visited[nx][ny])
            tmp = 1
            for ss in s:
                tmp += group[ss]
            result = max(result, tmp)
print(result)
