n = input()
lst = []
for i in range(len(n)):
    a = ""
    for k in range(i, len(n)):
        a += n[k]
    lst.append(a)
lst.sort()
for i in range(len(lst)):
    print(lst[i])
