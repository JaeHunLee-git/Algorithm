import sys


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(0, n):
        s.append(lst[i])
        dfs()
        s.pop()


input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []

dfs()
