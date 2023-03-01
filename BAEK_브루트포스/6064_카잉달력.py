## 약간 공식 느낌

t = int(input())
for _ in range(t):
    check = 0
    m, n, x, y = map(int, input().split())
    ans = 0
    check = 0
    k = x
    while k <= m * n:
        if (k - x) % m == 0 and (k - y) % n == 0:
            ans = k
            check += 1
            break
        k += m
    if check != 0:
        print(ans)
    else:
        print(-1)
