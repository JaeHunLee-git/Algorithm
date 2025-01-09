lst = []
for _ in range(9):
    lst.append(int(input()))
lst.sort()
div = sum(lst) - 100
tmp = 0
for i in range(9):
    for k in range(i + 1, 9):
        if lst[i] + lst[k] == div:
            del lst[i]
            del lst[k - 1]
            tmp += 1
            break
    if tmp == 1:
        for q in range(7):
            print(lst[q])
        break
