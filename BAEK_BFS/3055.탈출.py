from collections import deque

r,c=map(int,input().split())
graph=[list(input()) for _ in range(r)]
visited=[[False]*c for _ in range(r)]
dx=[1,-1,0,0]
dy=[0,0,1,-1]

sx,sy=0,0
for i in range(r):
    for j in range(c):
        if graph[i][j]=="S":
            sx,sy=i,j
            visited[i][j]=True

def flood():
    water=[]
    for i in range(r):
        for j in range(c):
            if graph[i][j]=='*' and not visited[i][j]:
                water.append((i,j))
                visited[i][j]=True
    for x,y in water:
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]

            if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                if graph[nx][ny]=='.':
                    graph[nx][ny]='*'
def bfs(x,y):
    q=deque()
    q.append((x,y))
    visited[x][y]=True
    cnt=0
    
    while q:
        cnt+=1

        flood()

        for _ in range(len(q)):  # 이래야 1분에 cnt가 1칸씩 증가함
            x,y = q.popleft()

            for i in range(4):
                nx,ny=x+dx[i],y+dy[i]

                if 0<=nx<r and 0<=ny<c and not visited[nx][ny]:
                    if graph[nx][ny]=='.':
                        q.append((nx,ny))
                        visited[nx][ny]=True
                    elif graph[nx][ny]=='D':
                        return cnt
    return "KAKTUS"

print(bfs(sx,sy))