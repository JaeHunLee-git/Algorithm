T = int(input())
rows = 100
cols = 100
cnt = 0
arr = [[0 for j in range(cols)] for i in range(rows)]

for _ in range(T):
    a, b = map(int, input().split())
    for i in range(a, a + 10):
        for k in range(b, b + 10):
            arr[i][k] = 1
for i in range(100):
    for k in range(100):
        if arr[i][k] == 1:
            cnt += 1

print(cnt)

