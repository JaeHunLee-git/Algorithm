# import sys

# input = sys.stdin.readline

# n = input().strip()

# num = []
# tmp = 0
# for i in range(len(n)):
#     if i == "+" or i == "-":
#         num.append(int("".join(n[j] for j in range(tmp, i))))
#         tmp = i + 1
# num.append(int("".join(n[j] for j in range(tmp, len(n)))))
# # num[]에 숫자만 들어가있음

# func = []
# func1 = []

# for i in range(len(n)):
#     if n[i] == "+":
#         func.append(i)
#         func1.append("+")
#     elif n[i] == "-":
#         func.append(i)
#         func1.append("-")
# # func[]에 기호를
# print(func, num)
# ans = num[0]
# i = 0
# while i < len(func):
#     if func1[i] == "+":
#         ans += num[i + 1]
#         i += 1
#     elif func1[i] == "-":
#         tmp = num[i + 1]
#         i += 1
#         while func1[i] == "+":
#             tmp += num[i + 1]
#             i += 1
#             if i == len(func1):
#                 break
#         ans -= tmp
# print(ans)
import sys

input = sys.stdin.readline

n = input().strip()

func = []
num = []
tmp = ""

for i in range(len(n)):
    if n[i] == "+" or n[i] == "-":
        func.append(n[i])
        num.append(int(tmp))
        tmp = ""
    else:
        tmp += n[i]

num.append(int(tmp))

ans = num[0]
i = 0
while i < len(func):
    if func[i] == "+":
        ans += num[i + 1]
        i += 1
    elif func[i] == "-":
        tmp = num[i + 1]
        i += 1
        while i < len(func) and func[i] == "+":
            tmp += num[i + 1]
            i += 1
        ans -= tmp

print(ans)