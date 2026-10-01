def solution(phone_book):
    answer = True
    
    tmp = {}
    
    for i in phone_book:
        for k in range(1,len(i)+1):
            tmp[i[:k]] = tmp.get(i[:k],0)+1
            
    for j in phone_book:
        if tmp[j]>=2:
            answer=False
    
    return answer