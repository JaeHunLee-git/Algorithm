import sys

input = sys.stdin.readline

n = input().strip()

if n[0] == "d":
    ans = 10
    tmp = 10
else:
    ans = 26
    tmp = 26
for i in range(1, len(n)):
    if n[i] == n[i - 1]:
        ans *= tmp - 1
    else:
        if n[i] == "d":
            tmp = 10
            ans *= tmp
        else:
            tmp = 26
            ans *= tmp
print(ans)
