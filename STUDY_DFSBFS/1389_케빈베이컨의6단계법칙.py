import sys

input = sys.stdin.readline

n, m = map(int, input().split())
user = [[] for _ in range(n + 1)]
relation = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)
