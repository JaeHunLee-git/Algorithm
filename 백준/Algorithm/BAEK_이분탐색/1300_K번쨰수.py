## ex) 20보다 작거나 같은 수는 20을 행으로 나눈 것
import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2
    tmp = 0
    for i in range(1, n + 1):
        tmp += min(mid // i, n)  # 행으로 나눈 것과, 최대 n 중 최소
    if tmp >= k:
        end = mid - 1
    else:
        start = mid + 1
print(start)
