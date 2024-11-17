n = int(input())
tmp = [input().strip() for _ in range(n)]
arr = []
for i in range(n):
    lst = []
    for j in range(n):
        lst.append(int(tmp[i][j]))
    arr.append(lst)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y):
    global house_cnt
    arr[x][y] = cnt
    house_cnt += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1:
            dfs(nx, ny)


ans_cnt = []
cnt = 1
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            house_cnt = 0
            cnt += 1
            dfs(i, j)
            ans_cnt.append(house_cnt)

print(cnt - 1)
ans_cnt.sort()
for count in ans_cnt:
    print(count)
