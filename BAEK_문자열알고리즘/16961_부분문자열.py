import sys

input = sys.stdin.readline

s = input().strip()
p = input().strip()
tmp = False

if p in s:
    print(1)
else:
    print(0)
