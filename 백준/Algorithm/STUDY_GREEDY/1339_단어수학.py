## 성공
## 위치를 기준으로 알파벳에 인덱스를 넣어놓음
## 예를들어 ABC이면 A=3 B=2 C=1,   DE면 D=2 E=1
# 2
# ADEBC
# GCF
# 98754
# 643
# 98745
# 653
## 처음엔 위의 테스트케이스에서 BC에 대해서도 우선순위를 정해줘야하는 것을 고려 못했음
## 10 ** (tmp - 1) 처럼 각 자리 수의 합으로 우선순위를 줌
import sys

input = sys.stdin.readline
n = int(input())
arr = [input().strip() for _ in range(n)]

## 길이가 긴 순으로 정렬
arr = sorted(arr, key=lambda a: len(a), reverse=True)

# 각 단어마다 숫자를 집어 넣은 후에 계산
num_dict = dict()

for i in arr:
    tmp = len(i)
    for k in range(len(i)):
        if i[k] not in num_dict or num_dict[i[k]] is None:  ## 키가 존재하지 않거나 값이 None인 경우
            num_dict[i[k]] = 10 ** (tmp - 1)
        else:
            num_dict[i[k]] += 10 ** (tmp - 1)
        tmp -= 1

num_dict = dict(sorted(num_dict.items(), key=lambda a: a[1], reverse=True))
## 딕셔너리 정렬법 구글링 함  ##

## for문으로 딕셔너리에 9부터 숫자 넣어주기
tmp = 9
for i in num_dict:
    num_dict[i] = tmp
    tmp -= 1

ans_arr = []
for i in arr:
    tmp = ""
    for k in i:
        tmp += str(num_dict[k])
    ans_arr.append(int(tmp))

print(sum(ans_arr))
