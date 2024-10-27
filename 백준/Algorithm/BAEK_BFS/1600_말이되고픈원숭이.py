import sys
from collections import deque

input = sys.stdin.readline
k = int(input())
w, h = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(h)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
horse_dx = [1, 1, 2, 2, -1, -1, -2, -2]
horse_dy = [-2, 2, -1, 1, 2, -2, 1, -1]
visited = [[[0] * (k + 1) for _ in range(w)] for _ in range(h)]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1:
            return visited[x][y][z] - 1
        if z < k:
            for i in range(8):
                nx = x + horse_dx[i]
                ny = y + horse_dy[i]
                if (
                    0 <= nx < h
                    and 0 <= ny < w
                    and arr[nx][ny] == 0
                    and not visited[nx][ny][z + 1]
                ):
                    visited[nx][ny][z + 1] = visited[x][y][z] + 1
                    q.append([nx, ny, z + 1])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < h
                and 0 <= ny < w
                and not visited[nx][ny][z]
                and arr[nx][ny] == 0
            ):
                visited[nx][ny][z] = visited[x][y][z] + 1
                q.append([nx, ny, z])
    return -1


print(bfs())
