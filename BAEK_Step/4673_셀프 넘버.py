nums = list(range(1, 10001))
nums_del = []
for i in nums:
    for k in str(i):
        i += int(k)
    if i <= 10000:
        nums_del.append(i)
for a in set(nums_del):
    nums.remove(a)

for q in nums:
    print(q)
