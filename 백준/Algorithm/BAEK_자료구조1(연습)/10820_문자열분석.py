while True:
    try:
        s = list(input())
        ans = [0] * 4
        for i in s:
            if "a" <= i <= "z":
                ans[0] += 1
            elif "A" <= i <= "Z":
                ans[1] += 1
            elif i == " ":
                ans[3] += 1
            else:
                ans[2] += 1
        print(*ans)
    except EOFError:
        break
