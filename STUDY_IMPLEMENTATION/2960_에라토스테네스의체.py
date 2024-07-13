import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [_ for _ in range(2, n + 1)]


def sosu(num):
    check = True
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            check = False
            break
    if check:
        return True
    else:
        return False


arr_sosu = []
for num in range(2, n + 1):
    if sosu(num):
        arr_sosu.append(num)

ans = 0
for _ in range(k):
    tmp = arr_sosu.pop(0)
    while tmp < max(arr):
        if tmp in arr:
            arr.remove(tmp)
            tmp += tmp
