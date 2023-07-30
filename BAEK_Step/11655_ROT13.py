n = list(input())
ans = []
for k in range(len(n)):
    if "a" <= n[k] <= "z":
        tmp = ord(n[k]) + 13
        if tmp > 122:
            tmp -= 26
        ans.append(chr(tmp))
    elif "A" <= n[k] <= "Z":
        tmp = ord(n[k]) + 13
        if tmp > 90:
            tmp -= 26
        ans.append(chr(tmp))
    else:
        ans.append(n[k])
for i in range(len(ans)):
    print(ans[i], end="")
