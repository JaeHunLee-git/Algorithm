# import sys
# from collections import deque

# input=sys.stdin.readline

# n=int(input().strip())
# r1,c1,r2,c2=map(int,input().split())

# dx=[-2,-2,0,0,2,2]
# dy=[-1,1,-2,2,-1,+1]

# ans=100

# def dfs(x,y,cnt):
#     global ans

#     if x==r2 and y==c2:
#         ans=min(ans,cnt)
#     for i in range(6):
#         nx=x+dx[i]
#         ny=y+dy[i]
#         if 0<=nx<n and 0<=ny<n:
#             dfs(nx,ny,cnt+1)
#         nx-=dx[i]
#         ny-=dy[i]

# dfs(r1,c1,0)
# print(ans)

from collections import deque

def bfs(y, x):
    q = deque()
    q.append((y, x))
    graph[y][x] = 0
    while q:
        y, x = q.popleft()
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if 0 <= ny < n and 0 <= nx < n and graph[ny][nx] == -1:
                q.append((ny, nx))
                graph[ny][nx] = graph[y][x]+1

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
graph = [[-1] * n for _ in range(n)]
d = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
bfs(r1, c1)

print(graph[r2][c2])