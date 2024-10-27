# 메모리 초과
# import sys
# from itertools import combinations

# input = sys.stdin.readline
# n, m = map(int, input().split())
# rela = [list(map(int, input().split())) for _ in range(m)]
# person = list(combinations(range(1, n+1), 3))
# for i in range(m):
#     if rela[i][0] > rela[i][1]:
#         tmp = rela[i][0]
#         rela[i][0] = rela[i][1]
#         rela[i][1] = tmp
# rela.sort(key=lambda x: x[0])

# ans = float("inf")
# for i in person:
#     if [i[0], i[1]] in rela and [i[0], i[2]] in rela and [i[1], i[2]] in rela:
#         cnt = 0
#         for k in rela:
#             if k[0] == i[0] or k[1] == i[0]:
#                 cnt += 1
#             if k[0] == i[1] or k[1] == i[1]:
#                 cnt += 1
#             if k[0] == i[2] or k[1] == i[2]:
#                 cnt += 1
#         ans = min(ans, cnt - 6)
# if ans == float("inf"):
#     print(-1)
# else:
#     print(ans)
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
rela = [[False for _ in range(n)] for _ in range(n)]  # 친구 여부
cnt = [0 for _ in range(n)]  # 친구 수
for i in range(m):
    i1, i2 = map(int, input().split())
    rela[i1 - 1][i2 - 1] = True
    rela[i2 - 1][i1 - 1] = True
    cnt[i1 - 1] += 1
    cnt[i2 - 1] += 1
result = 12001

for i in range(n):
    for j in range(i + 1, n):
        if not rela[i][j]:  # A와 B가 친구가 아닌 경우
            continue
        for k in range(j + 1, n):
            if not rela[i][k] or not rela[j][k]:  # A와 C 또는 B와 C가 친구가 아닌 경우
                continue
            result = min(result, cnt[i] + cnt[j] + cnt[k] - 6)

if result == 12001:
    print(-1)
else:
    print(result)
