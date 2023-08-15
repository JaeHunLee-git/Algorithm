## pypy통과, tmp에서 찾는 방식 확인하기
import sys

input=sys.stdin.readline

r,c=map(int,input().split())
board=[]
for _ in range(r):
    board.append(input().strip())

tmp=set()
tmp.add(board[0][0])
cnt=0
dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(ans,x1,y1):
    global cnt

    cnt = max(cnt,ans)

    for i in range(4):
        x=x1+dx[i]
        y=y1+dy[i]
        if 0<=x<r and 0<=y<c and not board[x][y]in tmp:
            tmp.add(board[x][y])
            dfs(ans+1,x,y)
            tmp.remove(board[x][y])

dfs(1,0,0)
print(cnt)