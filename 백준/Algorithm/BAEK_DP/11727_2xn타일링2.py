n = int(input())
lst = [0, 1, 3]
for i in range(3, 1001):
    lst.append((lst[i - 1] + 2 * lst[i - 2]) % 10007)
print(lst[n])
