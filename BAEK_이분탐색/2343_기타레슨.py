# 최소합을 구하는 것이기 때문에 start가 정답
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = max(arr), sum(arr)

while start <= end:
    mid = (start + end) // 2
    cnt = 1
    tmp = 0
    for i in range(n):
        tmp += arr[i]
        if tmp > mid:
            tmp = arr[i]
            cnt += 1
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1
print(start)
