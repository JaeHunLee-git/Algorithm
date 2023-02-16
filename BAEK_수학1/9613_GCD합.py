import sys

t = int(sys.stdin.readline())
for _ in range(t):
    ans = 0
    num_lst = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(num_lst)):
        for k in range(i + 1, len(num_lst)):
            a = min(num_lst[i], num_lst[k])
            while num_lst[i] % a != 0 or num_lst[k] % a != 0:
                a -= 1
            ans += a
    print(ans)
