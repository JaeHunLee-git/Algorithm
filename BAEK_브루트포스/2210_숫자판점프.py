import sys

input = sys.stdin.readline
arr = []
for _ in range(5):
    arr.append(list(input().split()))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

ans = set()


def dfs(x, y, cnt, tmp):
    global ans
    if cnt == 6:
        ans.add(tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            tmp += arr[nx][ny]
            dfs(nx, ny, cnt + 1, tmp)
            tmp = tmp[:-1]


for x in range(5):
    for y in range(5):
        tmp1 = arr[x][y]
        dfs(x, y, 1, tmp1)

print(len(ans))
