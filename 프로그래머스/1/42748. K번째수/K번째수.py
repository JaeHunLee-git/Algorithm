def solution(array, commands):
    answer = []
    
    for i in commands:
        a,b,c = i[0]-1,i[1],i[2]-1
        tmp = array[a:b]
        tmp.sort()
        answer.append(tmp[c])
    
    return answer