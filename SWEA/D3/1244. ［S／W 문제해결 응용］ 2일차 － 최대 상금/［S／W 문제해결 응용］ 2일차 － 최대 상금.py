def find_max_value(arr, change, visited):
    global max_value

    # 남은 교환 횟수가 0이면 현재 배열을 문자열로 변환하고 최대값을 갱신
    if change == 0:
        max_value = max(max_value, int("".join(arr)))
        return

    # 배열 상태와 남은 교환 횟수를 키로 사용해 이미 방문한 상태인지 확인
    state = (tuple(arr), change)
    if state in visited:
        return
    visited.add(state)

    # 현재 배열에서 두 자리씩 선택해 교환
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            # 두 자리 교환
            arr[i], arr[j] = arr[j], arr[i]
            # 재귀적으로 다음 단계 탐색
            find_max_value(arr, change - 1, visited)
            # 원래 상태로 복구
            arr[i], arr[j] = arr[j], arr[i]

T = int(input())
for test_case in range(1, T + 1):
    board, change = input().split()
    change = int(change)
    arr = list(board)
    max_value = 0

    # 방문한 상태를 기록하기 위한 집합
    visited = set()
    
    # 백트래킹 함수 호출
    find_max_value(arr, change, visited)
    
    print(f"#{test_case} {max_value}")
