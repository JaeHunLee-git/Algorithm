import sys

n = int(sys.stdin.readline())
cnt = 0
for i in range(1, n + 1):
    b = list(map(int, str(i)))
    if n == i + sum(b):
        print(i)
        cnt += 1
        break
if cnt == 0:
    print(0)
