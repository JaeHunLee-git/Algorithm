import sys

input = sys.stdin.readline
arr = [list(map(str, input().split())) for _ in range(20)]
sum_point = 0
sum_lecture = 0
grade_to_point = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
    "P": 0.0,
}

for i in range(20):
    tmp = arr[i][2]
    sum_point += float(arr[i][1]) * grade_to_point.get(tmp)
    if tmp != "P":
        sum_lecture += float(arr[i][1])

print(sum_point / sum_lecture)
