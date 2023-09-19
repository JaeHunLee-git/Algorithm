n, m = map(int, input().split())
times = list(map(int, input().split()))

start, end = 0, 2_000_000_000_000_000_000  # N의 최댓값 x M의 최댓값
total_time = 0  # n명까지 놀이기구를 모두 타는데 걸리는 시간

while start <= end:  # total_time을 이진탐색으로 구해준다.
    mid = (start + end) // 2
    is_possible = False
    cnt = m
    for time in times:
        cnt += mid // time
        if cnt >= n:
            is_possible = True
    if is_possible:  # 현재 mid값(tmp_total_time) 안에 n보다 많은 사람이 탈수 있으면
        total_time = mid
        end = mid - 1
    else:  # 현재 mid 값 안에 n이 충분히 탈 수 없으면
        start = mid + 1

tmp_person = m  # 현재 놀이기구를 탄사람의 수, 0초에 m명이 탈수있으므로 m값으로 초기화
for time in times:
    tmp_person += (total_time - 1) // time  # total_time의 1초 전 몇명까지 탈 수 있는지?

for index, time in enumerate(times, 1):
    if total_time % time == 0:  # total_time일 때, 기구가 비어있으면 현재사람 += 1
        tmp_person += 1
    if tmp_person == n:  # 현재사람(tmp_person)이 마지막 n번째이면 print
        print(index)
        break
