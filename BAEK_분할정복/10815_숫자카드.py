import sys

input = sys.stdin.readline

n = int(input().strip())
arr1 = list(map(int, input().split()))
m = int(input().strip())
arr2 = list(map(int, input().split()))

visit = [0] * 20000001

for i in arr1:
    visit[i - 10000001] = 1

for i in arr2:
    if visit[i - 10000001] == 1:
        print(1, end=" ")
    else:
        print(0, end=" ")
