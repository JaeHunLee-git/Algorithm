T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = input().strip()
    cnt = n // 4
    num_set = set()  # 중복 제거를 위해 set 사용

    # 시계 방향 회전을 위해 전체 문자열 길이 만큼 반복
    for _ in range(cnt):
        # 네 면에서 추출 가능한 16진수 숫자 추가
        for i in range(4):
            hex_str = arr[i * cnt:(i + 1) * cnt]  # 고정된 4자리씩 추출
            num_set.add(int(hex_str, 16))  # 10진수로 변환하여 set에 저장

        # 시계 방향 회전
        arr = arr[-1] + arr[:-1]

    # 중복 제거 후 내림차순 정렬
    num_lst = sorted(num_set, reverse=True)
    print(f"#{test_case} {num_lst[k - 1]}")
