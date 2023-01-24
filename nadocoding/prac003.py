"""
치킨집
"""


class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1
while True:
    try:
        print("[남은 치킨 : {0}".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order < 1 or order == str:
            raise ValueError
        if order > chicken:
            print("재료가 부족합니다.")
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order
            if chicken == 0:
                raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break

