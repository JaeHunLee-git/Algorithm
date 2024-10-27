# 시간초과
# 앞으로 간 횟수로 버블소트의 횟수를 구할 수 있음
# import sys

# input = sys.stdin.readline
# n = int(input())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))

# changed = False
# for i in range(n):
#     changed = False
#     for j in range(n - i - 1):
#         if arr[j] > arr[j + 1]:
#             changed = True
#             tmp = arr[j]
#             arr[j] = arr[j + 1]
#             arr[j + 1] = tmp
#     if changed == False:
#         print(i + 1)
#         break

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append((int(input()), i))
sorted_arr = sorted(arr)
answer = []

for i in range(n):
    answer.append(sorted_arr[i][1] - arr[i][1])

print(max(answer) + 1)
