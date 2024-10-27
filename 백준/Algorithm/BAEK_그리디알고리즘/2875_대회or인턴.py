import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

ans = 0

while n > 1 and m > 0:
    ans += 1
    n -= 2
    m -= 1

k -= m + n

while k > 0:
    ans -= 1
    k -= 3
print(ans)
