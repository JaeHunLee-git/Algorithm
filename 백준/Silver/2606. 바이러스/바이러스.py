n = int(input())
t = int(input())
arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(t):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1
visited = [0] * (n + 1)


def dfs(v):
    visited[v] = 1
    for i in range(n + 1):
        if arr[v][i] == 1 and visited[i] == 0:
            dfs(i)


dfs(1)

ans = 0
for i in visited:
    if i == 1:
        ans += 1
print(ans - 1)
