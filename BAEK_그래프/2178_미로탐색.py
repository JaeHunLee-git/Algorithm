# 최단거리는 bfs로
import sys
from collections import deque


def bfs(i, k):
    q = deque([[i, k]])
    while q:
        i, k = q.popleft()
        for x in dir:
            ni = i + x[0]
            nk = k + x[1]
            if i == n - 1 and k == m - 1:
                print(lst[n - 1][m - 1])
                break
            if 0 <= ni < n and 0 <= nk < m:
                if visited[ni][nk] == 0 and lst[ni][nk] == 1:
                    lst[ni][nk] = lst[i][k] + 1
                    visited[ni][nk] = 1
                    q.append([ni, nk])


input = sys.stdin.readline
n, m = map(int, input().strip().split())
lst = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

bfs(0, 0)

