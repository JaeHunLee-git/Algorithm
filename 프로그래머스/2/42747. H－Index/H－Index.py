def solution(citations):
    n = len(citations)
    
    for h in range(n, -1, -1):
        cnt = 0
        
        for citation in citations:
            if citation >= h:
                cnt += 1
        
        if cnt >= h:
            return h
    
    return 0