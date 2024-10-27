# import sys

# input = sys.stdin.readline
# from collections import deque


# def bfs(i, j):
#     visited = [[0] * n for _ in range(n)]
#     q = deque()
#     q.append((i, j))
#     size = 2
#     eat = 0  # 먹은 횟수
#     ans = 0  # 답
#     while q:
#         x, y = q.popleft()
#         if board[x][y] < size and board[x][y] != 0:  # 먹을 수 있는 물고기가 있을 시
#             ans += visited[x][y]  # 먹을 수 있는 물고기가 있으면 visitied를 더함
#             eat += 1  # 먹은 횟수
#             board[x][y] = 0
#             if eat == size:
#                 size += 1
#                 eat = 0
#             q.clear()  # 먹을 시 큐를 비우고 다시 탐색
#             for i in range(n):
#                 for j in range(n):
#                     visited[i][j] = 0

#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
#                 if board[nx][ny] <= size:
#                     visited[nx][ny] = visited[x][y] + 1
#                     q.append((nx, ny))
#     return ans


# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 9:
#             x = i
#             y = j

# dx = [-1, 0, 0, 1]
# dy = [0, -1, 1, 0]


# print(bfs(x, y))

import sys
from collections import deque

input = sys.stdin.readline

# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0
x, y, size = 0, 0, 2
# 상어위치
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x = i
            y = j


def BFS(i, j, shark_size):
    distance = [[0] * n for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
    q = deque()
    q.append((i, j))
    visited[i][j] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
                if board[nx][ny] <= shark_size:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    distance[nx][ny] = distance[x][y] + 1
                    if board[nx][ny] < shark_size and board[nx][ny] != 0:
                        temp.append((nx, ny, distance[nx][ny]))

    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    return sorted(temp, key=lambda x: (-x[2], -x[0], -x[1]))


cnt = 0
result = 0
while 1:
    shark = BFS(x, y, size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
    # 정렬한 결과를 반영해준다.
    nx, ny, dist = shark.pop()

    # 움직이는 칸수가 곧 시간이 된다.
    result += dist
    board[x][y], board[nx][ny] = 0, 0
    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    x, y = nx, ny
    cnt += 1
    if cnt == size:
        size += 1
        cnt = 0
print(result)
