N = int(input())
cnt = 0
for i in range(N + 1):
    if i == 0:
        continue
    if i < 100:
        cnt += 1
    else:
        if i // 100 - i % 100 // 10 == i % 100 // 10 - i % 10:
            cnt += 1

print(cnt)

