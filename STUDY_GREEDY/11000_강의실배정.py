import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort()
end = [arr[0][1]]
for i in range(1, n):
    if end[0] <= arr[i][0]:
        heapq.heappop(end)
    heapq.heappush(end, arr[i][1])
print(len(end))
