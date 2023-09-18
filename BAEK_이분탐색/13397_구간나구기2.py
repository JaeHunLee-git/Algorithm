import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))


def check(mid):
    maxi, mini = arr[0], arr[0]
    cnt = 1
    for i in range(1, n):
        maxi = max(maxi, arr[i])
        mini = min(mini, arr[i])
        if maxi - mini > mid:
            cnt += 1
            maxi = arr[i]
            mini = arr[i]
    return cnt


start, end = 0, max(arr)
while start <= end:
    mid = (start + end) // 2

    if check(mid) > m:
        start = mid + 1
    else:
        end = mid - 1
print(start)
