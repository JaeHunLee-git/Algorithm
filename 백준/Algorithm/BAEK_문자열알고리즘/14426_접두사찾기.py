# import sys
# input = sys.stdin.readline
# n, m = map(int, input().split())
# s = [input().strip() for _ in range(n)]
# p = [input().strip() for _ in range(m)]
# ans = 0
# s.sort()
# p.sort()
# tmp = 0

# for i in p:
#     for j in range(tmp, n):
#         if s[j].startswith(i):
#             ans += 1
#             tmp = j
#             break
# print(ans)
import bisect

n, m = map(int, input().split())
tmp = []
for _ in range(n):
    S = input()
    tmp.append(S)

tmp.sort()
cnt = 0
for _ in range(m):
    S = input()
    idx = bisect.bisect_left(tmp, S)
    if idx != len(tmp):
        target = tmp[idx]
        if S == target[: len(S)]:
            cnt += 1

print(cnt)