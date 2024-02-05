import sys

input = sys.stdin.readline

name = input().strip()
dic = dict()

for i in name:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

check = 0
for i in dic:
    if dic[i] % 2 != 0:
        check += 1
dic = dict(sorted(dic.items(), key=lambda a: a[0]))
front = ""
mid = ""
end = ""
if check < 2:
    for i in dic:
        if dic[i] % 2 != 0:
            mid = i
        for k in range(dic[i] // 2):
            front += i
    for j in reversed(front):
        end += j
    if mid:
        print(front + mid + end)
    else:
        print(front + end)
else:
    print("I'm Sorry Hansoo")
