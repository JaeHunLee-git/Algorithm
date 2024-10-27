import sys


def push(n):
    global arr
    arr.append(n)


def pop():
    global arr
    if len(arr) == 0:
        print(-1)
    else:
        a = arr[len(arr) - 1]
        print(a)
        arr.pop()


def size():
    global arr
    print(len(arr))


def empty():
    global arr
    if len(arr) == 0:
        print(1)
    else:
        print(0)


def top():
    global arr
    if len(arr) == 0:
        print(-1)
    else:
        a = arr[len(arr) - 1]
        print(a)


n = int(sys.stdin.readline())
arr = []
for _ in range(n):
    a = sys.stdin.readline().split()
    if a[0] == "push":
        push(a[1])
    elif a[0] == "pop":
        pop()
    elif a[0] == "size":
        size()
    elif a[0] == "empty":
        empty()
    elif a[0] == "top":
        top()
    else:
        break
