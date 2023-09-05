import sys

input = sys.stdin.readline

n = int(input())
man = list(map(int, input().split()))
ans = 0
man.sort()
k = n - 1
for i in range(1, n + 1):
    ans += man[k] * i
    k -= 1
print(ans)
