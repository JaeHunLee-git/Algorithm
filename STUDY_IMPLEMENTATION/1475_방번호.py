## 인덱스로 저장
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] * 10

while n > 0:
    tmp = n % 10
    arr[tmp] += 1
    n //= 10

tmp = arr[6] + arr[9]
if tmp % 2 == 0:
    ans = (arr[9] + arr[6]) // 2
else:
    ans = ((arr[9] + arr[6]) // 2) + 1
arr[9], arr[6] = 0, 0
if max(arr) > ans:
    ans = max(arr)
print(ans)
