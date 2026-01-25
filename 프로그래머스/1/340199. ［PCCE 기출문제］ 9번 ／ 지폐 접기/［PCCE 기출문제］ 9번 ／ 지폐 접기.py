def solution(wallet, bill):
    answer = 0

    w_min, w_max = min(wallet), max(wallet)
    b_min, b_max = min(bill), max(bill)

    while w_max < b_max or w_min < b_min:
        b_max //= 2
        answer += 1
        
        if b_max < b_min:
            tmp = b_max
            b_max = b_min
            b_min = tmp
        

    return answer