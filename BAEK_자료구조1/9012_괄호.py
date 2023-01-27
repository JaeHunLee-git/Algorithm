import sys

T = int(input())
for _ in range(T):
    cnt = 0
    a = list(sys.stdin.readline())
    for i in range(len(a)):
        if a[i] == "(":
            cnt += 1
        elif a[i] == ")":
            cnt -= 1
        if cnt < 0:
            cnt = -1
            break
    if cnt == 0:
        print("YES")
    else:
        print("NO")
