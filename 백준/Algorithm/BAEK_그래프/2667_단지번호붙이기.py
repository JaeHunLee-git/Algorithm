# 대각선은 떨어진걸로 간주

import sys


def dfs(i, k):
    global ans
    visited[i][k] = 1
    ans += 1
    if k < n - 1 and lst[i][k + 1] == 1 and visited[i][k + 1] == 0:
        dfs(i, k + 1)

    if i < n - 1 and lst[i + 1][k] == 1 and visited[i + 1][k] == 0:
        dfs(i + 1, k)

    if i > 0 and lst[i - 1][k] == 1 and visited[i - 1][k] == 0:
        dfs(i - 1, k)

    if k > 0 and lst[i][k - 1] == 1 and visited[i][k - 1] == 0:
        dfs(i, k - 1)


input = sys.stdin.readline
n = int(input().strip())
lst = []
visited = [[0] * n for _ in range(n)]
for i in range(n):
    lst.append(list(map(int, input().strip())))
cnt = 0
tmp = []
for i in range(n):
    for k in range(n):
        if lst[i][k] == 1 and visited[i][k] == 0:
            ans = 0
            dfs(i, k)
            tmp.append(ans)
            cnt += 1
print(cnt)
tmp.sort()
for i in tmp:
    print(i)
