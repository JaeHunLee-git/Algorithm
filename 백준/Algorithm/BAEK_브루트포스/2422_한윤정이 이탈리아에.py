import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
ban = [[False for i in range(n)] for _ in range(n)]
for i in range(m):
    tmp1, tmp2 = map(int, input().split())
    ban[tmp1 - 1][tmp2 - 1] = True
    ban[tmp2 - 1][tmp1 - 1] = True   # 순서를 오름차순으로 준다는 가정이 없기 때문

cnt = 0
com_list = list(combinations(range(n), 3))

for i in com_list:
    if ban[i[0]][i[1]] or ban[i[1]][i[2]] or ban[i[0]][i[2]]:
        continue
    cnt += 1
print(cnt)
