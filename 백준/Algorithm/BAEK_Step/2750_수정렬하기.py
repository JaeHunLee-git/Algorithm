T = int(input())
a = []
for _ in range(T):
    a.append(int(input()))

a.sort()
for _ in range(T):
    print(a[_])
