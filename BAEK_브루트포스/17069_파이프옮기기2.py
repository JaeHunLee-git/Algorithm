# 로봇 계단 오르기와 비슷
import sys

input = sys.stdin.readline
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
# dp[x][x][0] = 가로, dp[x][x][1] = 세로, dp[x][x][2] = 대각선
dp[0][1][0] = 1
for i in range(1, N):
    if m[0][i] == 1:
        break
    else:
        dp[0][i][0] = 1

for i in range(1, N):
    for j in range(2, N):
        if not m[i][j]:
            # 가로
            dp[i][j][0] = dp[i][j - 1][0] + dp[i][j - 1][2]
        if not m[i][j]:
            # 세로
            dp[i][j][1] = dp[i - 1][j][1] + dp[i - 1][j][2]
        if not m[i][j - 1] and not m[i - 1][j] and not m[i][j]:
            # 대각선
            dp[i][j][2] = (
                dp[i - 1][j - 1][1] + dp[i - 1][j - 1][0] + dp[i - 1][j - 1][2]
            )

print(sum(dp[-1][-1]))
