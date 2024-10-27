import sys

input = sys.stdin.readline


def dfs(x, y, n):
    global ans_minus, ans_zero, ans_plus
    tmp = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if tmp != arr[i][j]:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return
    if tmp == -1:
        ans_minus += 1
    elif tmp == 0:
        ans_zero += 1
    else:
        ans_plus += 1


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
ans_minus = 0
ans_zero = 0
ans_plus = 0
dfs(0, 0, n)
print(f"{ans_minus}\n{ans_zero}\n{ans_plus}")
