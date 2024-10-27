import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
q = deque()

for _ in range(k):
    tmp = int(input())
    if tmp == 0:
        if len(q) > 0:
            q.pop()
    else:
        q.append(tmp)
print(sum(q))
