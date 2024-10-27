import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, max(arr)

while left <= right:
    mid = (left + right) // 2
    tmp = 0
    for i in range(n):
        if arr[i] > mid:
            tmp += arr[i] - mid
    # print(tmp)
    if tmp >= m:
        left = mid + 1
        # print(f"left={left}")
    else:
        right = mid - 1
        # print(f"right={right}")
print(right)
