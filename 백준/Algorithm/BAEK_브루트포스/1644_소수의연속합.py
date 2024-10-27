import sys

input = sys.stdin.readline
n = int(input())


def sosu(x):
    for i in range(3, int(x ** (0.5)) + 1, 2):
        if x % i == 0:
            return False
    return True


arr = [2]

for i in range(3, n + 1, 2):
    if sosu(i):
        arr.append(i)

ans = 0
left, right = 0, 0
sum = 0

while right <= len(arr):
    if sum < n:
        if right == len(arr):
            break
        sum += arr[right]
        right += 1
    else:
        sum -= arr[left]
        left += 1
    if sum == n:
        ans += 1
print(ans)
