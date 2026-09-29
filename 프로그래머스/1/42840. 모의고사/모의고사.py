def solution(answers):
    answer = []
    answer_chk = []
    
    for i in range(3):
        tmp = 0
        if i == 0:
            answer_tmp = [1,2,3,4,5] * 2000
        elif i == 1:
            answer_tmp = [2,1,2,3,2,4,2,5] * 1250
        else:
            answer_tmp = [3,3,1,1,2,2,4,4,5,5] * 1000
        
        for k in range(len(answers)):
            if answer_tmp[k] == answers[k]:
                tmp += 1
        
        answer_chk.append(tmp)
    max_answer = max(answer_chk)
    
    for i in range(0,3):
        if max_answer == answer_chk[i]:
            answer.append(i+1)
    
    return answer