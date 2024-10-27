T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = 0
    for i in range(10):
        if (arr[i]%2) != 0:
	        ans+=arr[i]
    print(f"#{test_case} {ans}")