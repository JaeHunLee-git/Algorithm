## 배열의 모든 수와 그 수의 개수를 딕셔너리로 저장
## 배열안의 최대 최소 범위 내의 모든 경우의 수 계산하여 가장 낮은 것 출력
import sys

input = sys.stdin.readline
n, m, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
duplicate = dict()

for select_height in range(n):
    for j in range(m):
        if arr[select_height][j] not in duplicate:
            duplicate[arr[select_height][j]] = 1
        else:
            duplicate[arr[select_height][j]] += 1
duplicate = dict(sorted(duplicate.items(), key=lambda a: a[0], reverse=True))
## 높이가 제일 높은 것부터 정렬해야 인벤토리에 블럭이 가장 많이 남음

max_height = max(duplicate)
min_height = min(duplicate)

ans_time = 1e9
ans_height = -1

for select_height in range(min_height, max_height + 1):
    check = True
    time = 0
    remain_block = b
    for k in duplicate:
        if select_height == k:
            continue
        elif select_height < k:
            tmp = k - select_height
            time += tmp * duplicate[k] * 2  ## 땅 제거
            remain_block += tmp * duplicate[k]  ## 목재가 생김
        elif select_height > k:
            tmp = select_height - k  ## 채워넣어야 할 땅 높임
            if remain_block >= (tmp * duplicate[k]):  ## 목재가 더 많을 경우
                time += duplicate[k] * tmp
                remain_block -= duplicate[k] * tmp
            else:
                check = False
    if check:
        if time <= ans_time:
            if select_height > ans_height:
                ans_time = time
                ans_height = select_height

print(ans_time, ans_height)
