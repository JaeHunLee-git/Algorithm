T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    tmp = min(a, b)
    min = 0
    max = 0
    for i in range(1, tmp + 1):
        if a % i == 0 and b % i == 0 and i > max:
            max = i
            min = max * (a // i) * (b // i)
    print(min)
    del min
