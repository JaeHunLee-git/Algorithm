import math

n = int(input())
arr = sorted(list(map(int, input().split())))
print(arr[math.floor(n / 2)])
