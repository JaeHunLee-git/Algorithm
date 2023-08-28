import sys
input=sys.stdin.readline
from collections import deque

def bfs():
    global a,b,c,sum,visited
    q=deque()
    q.append((a,b))
    visited[a][b]=True

    while q:
        x,y=q.popleft()
        z=sum-x-y
        if x==y==z:
            print(1)
            return
        
        for a,b in (x,y), (y,z), (x,z):
            if a<b:
                b-=a
                a+=a
            elif a>b:
                a-=b
                b+=b
            else:
                continue
            c=sum-a-b
            x=min(a,b,c)
            y=max(a,b,c)
            if not visited[x][y]:
                q.append((x,y))
                visited[x][y]=True
    print(0)

a,b,c=map(int,input().split())
sum=a+b+c
visited=[[False]*(sum+1) for _ in range(sum+1)]
if sum%3 != 0:
    print(0)
else:
    bfs()