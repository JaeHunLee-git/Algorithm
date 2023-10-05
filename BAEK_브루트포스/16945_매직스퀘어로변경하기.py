# import sys

# a = [0] * 9
# b = [0] * 9
# ans = 1e9
# visited = [False] * 10


# def cal_cost():  # 비용 계산
#     cost = 0
#     for i in range(9):
#         tmp = abs(a[i] - b[i])
#         cost += tmp
#     return cost


# def check():  # 매직 스퀘어인지 확인
#     global ans
#     sum_val = b[0] + b[1] + b[2]

#     for i in range(3):
#         tsum = 0
#         for j in range(3):
#             tsum += b[i * 3 + j]
#         if sum_val != tsum:
#             return False

#     for i in range(3):
#         tsum = 0
#         for j in range(0, 9, 3):
#             tsum += b[i + j]
#         if sum_val != tsum:
#             return False

#     tsum = b[0] + b[4] + b[8]
#     if sum_val != tsum:
#         return False

#     tsum = b[2] + b[4] + b[6]
#     if sum_val != tsum:
#         return False

#     return True


# def dfs(idx):  # 1~9의 순열
#     global ans
#     if idx == 9:
#         if check():
#             ans = min(ans, cal_cost())
#         return

#     for i in range(1, 10):
#         if visited[i]:
#             continue
#         visited[i] = True
#         b[idx] = i
#         dfs(idx + 1)
#         visited[i] = False


# a = []
# for _ in range(3):
#     row = list(map(int, input().split()))
#     a.extend(row)  # 각 행의 원소를 하나의 리스트로 확장
# dfs(0)
# print(ans)

import sys
from itertools import permutations

a = [list(map(int, input().split())) for _ in range(3)]

a_per = list(permutations(range(1, 10), 9))

ans = 1e9


def cal_cost(i):  # 비용 계산
    cost = 0
    for j in range(3):
        tmp = abs(i[j] - a[0][j])
        cost += tmp
    cost += abs(i[3] - a[1][0]) + abs(i[4] - a[1][1]) + abs(i[5] - a[1][2])
    cost += abs(i[6] - a[2][0]) + abs(i[7] - a[2][1]) + abs(i[8] - a[2][2])
    return cost


def check(i):  # 매직 스퀘어인지 확인
    sum_val = i[0] + i[1] + i[2]

    for k in range(3):
        tsum = 0
        for j in range(3):
            tsum += i[k * 3 + j]
        if sum_val != tsum:
            return False

    for k in range(3):
        tsum = 0
        for j in range(0, 9, 3):
            tsum += i[k + j]
        if sum_val != tsum:
            return False

    tsum = i[0] + i[4] + i[8]
    if sum_val != tsum:
        return False

    tsum = i[2] + i[4] + i[6]
    if sum_val != tsum:
        return False

    return True


for i in a_per:
    if check(i):
        ans = min(ans, cal_cost(i))
print(ans)
