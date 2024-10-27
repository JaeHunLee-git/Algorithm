import sys

input = sys.stdin.readline
n = int(input())
k = int(input())
arr = sorted(list(map(int, input().split())))

if n == 1:
    print(0)
    exit(0)
elif k == 1:
    print(max(arr) - min(arr))
    exit(0)
else:
    distance = []
    for i in range(n - 1):
        distance.append(arr[i + 1] - arr[i])
    distance.sort()

    for i in range(k - 1):
        distance.pop()

    print(sum(distance))
