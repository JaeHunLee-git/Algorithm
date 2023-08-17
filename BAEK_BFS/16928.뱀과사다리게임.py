# import sys
# input=sys.stdin.readline

# n,m=map(int,input().split())

# ladder=[]
# for _ in range(n):
#     ladder.append(list(map(int,input().split())))

# snake=[]
# for _ in range(m):
#     snake.append(list(map(int,input().split())))

# def dfs(a,b):  #a=현재 있는 칸, b=주사위 횟수
#     if a==100:
#         print(b)
#         exit()
#     elif a>100:
#         return

#     for j in range(len(ladder)):
#         if a==ladder[j][0]:
#             a=ladder[j][1]
    
#     for k in range(len(snake)):
#         if a==snake[k][0]:
#             a=snake[k][1]

#     for i in range(1,7):
#         a+=i
#         dfs(a,b+1)
#         a-=i

# dfs(1,0)
import sys
from collections import deque

input  = sys.stdin.readline

n,m = map(int,input().split())
graph = [i for i in range(101)]
for _ in range(n):
    a,b = map(int,input().split())
    graph[a] = b
for _ in range(m):
    a,b = map(int,input().split())
    graph[a] = b
visited  = [0 for _ in range(101)]


def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        x = q.popleft()
        for i in range(1,7):
            nx = x + i
            if nx > 100:
                continue
            kan = graph[nx]
            if visited[kan] == 0:
                q.append(kan)
                visited[kan] = visited[x] + 1
                if kan == 100:
                    return

bfs()
print(visited[100]-1)