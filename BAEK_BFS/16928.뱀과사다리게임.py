# import sys
# sys.setrecursionlimit(10**6)

# n, m = map(int, sys.stdin.readline().split(' '))

# graph = [[] for _ in range(100+1)]
# short_cut = []   # 뱀, 사다리가 놓여진 시작 칸
# for _ in range(n+m):
#     x, y = map(int, sys.stdin.readline().split(' '))
#     graph[x].append(y)
#     short_cut.append(x)

# for i in range(1, 100+1):
# 	# 뱀, 사다리가 놓여진 시작 칸일 경우 +1 ~ +6으로 이동할 수 없음.
#     if i in short_cut:
#         continue
#     for j in range(1, 6+1):
#         if i+j <= 100:
#             graph[i].append(i+j)

# #print(graph)

# # 인덱스는 칸 번호를 나타내고, 각 칸에 도달할 수 있는 최소 경우의 수가 들어감.
# cost = [0] * (100+1)
# #print(cost)


# def dfs(x, cnt):
#     cost[x] = cnt
#     # 뱀, 사다리를 만났을 경우, 바로 이동하기 때문에 이동 횟수가 추가되지 않음.
#     if x in short_cut:
#         cnt -= 1
#     for i in graph[x]:
#         if not cost[i] or cost[i] > cnt + 1:
#             dfs(i, cnt+1)


# dfs(1, 0)
# print(cost[100])
import sys
from collections import deque

input  = sys.stdin.readline

n,m = map(int,input().split())
graph = [i for i in range(101)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    graph[a] = b
visited  = [0 for _ in range(101)]


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in range(1,7):
            nx = x + i
            if nx > 100:
                continue
            kan = graph[nx]
            if visited[kan] == 0:
                q.append(kan)
                visited[kan] = visited[x] + 1
                if kan == 100:
                    return

bfs()
print(visited[100]-1)