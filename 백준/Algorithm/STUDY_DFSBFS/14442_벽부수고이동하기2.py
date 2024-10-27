# PyPy3로만 통과
# 벽을 부술 수 있는 수만큼 3차원 배열 생성
# arr[nx][ny] == "1" and check < k and visited[nx][ny][check + 1] == 0
# 위의 코드를
# arr[nx][ny] == "1" and check < k and visited[nx][ny][check] == 0
# 로 해서 시간초과 났었음 (배열이 커서 한 틱 차이가 큼)
import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
arr = [input().strip() for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
visited = [[[0] * (k + 1) for _ in range(m)] for __ in range(n)]


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
                    arr[nx][ny] == "1" and check < k and visited[nx][ny][check + 1] == 0
                ):
                    visited[nx][ny][check + 1] = visited[x][y][check] + 1
                    q.append([nx, ny, check + 1])
    return -1


print(bfs())
