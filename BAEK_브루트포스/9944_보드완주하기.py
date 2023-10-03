import sys

input = sys.stdin.readline
case = 1
d = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def backTracking(x, y, cnt):
    global ans
    if all("." not in row for row in board):
        ans = min(ans, cnt)
    if cnt < ans:
        for i in range(4):
            tmp = []
            nx = x
            ny = y
            while True:
                nx += d[i][0]
                ny += d[i][1]
                if 0 <= ny < m and 0 <= nx < n and board[nx][ny] == ".":
                    tmp.append([nx, ny])
                    board[nx][ny] = "*"
                else:
                    break
            if tmp:
                backTracking(nx - d[i][0], ny - d[i][1], cnt + 1)
            for a, b in tmp:
                board[a][b] = "."
        board[x][y] = "."


while True:
    try:
        n, m = map(int, input().split())
        visited = [[False] * m for _ in range(n)]
        board = [list(input().strip()) for _ in range(n)]
        ans = 1000001
        for i in range(n):
            for j in range(m):
                if board[i][j] == ".":
                    board[i][j] = "*"
                    backTracking(i, j, 0)
        if ans == 1000001:
            ans = -1
        print(f"Case {case}: {ans}")
        case += 1
    except:
        break
