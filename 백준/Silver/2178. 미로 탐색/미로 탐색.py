from collections import deque

n, m = map(int, input().split())
arr = []
for _ in range(n):
    tmp = input().strip()
    tmp_lst = []
    for k in tmp:
        tmp_lst.append(int(k))
    arr.append(tmp_lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

visited = [[0] * m for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if nx == n - 1 and ny == m - 1:
                    return visited[x][y] + 1
                if arr[nx][ny] == 1 and visited[nx][ny] == 0:
                    q.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1


print(bfs(0, 0) + 1)
