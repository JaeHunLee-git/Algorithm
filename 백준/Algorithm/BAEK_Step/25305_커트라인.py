a, b = map(int, input().split())
ans = list((map(int, input().split())))
ans.sort()
print(ans[a - b])

