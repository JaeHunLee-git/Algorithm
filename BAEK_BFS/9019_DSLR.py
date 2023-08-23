import sys
input=sys.stdin.readline
from collections import deque

def d(x):
    return (int(x) * 2) % 10000

def s(x):
    return (int(x)-1) % 10000

def l(x):
    tmp=x//1000
    return x%1000*10+tmp

def r(x):
    tmp=x%10
    return x//10+1000*tmp

dx=['D','S','L','R']

def bfs(a,b,visited):
    q=deque([[a,""]])
    visited[a]=1
    while q:
        num, case=q.popleft()
        if num==b:
            print(case)
            break
        for i in range(4):
            if i==0:
                n_case=d(num)
            elif i==1:
                n_case=s(num)
            elif i==2:
                n_case=l(num)
            elif i==3:
                n_case=r(num)
            if visited[n_case]==0:
                q.append((n_case,case+dx[i]))
                visited[n_case]=1

t=int(input().strip())
for _ in range(t):
    visited=[0 for _ in range(10000)]
    a,b=map(int,input().split())
    bfs(a,b,visited)
