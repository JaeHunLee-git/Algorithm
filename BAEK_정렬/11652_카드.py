# import sys

# input = sys.stdin.readline
# n = int(input())
# arr = []

# for i in range(n):
#     arr.append(int(input()))

# arr.sort()
# num = set(arr)
# count = []
# cnt = 0
# check = arr[0]
# for i in arr:
#     if i == check:
#         cnt += 1
#     else:
#         count.append(cnt)
#         cnt = 1
#         check = i
# count.append(cnt)

# max_num = max(count)
# max_index = count.index(max_num)
# num = list(num)
# print(num[max_index])
# 11652 카드
import sys

input = sys.stdin.readline

n = int(input())
card_dic = {}

for i in range(n):
    card = int(input())
    if card in card_dic:
        card_dic[card] += 1
    else:
        card_dic[card] = 1

result = sorted(card_dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
