for test in range(1, 11):
    dum = int(input())

    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    for i in range(dum):
        arr[0] -= 1
        arr[-1] += 1
        arr.sort(reverse=True)

    print(f"#{test} {arr[0] - arr[-1]}")
