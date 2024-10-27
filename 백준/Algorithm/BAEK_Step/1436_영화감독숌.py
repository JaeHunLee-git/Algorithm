import sys

n = int(sys.stdin.readline())
cnt = 0
start = 666
while cnt < n:
    a = list(map(int, str(start)))
    for i in range(len(a)):
        if i < len(a) - 2 and a[i] == 6 and a[i + 1] == 6 and a[i + 2] == 6:
            cnt += 1
            break
    start += 1
print(start - 1)
