total = int(input())
a = int(input())
i = 0
amount = 0
while i < a:
    b, c = map(int, input().split())
    amount += b * c
    i += 1
if amount == total:
    print("Yes")
else:
    print("No")
