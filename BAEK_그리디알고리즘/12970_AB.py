# import sys

# input = sys.stdin.readline
# import math

# n, k = map(int, input().split())

# c, f = math.ceil(n / 2), math.floor(n / 2)

# ans = ""
# if k > c * f:
#     print(-1)
#     exit(0)
# elif k == 0:
#     for _ in range(n - 1):
#         ans += "B"
#     ans += "A"
#     print(ans)
#     exit(0)
# elif k == c * f:
#     for _ in range(c):
#         ans += "A"
#     for _ in range(f):
#         ans += "B"
#     print(ans)
#     exit(0)

# tmp = k  # 12
# total = n - 1  # 9


# # 4,5  #123456789
# while tmp > 0:
#     while tmp >= total and tmp != 0:
#         ans += "A"
#         tmp -= total  # 3
#         total -= 1  # 8
#         tmp += 1  # 4
#     while total > tmp and tmp != 0:  # ABBB, total=4,tmp=4
#         ans += "B"
#         total -= 1
# print(ans)
def solution():
    n, k = map(int, input().split())

    a = 0
    b = n
    while a * b < k and b > 0:  # A의 개수를 구함 a=2,b=8
        a += 1
        b -= 1

    if k == 0:
        return "B" * n
    elif b == 0:
        return -1

    remain = k - (a - 1) * b

    return "A" * (a - 1) + "B" * (b - remain) + "A" + "B" * remain


print(solution())
