import sys

T = int(sys.stdin.readline())
a = []
for _ in range(T):
    a.append(int(sys.stdin.readline()))

a.sort()
for _ in range(T):
    print(a[_])
