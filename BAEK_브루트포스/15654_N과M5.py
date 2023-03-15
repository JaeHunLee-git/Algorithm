## visited는 순열에서 중복 조건을 해결하기 위해 사용
## dfs()안에 숫자를 넣는 것은 오름차순인 순열만 사용하기 위해 사용

import sys
from itertools import permutations


def dfs():
    if len(s) == m:
        print(" ".join(map(str, s)))
        return
    for i in range(0, n):
        if visited[i]:
            continue
        visited[i] = True
        s.append(lst[i])
        dfs()
        s.pop()
        visited[i] = False


input = sys.stdin.readline
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = []
visited = [False] * (n)
dfs()
