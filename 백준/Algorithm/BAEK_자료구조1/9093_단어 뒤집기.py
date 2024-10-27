import sys

T = int(input())
for _ in range(T):
    a = list(input().split())
    for i in a:
        x = len(i) - 1
        for k in range(len(i)):
            print(i[x], end="")
            x -= 1
        print("", end=" ")
    print()
