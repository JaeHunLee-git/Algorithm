import sys
import copy
from itertools import permutations


def dfs():
    print()


input = sys.stdin.readline
n, m, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
arr_k = []
for _ in range(k):
    arr_k.append(list(map(int, input().split())))
ans = 1e9

for i in permutations(arr_k, k):
    tmp_a = copy.deepcopy(a)
    for r, c, s in i:
        r -= 1
        c -= 1
        for n in range(s, 0, -1):  # s부터 시작해서  1까지 역순으로
            tmp = tmp_a[r - n][c + n]
            tmp_a[r - n][c - n + 1 : c + n + 1] = tmp_a[r - n][c - n : c + n]  # 오
            for row in range(r - n, r + n):  # 위
                tmp_a[row][c - n] = tmp_a[row + 1][c - n]
            tmp_a[r + n][c - n : c + n] = tmp_a[r + n][c - n + 1 : c + n + 1]  # 왼
            for row in range(r + n, r - n, -1):  # 아래
                tmp_a[row][c + n] = tmp_a[row - 1][c + n]
            tmp_a[r - n + 1][c + n] = tmp
    for k in tmp_a:
        ans = min(ans, sum(k))

print(ans)
