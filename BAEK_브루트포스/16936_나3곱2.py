import sys

input = sys.stdin.readline
n = int(input())
b = list(map(int, input().split()))
a = []


def dfs(idx, tmp):
    if idx == n:
        print(*a)
        exit(0)

    for j in range(len(b)):
        if tmp % 3 == 0 and tmp // 3 == b[j] and (b[j] not in a):
            a.append(b[j])
            dfs(idx + 1, b[j])
            a.pop()
        if tmp * 2 == b[j] and (b[j] not in a):
            a.append(b[j])
            dfs(idx + 1, b[j])
            a.pop()


for i in range(n):
    a.append(b[i])
    dfs(1, b[i])
    a.pop()
