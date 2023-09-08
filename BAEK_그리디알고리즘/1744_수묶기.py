# import sys

# input = sys.stdin.readline
# n = int(input().strip())

# arr = []
# for _ in range(n):
#     arr.append(int(input().strip()))
# arr.sort()

# ans = 0
# i = n - 1

# while i > -1:
#     if i == 0:
#         ans += arr[i]
#         break
#     elif arr[i - 1] < 0 and arr[i] > 0:  # -,+
#         ans += arr[i] * arr[i - 1]
#         i -= 2
#     elif arr[i - 1] < 0 and arr[i] == 0:  # -,0
#         ans += arr[i] * arr[i - 1]
#         i -= 2
#     elif arr[i] < 0 and arr[i - 1] < 0:  # -,-
#         ans += arr[i] * arr[i - 1]
#         i -= 2
#     elif arr[i - 1] == 0 and arr[i] > 0:  # 0,+
#         ans += arr[i]
#         i -= 1
#     elif arr[i] > 0 and arr[i - 1] > 0:  # +,+
#         ans += arr[i] * arr[i - 1]
#         i -= 2
#     elif arr[i] == 0 and arr[i - 1] == 0:  # 0,0
#         ans += arr[i]
#         i -= 1
#     else:
#         ans += arr[i]
#         i -= 1
# print(ans)
# n : 데이터의 크기
n = int(input())

# plus : 양수 데이터 리스트, minus : 음수 데이터 리스트
plus = []
minus = []

result = 0
for i in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

# 정렬
plus.sort(reverse=True)
minus.sort()  # ex) -3 -2 -1

# 양수 묶기
for i in range(0, len(plus), 2):
    if i + 1 >= len(plus):
        result += plus[i]
    else:
        result += plus[i] * plus[i + 1]

# 음수 묶기
for i in range(0, len(minus), 2):
    if i + 1 >= len(minus):
        result += minus[i]
    else:
        result += minus[i] * minus[i + 1]

print(result)
