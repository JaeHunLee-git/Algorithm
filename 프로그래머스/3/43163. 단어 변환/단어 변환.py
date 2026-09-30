from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = set()
    visited.add(begin)
    
    q = deque()
    q.append((begin, 0))
    
    while q:
        word, count = q.popleft()
        
        if word == target:
            return count
        
        for nxt_word in words:
            diff = 0
            if nxt_word not in visited:
                for i in range(len(nxt_word)):
                    if word[i] != nxt_word[i]:
                        diff += 1
            
            if diff == 1:
                count += 1
                visited.add(nxt_word)
                q.append((nxt_word, count))
                
    return 0