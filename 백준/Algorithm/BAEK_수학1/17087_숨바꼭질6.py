def GCD(n1, n2):
    rem = 1
    while rem != 0:
        rem = n1 % n2
        n1 = n2
        n2 = rem
    return n1


N, S = map(int, input().split())
A = list(map(int, input().split()))

new_A = []
for i in A:
    new_A.append(abs(i - S))

result = new_A[0]
for i in range(1, N):
    result = GCD(result, new_A[i])
print(result)
