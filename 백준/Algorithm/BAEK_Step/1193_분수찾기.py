x = int(input())
i = 1
buf = x
while buf > i:
    buf -= i
    i += 1
sum = 0
for k in range(i):
    sum += k
b = x - sum
a = i - b + 1

if i % 2 != 0:
    print(f"{a}/{b}")
else:
    print(f"{b}/{a}")
