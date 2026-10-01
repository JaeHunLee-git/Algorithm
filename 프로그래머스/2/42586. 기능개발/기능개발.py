def solution(progresses, speeds):
    answer = []
    
    for i in range(len(progresses)):
        progresses[i] = 100 - progresses[i]
        
        if progresses[i] % speeds[i] == 0:
            progresses[i] = progresses[i] // speeds[i]
        else:
            progresses[i] = progresses[i] // speeds[i] + 1
            
    tmp = progresses[0]
    cnt = 0
    
    for i in progresses:
        if i > tmp:
            answer.append(cnt)
            cnt = 1
            tmp = i
        else:
            cnt += 1
    answer.append(cnt)
    
    return answer