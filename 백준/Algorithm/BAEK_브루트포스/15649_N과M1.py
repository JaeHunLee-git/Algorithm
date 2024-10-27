from itertools import permutations

n, m = map(int, input().split())
nums = [i for i in range(1, n + 1)]

p = list(permutations(nums, m))

for i in p:
    print(" ".join(map(str, i)))

