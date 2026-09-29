def solution(sizes):
    answer = 0
    
    ga=0
    se=0
    
    for i in range(len(sizes)):
        sizes[i].sort()
    
    for k in sizes:
        if k[0] > ga:
            ga = k[0]
        if k[1] > se:
            se = k[1]
    
    answer = ga*se
    
    return answer