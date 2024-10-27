import sys

input = sys.stdin.readline
n = int(input())
b = list(map(int,input().split()))
result = 100001

if n < 3:
    print(0)
    exit(0)


def check(i, j):
    cnt = abs(i) + abs(j)
    arr = []
    arr.append(b[1] + j)
    diff = arr[0] - b[0] - i

    for k in range(2, n):
        if b[k] == arr[k - 2] + diff:
            arr.append(b[k])
        elif b[k] - 1 == arr[k - 2] + diff:
            arr.append(b[k] - 1)
            cnt += 1
        elif b[k] + 1 == arr[k - 2] + diff:
            arr.append(b[k] + 1)
            cnt += 1
        else:
            return False
    return cnt


for i in range(-1, 2):
    for j in range(-1, 2):
        tmp = check(i, j)
        if tmp == False:
            continue
        else:
            result = min(result, tmp)

if result == 100001:
    print(-1)
else:
    print(result)
