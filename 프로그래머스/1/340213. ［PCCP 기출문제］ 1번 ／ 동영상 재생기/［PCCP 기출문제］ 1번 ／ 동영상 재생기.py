def solution(video_len, pos, op_start, op_end, commands):
    answer = ""

    # 🔹 시간 문자열 → 초 단위
    video_len_time = int(video_len[0:2]) * 60 + int(video_len[3:5])
    op_start_time = int(op_start[0:2]) * 60 + int(op_start[3:5])
    op_end_time = int(op_end[0:2]) * 60 + int(op_end[3:5])

    pos_m, pos_s = int(pos[0:2]), int(pos[3:5])

    # 🔹 시작 위치 오프닝 체크
    if op_start_time <= pos_m * 60 + pos_s <= op_end_time:
        pos_m, pos_s = int(op_end[0:2]), int(op_end[3:5])

    for i in commands:
        if i == "next":
            # 🔹 영상 끝 초과 방어
            if pos_m * 60 + pos_s + 10 >= video_len_time:
                pos_m = video_len_time // 60
                pos_s = video_len_time % 60
            else:
                if pos_s >= 50:
                    pos_s -= 50
                    pos_m += 1
                else:
                    pos_s += 10
        else:  # prev
            if pos_m * 60 + pos_s < 10:
                pos_m = 0
                pos_s = 0
            else:
                if pos_s < 10:
                    pos_m -= 1
                    pos_s = 60 - (10 - pos_s)
                else:
                    pos_s -= 10

        # 🔹 명령 수행 후 오프닝 체크
        if op_start_time <= pos_m * 60 + pos_s <= op_end_time:
            pos_m, pos_s = int(op_end[0:2]), int(op_end[3:5])

    # 🔹 결과 포맷
    if pos_m < 10:
        pos_m = "0" + str(pos_m)
    if pos_s < 10:
        pos_s = "0" + str(pos_s)

    answer = str(pos_m) + ":" + str(pos_s)
    return answer
