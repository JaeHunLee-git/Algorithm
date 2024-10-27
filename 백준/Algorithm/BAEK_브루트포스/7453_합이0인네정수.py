import sys
import bisect

input = sys.stdin.readline

n = int(input())
a = []
b = []
c = []
d = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp[0])
    b.append(tmp[1])
    c.append(tmp[2])
    d.append(tmp[3])

ans = 0
ab = dict()
for A in a:
    for B in b:
        v = A + B
        if v not in ab.keys():
            ab[v] = 1
        else:
            ab[v] += 1

for C in c:
    for D in d:
        v = -(C + D)
        if v in ab.keys():
            ans += ab[v]
print(ans)
# absum = []
# cdsum = []

# for i in range(n):
#     tmp = a[i]
#     for j in range(n):
#         tmp = a[i] + b[j]
#         absum.append(tmp)

# for i in range(n):
#     tmp = c[i]
#     for j in range(n):
#         tmp = c[i] + d[j]
#         cdsum.append(tmp)

# absum.sort()
# cdsum.sort()
# ans = 0

# for i in range(len(absum)):
#     l = bisect.bisect_left(cdsum, -absum[i])
#     r = bisect.bisect_right(cdsum, -absum[i])
#     ans += r - l
# print(ans)
