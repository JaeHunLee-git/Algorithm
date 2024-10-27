import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += arr[j]
        if tmp == m:
            ans += 1
            break
        elif tmp > m:
            break
print(ans)
