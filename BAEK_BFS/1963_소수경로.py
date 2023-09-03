from collections import deque
import sys

input = sys.stdin.readline


# 소수판별함수
def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**1 / 2) + 1):
        if x % i == 0:
            return False
    return True


# BFS
def bfs(a, b):
    q = deque()
    q.append((a, 0))
    while q:
        password, count = q.popleft()
        if password == b:
            print(count)
            return
        for i in range(4):
            for j in range(10):
                new_pass = list(str(password))
                new_pass[i] = str(j)
                new_pass = int("".join(new_pass))
                if 1000 <= new_pass and not visited[new_pass] and sosu[new_pass]:
                    visited[new_pass] = 1
                    q.append((new_pass, count + 1))


# 소수판별테이블
sosu = [False]
for i in range(1, 10000):
    sosu.append(isPrime(i))

# 테스트케이스
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [0] * 10000
    visited[a] = 1
    bfs(a, b)
