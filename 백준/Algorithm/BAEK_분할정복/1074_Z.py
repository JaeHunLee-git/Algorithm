# import sys

# input = sys.stdin.readline
# n, r, c = map(int, input().split())


# maxi = 2**n
# visited = [[0] * (maxi) for _ in range(maxi)]

# tmp = 2 ** (n - 1)
# cnt = 0

# for i in range(tmp):
#     for j in range(tmp):
#         visited[i][j] = cnt
#         cnt += 1

# for i in range(tmp):
#     for j in range(tmp, 2 * tmp):
#         visited[i][j] = cnt
#         cnt += 1

# for i in range(tmp, 2 * tmp):
#     for j in range(tmp):
#         visited[i][j] = cnt
#         cnt += 1

# for i in range(tmp, 2 * tmp):
#     for j in range(tmp, 2 * tmp):
#         visited[i][j] = cnt
#         cnt += 1

# print(visited[r][c])
N, r, c = map(int, input().split())

ans = 0

while N != 0:
    N -= 1

    # 1사분면
    if r < 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0

    # 2사분면
    elif r < 2**N and c >= 2**N:
        ans += (2**N) * (2**N) * 1
        c -= 2**N

    # 3사분면
    elif r >= 2**N and c < 2**N:
        ans += (2**N) * (2**N) * 2
        r -= 2**N

    # 4사분면
    else:
        ans += (2**N) * (2**N) * 3
        r -= 2**N
        c -= 2**N

print(ans)
