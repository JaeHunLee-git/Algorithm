## 새로운 값을 넣을 때마다 정렬을 해서 넣어줘야 함
## 최대힙, 최소힙 개념 파악하기

import sys
import heapq

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()

ans = 0
while len(arr) > 1:
    x, y = heapq.heappop(arr), heapq.heappop(arr)
    tmp = x + y
    ans += tmp
    heapq.heappush(arr, tmp)

print(ans)