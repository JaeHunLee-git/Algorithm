from collections import deque

def solution(priorities, location):
    answer = 0
    
    q = deque()
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while q:
        priority, index = q.popleft()
        chk = False ##더 높은 우선순위가 없으면
        
        for p in q:
            if priority < p[0]:
                chk = True
                break
        
        if chk:
            q.append((priority, index))
            continue
        
        answer += 1
        
        if index == location:
            return answer
        
        