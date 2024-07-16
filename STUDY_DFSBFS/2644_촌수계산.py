import sys

input = sys.stdin.readline
n = int(input())
a, b = map(int, input().split())
m = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
result = []

for _ in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def dfs(v, cnt):
    cnt += 1
    visited[v] = True
    if v == b:
        result.append(cnt)
    for i in arr[v]:
        if not visited[i]:
            dfs(i, cnt)


ans = dfs(a, 0)
if len(result) == 0:
    print(-1)
else:
    print(result[0] - 1)
