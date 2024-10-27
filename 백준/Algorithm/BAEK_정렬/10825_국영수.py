import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().strip().split()))

for i in range(n):
    for j in range(1, 4):
        arr[i][j] = int(arr[i][j])

arr.sort(key=lambda x: x[0])
arr.sort(key=lambda x: x[3], reverse=True)
arr.sort(key=lambda x: x[2])
arr.sort(key=lambda x: x[1], reverse=True)

for i in range(n):
    print(arr[i][0])
