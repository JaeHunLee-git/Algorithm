# 최단 경로 = BFS
# 벽을 부수고 간 곳의 visited와 부수지 않고 간 것의 visited는 다름
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[[0] * 2 for _ in range(m)] for __ in range(n)]


def bfs():
    q = deque()
    q.append([0, 0, 0])
    visited[0][0][0] = 1
    while q:
        x, y, check = q.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][check]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == "0" and visited[nx][ny][check] == 0:
                    visited[nx][ny][check] = visited[x][y][check] + 1
                    q.append([nx, ny, check])
                elif (
                    arr[nx][ny] == "1"
                    and check == 0
                    and visited[nx][ny][check + 1] == 0
                ):
                    visited[nx][ny][check + 1] = visited[x][y][check] + 1
                    q.append([nx, ny, check + 1])
    return -1


print(bfs())
# # 이 코드는 그리디 느낌으로 벽을 부숨
# import sys
# from collections import deque

# input = sys.stdin.readline
# n, m = map(int, input().split())
# arr = [input().strip() for _ in range(n)]
# dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
# visited = [[0] * m for _ in range(n)]


# def bfs():
#     q = deque()
#     q.append([0, 0, 0])
#     visited[0][0] = 1
#     while q:
#         x, y, check = q.popleft()
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
#                 if arr[nx][ny] == "0":
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append([nx, ny, check])
#                 elif arr[nx][ny] == "1":
#                     if check == 0:
#                         visited[nx][ny] = visited[x][y] + 1
#                         q.append([nx, ny, 1])
#                     else:
#                         continue


# bfs()
# ans = visited[n - 1][m - 1]
# if ans:
#     print(ans)
# else:
#     print(-1)
