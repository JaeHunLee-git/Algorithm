## 한 번 할 때마다 소수를 찾는 것이 아닌 한 번에 소수를 다 찾아 놓기

import sys


def Goldbach():
    check = [False, False] + [True] * 1000000

    for i in range(2, 1001):
        if check[i] == True:
            for j in range(i + i, 1000001, i):
                check[j] = False

    while True:
        n = int(sys.stdin.readline())

        if n == 0:
            break

        A = 0
        B = n
        for _ in range(1000000):
            if check[A] and check[B]:
                print(f"{n} = {A} + {B}")
                break
            A += 1
            B -= 1
        else:
            print("Goldbach's conjecture is wrong.")


Goldbach()
