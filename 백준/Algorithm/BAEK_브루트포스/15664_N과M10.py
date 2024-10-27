n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
lst.sort()
visited = [False] * n
tmp = []


def dfs(x):
    if len(tmp) == m:
        print(*tmp)
        return
    remember_me = 0
    for i in range(x, n):
        if not visited[i] and remember_me != lst[i]:
            visited[i] = True
            tmp.append(lst[i])
            remember_me = lst[i]
            dfs(i)
            visited[i] = False
            tmp.pop()


dfs(0)
