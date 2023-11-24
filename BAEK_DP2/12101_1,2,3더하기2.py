import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
answers = set()


def DFS(value, answer):
    if value == n:
        answers.add(tuple(answer))  ## 튜플,set 같은 불변자료형에는 list같은 가변 자료형 삽입 불가
        return

    if value + 1 <= n:
        DFS(value + 1, answer + [1])

    if value + 2 <= n:
        DFS(value + 2, answer + [2])

    if value + 3 <= n:
        DFS(value + 3, answer + [3])


DFS(0, [])

if len(answers) < k:
    print(-1)
else:
    answers = list(answers)
    answers.sort()
    answer = answers[k - 1]
    print(*answer, sep="+")
