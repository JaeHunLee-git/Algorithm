from collections import deque
import sys


def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(lst[x])
            break
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= max and lst[i] == 0:
                lst[i] = lst[x] + 1
                q.append(i)


input = sys.stdin.readline
n, k = map(int, input().strip().split())
max = 10 ** 5
lst = [0] * (max + 1)
bfs()

