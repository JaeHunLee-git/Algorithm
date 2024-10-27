e, s, m = map(int, input().split())
a = 1
b = 1
c = 1
cnt = 1
while a != e or b != s or c != m:
    cnt += 1
    a += 1
    b += 1
    c += 1
    if a > 15:
        a -= 15
    if b > 28:
        b -= 28
    if c > 19:
        c -= 19
print(cnt)
