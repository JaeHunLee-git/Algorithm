import sys

input = sys.stdin.readline
n, k = map(int, input().split())

a = []
for _ in range(n):
    a.append(int(input()))

a.sort(reverse=True)

ans = 0
for i in a:
    if i <= k:
        ans += k // i
        k %= i
print(ans)