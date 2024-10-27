import sys
import bisect

input = sys.stdin.readline
t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = 0
asum = []
bsum = []
for i in range(n):
    tmp = a[i]
    asum.append(tmp)
    for j in range(i + 1, n):
        tmp += a[j]
        asum.append(tmp)

for i in range(m):
    tmp = b[i]
    bsum.append(tmp)
    for j in range(i + 1, m):
        tmp += b[j]
        bsum.append(tmp)

asum.sort()
bsum.sort()

for i in range(len(asum)):
    l = bisect.bisect_left(bsum, t - asum[i])
    r = bisect.bisect_right(bsum, t - asum[i])
    ans += r - l
print(ans)
