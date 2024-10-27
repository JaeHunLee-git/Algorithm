# ## 시간초과
# import sys
# input=sys.stdin.readline
# from collections import deque
# import copy

# def bfs(tmp,i,j):
#     cnt=1
#     visited=[[False]*m for _ in range(n)]
#     visited[i][j]=True
#     q=deque()
#     q.append((i,j))
#     while q:
#         x,y=q.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False and tmp[nx][ny]==0:
#                 visited[nx][ny]=True
#                 q.append((nx,ny))
#                 cnt+=1
#     return cnt%10

# n,m=map(int,input().split())
# board=[]
# for _ in range(n):
#     board.append(list(map(int,input().strip())))

# ans_board=[[0]*m for _ in range(n)]
# dx=[0,0,1,-1]
# dy=[1,-1,0,0]

# for i in range(n):
#     for j in range(m):
#         if board[i][j]==1:
#             tmp_board=copy.deepcopy(board)
#             tmp_board[i][j]=0
#             ans_board[i][j]=bfs(tmp_board,i,j)
#         else:
#             continue
# for i in range(n):
#     print(*ans_board[i])
from collections import deque
input = __import__('sys').stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 1
    while q:
        i, j = q.popleft()
        zeros[i][j] = group
        for idx in range(4):
            ni, nj = i + dy[idx], j + dx[idx]
            if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] or graph[ni][nj] == 1:
                continue
            visited[ni][nj] = True
            q.append((ni, nj))
            cnt += 1
    return cnt

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
zeros = [[0] * m for _ in range(n)]
group = 1  # info의 인덱스
info = {}  # 0의 인접
info[0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            w = bfs((i, j))
            info[group] = w
            group += 1

for i in range(n):
    for j in range(m):
        addList = set()
        if graph[i][j]:
            for idx in range(4):
                ni, nj = i + dy[idx], j + dx[idx]
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                addList.add(zeros[ni][nj])
            for add in addList:
                graph[i][j] += info[add]
                graph[i][j] %= 10

for g in graph:
    print("".join(map(str, g)))