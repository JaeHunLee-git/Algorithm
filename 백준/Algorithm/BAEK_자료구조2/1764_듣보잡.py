import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr1 = set()
arr2 = set()

for _ in range(n):
    arr1.add(input().strip())

for _ in range(m):
    arr2.add(input().strip())

ans = arr1 & arr2
ans = sorted(list(ans))

print(len(ans))
for i in ans:
    print(i)
