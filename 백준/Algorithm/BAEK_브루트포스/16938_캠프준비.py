import sys

input = sys.stdin.readline

n, l, r, x = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0


def dfs(cnt, prob, idx):
    global ans

    if cnt == prob and l <= sum(tmp) <= r and max(tmp) - min(tmp) >= x:
        ans += 1
        return

    for i in range(idx, n):
        tmp.append(arr[i])
        dfs(cnt + 1, prob, i + 1)
        tmp.pop()


for prob in range(2, n + 1):
    tmp = []
    dfs(0, prob, 0)
print(ans)
