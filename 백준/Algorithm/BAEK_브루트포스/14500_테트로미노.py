import sys
input = sys.stdin.readline

move=[(0,1),(0,-1),(1,0),(-1,0)]

N,M=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*M for _ in range(N)]

max_value=0

def dfs(i, j, dsum, count):
    global max_value

    if count == 4:
        max_value = max(dsum,max_value)
        return
    
    for n in range(4):
        ni = i + move[n][0]
        nj = j + move[n][1]
        if 0<=ni<N and 0 <=nj<M and not visited[ni][nj]:
            visited[ni][nj]=True
            dfs(ni,nj,dsum + board[ni][nj],count+1)
            visited[ni][nj]=False

def exce(i,j):
    global max_value
    for n in range(4):
        tmp=board[i][j]
        for k in range(3):
            t=(n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0<=ni<N and 0<=nj<M):
                tmp=0
                break
            tmp += board[ni][nj]
        max_value=max(tmp,max_value)

for i in range(N):
    for j in range(M):
        visited[i][j]=True
        dfs(i,j,board[i][j],1)
        visited[i][j]=False

        exce(i,j)

print(max_value)