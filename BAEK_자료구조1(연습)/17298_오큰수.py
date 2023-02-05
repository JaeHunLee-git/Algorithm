import sys

n = int(input())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * n
stack = []  # 원소 값이 아닌 원소의 인덱스 값

stack.append(0)
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        answer[stack.pop()] = A[i]
    stack.append(i)

print(*answer)
