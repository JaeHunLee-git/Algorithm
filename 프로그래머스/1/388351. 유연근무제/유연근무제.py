def solution(schedules, timelogs, startday):
    answer = 0
    for i in range(len(schedules)):

        chk = 0

        tmp = schedules[i]
        h = tmp // 100
        m = tmp % 100

        if m >= 50:
            m -= 50
            h += 1
        else:
            m += 10

        time = h * 100 + m

        tmp_day = startday

        for k in range(7): ## 타임로그
            if tmp_day == 7:
                tmp_day = 1
                continue

            if tmp_day == 6:
                tmp_day += 1
                continue

            if timelogs[i][k] > time:
                chk = 1
            tmp_day += 1
        if chk == 0:
            answer += 1

    return answer
