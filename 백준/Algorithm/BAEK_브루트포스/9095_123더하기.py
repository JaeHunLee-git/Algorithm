# 앞에꺼 3개를 더하는 공식
import sys

input = sys.stdin.readline
t = int(input())
s = [1, 2, 4]
for i in range(3, 11):
    s.append(s[i - 3] + s[i - 2] + s[i - 1])
for _ in range(t):
    n = int(input())
    print(s[n - 1])
