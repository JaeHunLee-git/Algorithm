from collections import deque
import sys
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append(start)
    ans = 1
    time = True
    while q:
        for _ in range(len(q)):
            i, j, w = q.popleft()
            
            if i == n - 1 and j == m - 1:
                print(ans)
                return
            
            for dy, dx in dir:
                ni, nj = i + dy, j + dx
                if ni < 0 or ni >= n or nj < 0 or nj >= m or visited[ni][nj] <= w:
                    continue
                #벽이 아닌 경우 낮이든 밤이든 이동 가능
                if graph[ni][nj] == '0':
                        q.append((ni, nj, w))
                        visited[ni][nj] = w
                #벽인 경우
                elif w < k:
                    if not time: #밤 인 경우
                        q.append((i, j, w))
                    else:
                        visited[ni][nj] = w
                        q.append((ni, nj, w + 1))
        ans += 1
        time = not time
    print(-1)
    return

n, m, k = map(int, input().split())
graph = [input().strip() for _ in range(n)]
visited = [[k + 1 for _ in range(m)] for _ in range(n)]
visited[0][0] = 0

dir = ((1, 0), (-1, 0), (0, 1), (0, -1))

bfs((0,0,0))