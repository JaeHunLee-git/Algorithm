t = int(input())

for test in range(1, t + 1):
    arr = list(map(int, input().split()))
    ans = max(arr)
    print(f"#{test} {ans}")
