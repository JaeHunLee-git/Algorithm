import sys

input = sys.stdin.readline

n = int(input())
ans = -1
tmp = n // 5

while tmp > -1:
    n -= 5 * tmp
    if n % 3 == 0:
        ans = tmp + (n // 3)
        break
    else:
        n += 5 * tmp
        tmp -= 1

print(ans)
