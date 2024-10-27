for test_case in range(1, 11):
	N = int(input())
	building = list(map(int, input().split()))
	result = 0
	for i in range(2,N-2):
		left_best = max(building[i-1],building[i-2])
		right_best = max(building[i+1],building[i+2])
		best = max(left_best, right_best)
		if building[i]>best:
			result += building[i]-best
	print(f'#{test_case} {result}')