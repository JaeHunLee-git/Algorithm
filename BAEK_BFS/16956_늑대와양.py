import sys

input = sys.stdin.readline
r, c = map(int, input().split())
arr = []
for _ in range(r):
    arr.append(list(map(str, input().strip())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(r):
    for j in range(c):
        if arr[i][j] == "W":
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] == "S":
                    print(0)
                    exit(0)

print(1)
for i in range(r):
    for j in range(c):
        if arr[i][j] == ".":
            arr[i][j] = "D"

for i in arr:
    print("".join(i))
