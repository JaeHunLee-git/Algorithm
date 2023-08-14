import sys

input=sys.stdin.readline
board=[]
blank=[]

for _ in range(9):
    board.append(list(map(int,input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j]==0:
            blank.append((i,j))

def check_row(x,a):
    for i in range(9):
        if a==board[x][i]:
            return False
    return True

def check_col(y,a):
    for i in range(9):
        if a==board[i][y]:
            return False
    return True

def check_Rect(x,y,a):
    nx = x // 3*3
    ny = y // 3*3
    for i in range(3):
        for j in range(3):
            if a == board[nx+i][ny+j]:
                return False
    return True

def dfs(cnt):
    if cnt==len(blank):
        for i in range(9):
            print(*board[i])  # 리스트를 띄어쓰기 단위로 출력
        exit(0)  #exit으로 안하고 return으로 하면 모든 정답을 출력

    for i in range(1,10):
        x=blank[cnt][0]
        y=blank[cnt][1]

        if check_row(x,i) and check_col(y,i) and check_Rect(x,y,i):
            board[x][y]=i
            dfs(cnt+1)
            board[x][y]=0

dfs(0)