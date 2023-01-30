import sys

n = int(input())
lst = []
for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push_front":
        lst.insert(0, a[1])
    elif a[0] == "push_back":
        lst.append(a[1])
    elif a[0] == "pop_front":
        if len(lst) == 0:
            print(-1)
            continue
        else:
            print(lst[0])
            del lst[0]
    elif a[0] == "pop_back":
        if len(lst) == 0:
            print(-1)
            continue
        else:
            print(lst[-1])
            lst.pop()
    elif a[0] == "size":
        print(len(lst))
    elif a[0] == "empty":
        if len(lst) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(lst) == 0:
            print(-1)
            continue
        else:
            print(lst[0])
    else:
        if len(lst) == 0:
            print(-1)
            continue
        else:
            print(lst[-1])
