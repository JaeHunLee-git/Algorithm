import sys
from collections import deque

input = sys.stdin.readline
s, t = map(int, input().split())
queue = deque()
check = set()
queue.append((s, ""))
check.add(s)
MAX = 10e9

if s == t:
    print(0)
else:
    tmp = -1
    while queue:
        s1, ans = queue.popleft()
        if s1 == t:
            tmp = ans
            print(tmp)
            exit(0)

        s2 = s1 * s1
        if 0 <= s2 <= MAX and s2 not in check:
            queue.append((s2, ans + "*"))
            check.add(s2)

        s2 = s1 + s1
        if 0 <= s2 <= MAX and s2 not in check:
            queue.append((s2, ans + "+"))
            check.add(s2)

        s2 = 1
        if s2 not in check:
            queue.append((s2, ans + "/"))
            check.add(s2)
    print(tmp)
