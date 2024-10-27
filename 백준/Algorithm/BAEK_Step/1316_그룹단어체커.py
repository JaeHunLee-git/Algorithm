n = int(input())
cnt = 0
for i in range(n):
    err = 0
    a = input()
    a += "!"
    list = []
    for k in range(len(a) - 1):
        if a[k] != a[k + 1]:
            list.append(a[k])
    for q in a:
        if list.count(q) > 1:
            err += 1
    if err == 0:
        cnt += 1


print(cnt)
