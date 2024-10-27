import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]
arr_tmp = [[0] * m for _ in range(n)]

ans = 0

for i in range(n):
    for j in range(m):
        if arr_tmp[i][j] == 0:
            ans += 1
            if arr[i][j] == "-":
                arr_tmp[i][j] = 1
                tmp = j + 1
                while tmp < m:
                    if arr[i][tmp] == "-":
                        arr_tmp[i][tmp] = 1
                    else:
                        break
                    tmp += 1
            elif arr[i][j] == "|":
                arr_tmp[i][j] = 1
                tmp = i + 1
                while tmp < n:
                    if arr[tmp][j] == "|":
                        arr_tmp[tmp][j] = 1
                    else:
                        break
                    tmp += 1
print(ans)
