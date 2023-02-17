import sys

n, b = map(int, sys.stdin.readline().split())
tmp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
while n > 0:
    ans += tmp[n % b]
    n //= b

print(ans[::-1])
