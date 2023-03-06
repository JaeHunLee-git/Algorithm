## 순열의 패턴을 파악해야 풀 수 있는 문제

n = int(input())
data = list(map(int, input().split()))

for i in range(n - 1, 0, -1):  # 맨 뒤 값부터 시작
    if data[i - 1] > data[i]:
        for j in range(n - 1, 0, -1):  # 다시 맨 뒤 값부터 큰 값찾기
            if data[i - 1] > data[j]:
                data[i - 1], data[j] = data[j], data[i - 1]  # 둘 값을 swap
                data = data[:i] + sorted(data[i:], reverse=True)
                for i in data:
                    print(i, end=" ")
                print()
                exit()
print(-1)
