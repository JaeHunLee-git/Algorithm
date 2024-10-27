import sys

input = sys.stdin.readline


def check(eggs):  # 몇 개가 깨졌는지 확인
    count = 0
    for egg in eggs:
        if egg[0] <= 0:
            count += 1
    return count


def dfs(index, eggs):
    global answer

    if index == n:
        answer = max(answer, check(eggs))
        return

    if eggs[index][0] <= 0:
        # 현재 계란의 내구도가 다 달았을 때 다음 계란으로 넘어간다.
        dfs(index + 1, eggs)
    else:
        # 현재 계란의 내구도가 남아있을 때 다른 계란들과 부딪친다. (현재 계란 제외, 내구도가 없는 계란 제외)
        is_all_broken = True
        for i in range(len(eggs)):
            if index != i and eggs[i][0] > 0:
                is_all_broken = False
                eggs[index][0] -= eggs[i][1]
                eggs[i][0] -= eggs[index][1]
                dfs(index + 1, eggs)
                eggs[index][0] += eggs[i][1]
                eggs[i][0] += eggs[index][1]
        # 모든 계란이 깨져있는 경우 dfs를 바로 빠져나와준다.
        if is_all_broken:
            dfs(n, eggs)


n = int(input())
eggs = [list(map(int, input().split())) for _ in range(n)]
answer = 0

dfs(0, eggs)
print(answer)
