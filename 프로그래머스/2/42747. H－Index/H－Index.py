def solution(citations):
    citations.sort()
    
    answer = 0
    
    for h in citations:
        cnt = 0
        
        for citation in citations:
            if citation >= h:
                cnt += 1
        
        if cnt >= h:
            answer = h
    
    for h in range(answer, len(citations) + 1):
        cnt = 0
        
        for citation in citations:
            if citation >= h:
                cnt += 1
        
        if cnt >= h:
            answer = h
    
    return answer