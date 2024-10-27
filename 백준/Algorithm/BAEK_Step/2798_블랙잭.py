import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()
ans = 0
for i in range(n - 2):
    k = 1
    while k < n - 1:
        for _ in range(1, n - i - k):
            max = lst[i] + lst[i + k] + lst[i + k + _]
            if ans < max <= m:
                ans = max
        k += 1
print(ans)
