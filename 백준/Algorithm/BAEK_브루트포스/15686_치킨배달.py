import sys
from itertools import combinations

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

arr_house = []
arr_chick = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            arr_house.append([i, j])
        elif arr[i][j] == 2:
            arr_chick.append([i, j])

com_chick = list(combinations(arr_chick, m))

ans = 1e9
for i in com_chick:
    dis = 0
    for j in arr_house:
        tmp = []
        for k in range(m):
            tmp.append(abs(i[k][0] - j[0]) + abs(i[k][1] - j[1]))
        dis += min(tmp)
    ans = min(dis, ans)
print(ans)
