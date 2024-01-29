import sys

input = sys.stdin.readline
dx = [0, 0, 1, -1, 1, 1, -1, -1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
while True:
    r, c = map(int, input().split())

    if r == 0 and c == 0:
        exit(0)

    arr = [input().strip() for _ in range(r)]
    ans = []

    for i in range(r):
        for j in range(c):
            tmp = 0
            for k in range(8):
                tmp_i = i + dx[k]
                tmp_j = j + dy[k]
                if 0 <= tmp_i < r and 0 <= tmp_j < c:
                    if arr[tmp_i][tmp_j] == "*":
                        tmp += 1
            if arr[i][j] == "*":
                ans.append("*")
            else:
                ans.append(tmp)
    final_ans = []
    tmp_cnt = 0
    for i in range(r):
        tmp = ""
        for j in range(c):
            tmp += str(ans[tmp_cnt])
            tmp_cnt += 1
        final_ans.append(tmp)
    for i in final_ans:
        print(i)
