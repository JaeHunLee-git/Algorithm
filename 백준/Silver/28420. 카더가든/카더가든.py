## 누적합을 이용
import sys

INF = 2**31 - 1
N, M = map(int, sys.stdin.readline().split())
a, b, c = map(int, sys.stdin.readline().split())
board = []
row_sum = []
col_sum = []

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
    tmp = [0]
    for j in range(1, M + 1):
        tmp.append(board[-1][j - 1] + tmp[j - 1])
    row_sum.append(tmp)

for i in range(M):
    tmp = [0]
    for j in range(1, N + 1):
        tmp.append(board[j - 1][i] + tmp[j - 1])
    col_sum.append(tmp)


def prix_sum(arr, a, b):
    return arr[b] - arr[a]


def way1(x, y):
    if x + a > N or y + b + c > M:
        return INF
    res = 0
    for i in range(x, x + a):
        res += prix_sum(row_sum[i], y, y + b + c)
    return res


def way2(x, y):
    if x + a > N or y + c > M or x + a + b > N or y + c + a > M:
        return INF
    res = 0
    for i in range(x, x + a):
        res += prix_sum(row_sum[i], y, y + c)
    for i in range(y + c, y + c + a):
        res += prix_sum(col_sum[i], x + a, x + a + b)
    return res


def way3(x, y):
    if x + a > N or y + b > M or x + a + c > N or y + b + a > M:
        return INF
    res = 0
    for i in range(x, x + a):
        res += prix_sum(row_sum[i], y, y + b)
    for i in range(y + b, y + b + a):
        res += prix_sum(col_sum[i], x + a, x + a + c)
    return res


ans = INF
for i in range(N):
    for j in range(M):
        ans = min(ans, way1(i, j), way2(i, j), way3(i, j))

print(ans)

## 시간초과코드
# import sys

# input = sys.stdin.readline
# n, m = map(int, input().split())
# a, b, c = map(int, input().split())

# arr = [list(map(int, input().split())) for _ in range(n)]
# ans = 1e9

# for i in range(n):
#     for j in range(m):
#         if 0 <= (i + a - 1) < n and 0 <= j + b + c - 1 < m:
#             tmp = 0
#             for x in range(i, i + a):
#                 for y in range(j, j + b + c):
#                     tmp += arr[x][y]
#             if tmp < ans:
#                 ans = tmp
#         if 0 <= (i + a + b - 1) < n and 0 <= j + a + c - 1 < m:
#             tmp = 0
#             for x in range(i, i + a):
#                 for y in range(j, j + c):
#                     tmp += arr[x][y]
#             for x in range(i + a, i + a + b):
#                 for y in range(j + c, j + c + a):
#                     tmp += arr[x][y]
#             if tmp < ans:
#                 ans = tmp
#         if 0 <= (i + a + c - 1) < n and 0 <= j + b + a - 1 < m:
#             tmp = 0
#             for x in range(i, i + a):
#                 for y in range(j, j + b):
#                     tmp += arr[x][y]
#             for x in range(i + a, i + a + c):
#                 for y in range(j + b, j + b + a):
#                     tmp += arr[x][y]
#             if tmp < ans:
#                 ans = tmp
#         else:
#             continue
# # i, j = 4, 1
# # tmp = 0
# # for x in range(i, i + a):
# #     for y in range(j, j + c):
# #         tmp += arr[x][y]
# # for x in range(i + a, i + a + b):
# #     for y in range(j + c, j + c + a):
# #         tmp += arr[x][y]
# # print(tmp)
# print(ans)
