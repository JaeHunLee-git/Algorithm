import sys

input = sys.stdin.readline
remain = 1000 - int(input())
ans = 0
arr = [500, 100, 50, 10, 5, 1]
for i in arr:
    while remain >= i:
        ans += 1
        remain -= i
print(ans)
