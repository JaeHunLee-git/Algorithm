t = int(input())

for test in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]

    dup = 1

    for i in range(9):
        check_row = []
        check_col = []
        for j in range(9):
            if arr[i][j] in check_row:
                dup = 0
                break
            else:
                check_row.append(arr[i][j])
            if arr[j][i] in check_col:
                dup = 0
                break
            else:
                check_col.append(arr[j][i])
        if dup == 0:
            break
        if i % 3 == 0:  ## 0, 3, 6
            for q in range(3):
                check_rec = []
                for x in range(i, i + 3):
                    for y in range(q * 3, q * 3 + 3):
                        if arr[x][y] in check_rec:
                            dup = 0
                            break
                        else:
                            check_rec.append(arr[x][y])

    if dup == 1:
        print(f"#{test} {dup}")
    else:
        print(f"#{test} {dup}")
