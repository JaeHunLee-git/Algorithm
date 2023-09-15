# import sys

# input = sys.stdin.readline

# k, n = map(int, input().split())

# arr = []
# for _ in range(k):
#     arr.append(int(input().strip()))

# ans = 1
# cnt = 10001
# while cnt >= n:
#     cnt = 0
#     for i in range(k):
#         cnt += arr[i] // ans
#     ans += 1

# print(ans - 2)
import sys

input = sys.stdin.readline

k, n = map(int, input().split())

arr = []
for _ in range(k):
    arr.append(int(input().strip()))

left, right = 1, max(arr)  # 이진 탐색을 위한 범위 설정

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in range(k):
        cnt += arr[i] // mid

    if cnt >= n:  # 랜선을 더 길게 자를 수 있음
        left = mid + 1
        # print(f"left={left}")
    else:  # 랜선을 더 짧게 자야 함
        right = mid - 1
        # print(f"right={right}")

print(right)  # 최대 랜선의 길이 출력
