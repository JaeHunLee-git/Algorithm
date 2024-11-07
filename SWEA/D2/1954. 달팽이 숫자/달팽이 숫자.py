# T = int(input())
# for test_case in range(1, T + 1):
#     n = int(input())
#
#     arr = [[0] * n for _ in range(n)]
#     x, y = 0, 0
#     i = 1
#     arr[0][0] = 1
#     ## 위와 같이 현재 방향을 1,2,3,4로 표시
#     direct = 1
#     while i < n * n + 1:
#         if direct == 1:
#             while arr[x][y] == 0:
#                 i += 1
#                 y += 1
#                 if y >= n:
#                     y -= 1
#                     i -= 1
#                     break
#                 arr[x][y] = i
#         elif direct == 2:
#             while arr[x][y] == 0:
#                 i += 1
#                 x += 1
#                 if x >= n:
#                     i -= 1
#                     x -= 1
#                     break
#                 arr[x][y] = i
#         elif direct == 3:
#             while arr[x][y] == 0:
#                 i += 1
#                 y -= 1
#                 if y < 0:
#                     i -= 1
#                     y += 1
#                     break
#                 arr[x][y] = i
#         else:
#             while arr[x][y] == 0:
#                 i += 1
#                 x -= 1
#                 if x < 0:
#                     i -= 1
#                     x += 1
#                     break
#                 arr[x][y] = i
#         print(1)
#         if direct < 4:
#             direct += 1
#         else:
#             direct = 1
#     print(f"#{test_case}")
#     for q in arr:
#         print("".join(map(str, q)))

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    arr = [[0] * n for _ in range(n)]
    x, y = 0, 0
    i = 1
    arr[0][0] = 1
    ## 위와 같이 현재 방향을 1,2,3,4로 표시
    direct = 1
    while i < n * n:
        if direct == 1:  # 오른쪽
            while y + 1 < n and arr[x][y + 1] == 0:
                y += 1
                i += 1
                arr[x][y] = i
            direct = 2  # 방향 전환
        elif direct == 2:  # 아래쪽
            while x + 1 < n and arr[x + 1][y] == 0:
                x += 1
                i += 1
                arr[x][y] = i
            direct = 3  # 방향 전환
        elif direct == 3:  # 왼쪽
            while y - 1 >= 0 and arr[x][y - 1] == 0:
                y -= 1
                i += 1
                arr[x][y] = i
            direct = 4  # 방향 전환
        elif direct == 4:  # 위쪽
            while x - 1 >= 0 and arr[x - 1][y] == 0:
                x -= 1
                i += 1
                arr[x][y] = i
            direct = 1  # 방향 전환
    print(f"#{test_case}")
    for q in arr:
        print(" ".join(map(str, q)))
