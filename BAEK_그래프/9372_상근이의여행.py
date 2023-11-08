import sys

input = sys.stdin.readline
t = int(input())


def dfs(i, cnt):
    check[i] = 1
    for n in arr[i]:
        if check[n] == 0:
            cnt = dfs(n, cnt + 1)
    return cnt


for _ in range(t):
    n, m = map(int, input().split())
    arr = [[] for i in range(n + 1)]
    for i in range(m):
        u, v = map(int, input().split())
        arr[u].append(v)
        arr[v].append(u)
    check = [0] * (n + 1)
    print(dfs(1, 0))
