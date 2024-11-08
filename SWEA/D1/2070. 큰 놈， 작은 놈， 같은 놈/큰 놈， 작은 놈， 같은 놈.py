t = int(input())

for test in range(1, t + 1):
    a, b = map(int, input().split())
    ans = ""
    if a > b:
        ans = '>'
    elif a < b:
        ans = '<'
    else:
        ans = '='

    print(f"#{test} {ans}")
