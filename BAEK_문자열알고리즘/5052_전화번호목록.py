import sys
import bisect

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    ans = "YES"
    n = int(input())
    arr = [int(input()) for i in range(n)]
    arr.sort()
    for i in range(n):
        for j in range(i + 1, n):
            print()
