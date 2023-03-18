import sys


def dfs(x):
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(x, n):
        s.append(lst[i])
        dfs(i + 1)
        s.pop()


input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []

dfs(0)
