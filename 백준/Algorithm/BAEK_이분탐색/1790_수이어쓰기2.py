import sys

input = sys.stdin.readline

n, k = map(int, input().split())

tmp = 1

while k > 0:
    k -= tmp * (9 * (10 ** (tmp - 1)))
    tmp += 1
tmp -= 1
k += tmp * (9 * (10 ** (tmp - 1)))

ans = 10 ** (tmp - 1)
k -= tmp
while k > 0:
    k -= tmp
    ans += 1
k += tmp
ans = str(ans)
if int(ans) > n:
    print(-1)
else:
    print(int(ans[k - 1]))
