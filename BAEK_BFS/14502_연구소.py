import sys
input=sys.stdin.readline
from collections import deque
import copy

def make_wall(cnt):  # dfs
    if cnt == 3:
        bfs()
        return
    for i in range(n):
        for k in range(m):
            if board[i][k] == 0:
                board[i][k] = 1
                make_wall(cnt+1)
                board[i][k] = 0

def bfs():
    q=deque()
    tmp_board=copy.deepcopy(board)
    for i in range(n):
        for j in range(m):
            if tmp_board[i][j]==2:
                q.append((i,j))

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if tmp_board[nx][ny]==0:
                    tmp_board[nx][ny]=2
                    q.append((nx,ny))
    global ans
    cnt=0
    for i in range(n):
        cnt+=tmp_board[i].count(0)
    ans=max(cnt,ans)

n,m=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

dx=[0,0,1,-1]
dy=[1,-1,0,0]

ans=0
make_wall(0)
print(ans)