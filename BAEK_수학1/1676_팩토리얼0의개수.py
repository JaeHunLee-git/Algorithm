a = int(input())
sum = 1
for i in range(1, a + 1):
    sum *= i

cnt = 0
while True:
    tmp = sum % 10
    sum //= 10
    if tmp != 0:
        break
    cnt += 1

print(cnt)
