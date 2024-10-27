a, b = map(int, input().split())
m = int(input())
lst = list(map(int, input().split()))
sum = 0
for i in range(m):
    sum += lst[i] * pow(a, m - 1)
    m -= 1

ans = []
while sum > 0:
    ans.append(str(sum % b))
    sum //= b
ans.reverse()
print(*ans)
