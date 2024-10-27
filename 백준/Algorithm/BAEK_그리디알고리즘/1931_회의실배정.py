import sys

input = sys.stdin.readline

n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int, input().split())))

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

end = 0
ans = 0

for i, j in time:
    if i >= end:
        ans += 1
        end = j

print(ans)
