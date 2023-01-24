"""
50명의 승객의 운행 시간이 5분~50분 사이의 난수로 정해진다.
5~15분 사이의 승객만 태운다고 할 때 총 탑승객 수
"""
from random import *

customer = range(1, 51)
total = 0
for i in customer:
    ride = " "
    time = randint(5, 50)
    if 5 <= time <= 15:
        ride = "O"
        total += 1

    print(f"[{ride}] {i}번째 손님 (소요시간 : {time}분)")

print(f"총 탑승 승객 : {total} 분")
