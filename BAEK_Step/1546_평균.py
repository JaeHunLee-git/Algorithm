N = int(input())
arr = list(map(int, input().split()))
arr.sort()
high = arr[N - 1]
ave = 0
for i in range(N):
    ave += arr[i] / high * 100

print(ave / N)

