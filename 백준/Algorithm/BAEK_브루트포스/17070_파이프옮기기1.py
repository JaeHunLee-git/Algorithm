import sys

input = sys.stdin.readline
n = int(input())
house = [list(map(int, input().split())) for _ in range(n)]
ans = 0


def dfs(x, y, direction):
    global ans
    if x == n - 1 and y == n - 1:
        ans += 1
        return
    if direction == "e":
        if y == n - 1:
            return
        if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
            dfs(x, y + 1, "e")

        if (
            0 <= x + 1 < n
            and 0 <= y + 1 < n
            and house[x][y + 1] == 0
            and house[x + 1][y] == 0
            and house[x + 1][y + 1] == 0
        ):
            dfs(x + 1, y + 1, "c")
    elif direction == "s":
        if x == n - 1:
            return

        if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
            dfs(x + 1, y, "s")

        if (
            0 <= x + 1 < n
            and 0 <= y + 1 < n
            and house[x][y + 1] == 0
            and house[x + 1][y] == 0
            and house[x + 1][y + 1] == 0
        ):
            dfs(x + 1, y + 1, "c")
    else:
        if 0 <= x < n and 0 <= y + 1 < n and house[x][y + 1] == 0:
            dfs(x, y + 1, "e")

        if 0 <= x + 1 < n and 0 <= y < n and house[x + 1][y] == 0:
            dfs(x + 1, y, "s")

        if (
            0 <= x + 1 < n
            and 0 <= y + 1 < n
            and house[x][y + 1] == 0
            and house[x + 1][y] == 0
            and house[x + 1][y + 1] == 0
        ):
            dfs(x + 1, y + 1, "c")


dfs(0, 1, "e")  # e,s,c
print(ans)
