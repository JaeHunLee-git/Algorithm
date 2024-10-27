import sys
from collections import deque

input = sys.stdin.readline

m, n, k = map(int, input().split())
arr = [[0] * n for _ in range(m)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
for _ in range(k):  ## 직사각형의 영역을 1로 채움
    sx, sy, ex, ey = map(int, input().split())
    sy = m - 1 - sy
    ex -= 1
    ey = m - ey
    # [sy][sx]부터 [ey][ex]
    tmp_x = ey
    while tmp_x <= sy:
        tmp_y = sx
        while tmp_y <= ex:
            arr[tmp_x][tmp_y] = 1
            tmp_y += 1
        tmp_x += 1


def bfs(x, y):
    q = deque()
    q.append([x, y])
    tmp = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 0:
                tmp += 1
                arr[nx][ny] = 1
                q.append([nx, ny])
    return tmp


cnt = 0
ans = []
for i in range(m):
    for j in range(n):
        if arr[i][j] == 0:
            arr[i][j] = 1
            ans.append(bfs(i, j))
            cnt += 1
print(cnt)
ans.sort()
for i in range(cnt):
    print(ans[i], end=" ")
