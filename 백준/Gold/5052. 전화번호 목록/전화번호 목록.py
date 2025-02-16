import sys
import bisect

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ans = "YES"
    n = int(input())
    arr = [input().strip() for i in range(n)]
    arr.sort()
    for i in range(n - 1):
        if arr[i + 1].startswith(arr[i]):
            ans = "NO"
    print(ans)
