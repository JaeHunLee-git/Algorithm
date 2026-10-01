def solution(brown, yellow):
    answer = []
    num_sum = brown + yellow
    yaksu = []

    for i in range(1, num_sum + 1):
        if num_sum % i == 0:
            yaksu.append([i, num_sum // i])

    for i in yaksu:
        n, m = i[0], i[1]
        if (2 * n) + (2 * (m - 2)) == brown:
            if n > m:
                answer.append([n,m])
            else:
                answer.append([m,n])
            return answer[0]
