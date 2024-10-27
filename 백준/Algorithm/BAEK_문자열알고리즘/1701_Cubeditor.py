def make_table(patten):
    length = len(patten)
    table = [0] * len(patten)
    j = 0
    for i in range(1, length):
        while j > 0 and patten[i] != patten[j]:
            j = table[j - 1]
        if patten[i] == patten[j]:
            j += 1
            table[i] = j
    return max(table)


s = input()
result = 0

for idx in range(len(s)):
    sub_str = s[idx : len(s)]
    result = max(result, make_table(sub_str))

print(result)
