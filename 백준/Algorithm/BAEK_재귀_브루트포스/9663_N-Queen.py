# import sys
# from itertools import permutations

# input=sys.stdin.readline
# n=int(input())
# num=[i for i in range(0,n)]
# tmp = list(permutations(num,n))
# cnt=0

# def dfs(x):
#     global cnt
#     board=[[0]*n for _ in range(n)]
#     put=0
#     for i in x:
#         board[put][i]=1
#         put+=1

#     for k in range(n-1):
#         input=0
#         cnt1=0
#         if abs(board[input][x[k]]-board[input+1][x[k+1]]) == abs(x[k]-x[k+1]):
#             cnt1+=1
#         input+=1
#     if cnt1==0:
#         cnt+=1

# for x in tmp:
#     dfs(x)

# print(cnt)

n=int(input())

cnt=0
row=[0]*n

def is_promising(x):
    for i in range(x):
        if row[x]==row[i] or abs(row[x]-row[i])==abs(x-i):
            return False
    return True

def n_queens(x):
    global cnt
    if x==n:
        cnt+=1
        return
    else:
        for i in range(n):
            row[x]=i
            if is_promising(x):
                n_queens(x+1)

n_queens(0)
print(cnt)