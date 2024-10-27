## 비 내림차순 순열
import sys

input = sys.stdin.readline

n = int(input())
arr = [1, 5, 10, 50]
tmp = []
ans = set()


def dfs(depth, idx):
    if depth == n:
        ans.add(sum(tmp))
        return

    for i in range(idx, 4):
        tmp.append(arr[i])
        dfs(depth + 1, i)
        tmp.pop()


dfs(0, 0)
print(len(ans))
