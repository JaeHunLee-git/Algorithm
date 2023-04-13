import sys

a = sys.stdin.readline()
a = list(a)
a.sort(reverse=True)
for i in a:
    print(i, end="")
