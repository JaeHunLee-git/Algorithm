import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def dfs(i, k):
    visited[i][k] = 1
    if k < w - 1 and lst[i][k + 1] == 1 and visited[i][k + 1] == 0:
        dfs(i, k + 1)

    if (
        i < h - 1
        and k < w - 1
        and lst[i + 1][k + 1] == 1
        and visited[i + 1][k + 1] == 0
    ):
        dfs(i + 1, k + 1)

    if i < h - 1 and lst[i + 1][k] == 1 and visited[i + 1][k] == 0:
        dfs(i + 1, k)

    if i < h - 1 and k > 0 and lst[i + 1][k - 1] == 1 and visited[i + 1][k - 1] == 0:
        dfs(i + 1, k - 1)
    if i > 0 and k > 0 and lst[i - 1][k - 1] == 1 and visited[i - 1][k - 1] == 0:
        dfs(i - 1, k - 1)
    if i > 0 and lst[i - 1][k] == 1 and visited[i - 1][k] == 0:
        dfs(i - 1, k)
    if i > 0 and k < w - 1 and lst[i - 1][k + 1] == 1 and visited[i - 1][k + 1] == 0:
        dfs(i - 1, k + 1)
    if k > 0 and lst[i][k - 1] == 1 and visited[i][k - 1] == 0:
        dfs(i, k - 1)


while True:
    w, h = map(int, input().strip().split())
    cnt = 0
    if w == 0 and h == 0:
        break
    lst = []
    for i in range(h):
        lst.append(list(map(int, input().strip().split())))
    visited = [[0] * w for i in range(h)]
    for i in range(h):
        for k in range(w):
            if lst[i][k] == 1 and visited[i][k] == 0:
                dfs(i, k)
                cnt += 1
    print(cnt)
