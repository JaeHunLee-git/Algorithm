from random import *
from math import gcd


def is_prime(n):  # n이 소수인지 확인하는 함수
    for i in range(2, int(n ** (0.5)) + 1):
        # 2부터 n의 제곱근까지의 수로 나누어지는지 확인
        if n % i == 0:
            return 1
    return 0


def extended_euclid_algorithm(a, b):
    # 확장 유클리드 알고리즘을 이용하여 a와 b의 최대공약수(d)와
    # ax + by = d를 만족하는 계수 x와 y를 반환하는 함수
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = extended_euclid_algorithm(b, a % b)
        return d, y, x - y * (a // b)


def find_s(n, phi):
    # n과 phi의 확장 유클리드 알고리즘을 사용하여 n의 phi에 대한 모듈러 역수를 찾고
    # 계산된 d 값을 전역 변수에 할당하고 s를 phi로 나눈 나머지를 반환하는 함수
    global d
    d, s, _ = extended_euclid_algorithm(n, phi)
    return s % phi


def encryption(a, n):
    # 평문 메시지 a의 n으로 암호화 하는 함수
    # 제곱-곱 알고리즘을 사용하여 x의 n 제곱을 반복적으로 계산하고
    # 홀수인 경우 결과에 x를 곱한 후 z로 모듈러 연산을 수행
    result = 1
    x = a % z
    while n > 0:
        if n % 2 == 1:
            result = result * x % z
        x = x * x % z
        n //= 2
    print(f"암호화 : {result}")
    return result


def decrypotion(c, s):
    # 암호문 c를 s로 복호화 하는 함수
    # c를 z로 모듈러 연산한 값을 x에 저장하고
    # 제곱-곱 알고리즘을 사용하여 x의 s 제곱을 반복적으로 계산
    # 홀수인 경우 결과에 x를 곱하고, z로 모듈러 연산을 수행
    result = 1
    x = c % z
    while s > 0:
        if s % 2 == 1:
            result = result * x % z
        x = x * x % z
        s //= 2
    print(f"복호화 : {result}")


while True:
    # 100 이하의 소수 p를 랜덤하게 생성하는 while문, 소수가 정해지면 break
    p = randrange(2, 100)
    if is_prime(p) == 0:
        break

while True:
    # 100 이하의 소수 q를 랜덤하게 생성하는 while문, 소수가 정해지면 break
    q = randrange(2, 100)
    if is_prime(q) == 0:
        break

z = p * q
phi = (p - 1) * (q - 1)
n = 2
while True:
    # n은 2부터 시작해서 gcd(n,phi)=1 이 되는 n이 될 때까지 +1을 하며 n을 구함
    if gcd(n, phi) == 1:
        break
    n += 1
while True:
    s = find_s(n, phi)
    if d == 1:
        break
print(f"공개키 : {z}, {n}")
print(f"개인키 : {s}")
c = encryption(5, n)  # 임의의 평문 메시지 5의 계산된 암호문을 c에 저장
decrypotion(c, s)  # c를 a로 다시 복호화

