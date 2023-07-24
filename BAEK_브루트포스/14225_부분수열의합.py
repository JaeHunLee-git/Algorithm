## set으로 중복 제거
def dfs(str, lst, index, total):
    if index >= len(lst):
        return

    total += lst[index]
    str.append(total)

    dfs(str, lst, index+1, total-lst[index])
    dfs(str, lst, index+1, total)

def check(answer):
    for i in range(1, max(answer) + 1):
        if i not in answer:
            return i
    return max(answer)+1

n = int(input())
lst = list(map(int, input().split()))

str = []
dfs(str, lst, 0, 0)
str=set(str)

print(check(str))