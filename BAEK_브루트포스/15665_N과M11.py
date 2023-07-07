n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
lst.sort()
tmp = []


def dfs():
    if len(tmp) == m:
        print(*tmp)
        return
    remember_me = 0
    for i in range(n):
        if remember_me != lst[i]:
            tmp.append(lst[i])
            remember_me = lst[i]
            dfs()
            tmp.pop()


dfs()

