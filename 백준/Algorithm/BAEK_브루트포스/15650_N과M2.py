from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

p = list(permutations(nums, m))
for i in p:
    a = str(" ".join(map(str, i)))
    cnt = 0
    for k in range(0, len(a) - 2)[0 : len(a) - 2 : 2]:
        if a[k] > a[k + 2]:
            cnt += 1
    if cnt == 0:
        print(a)
