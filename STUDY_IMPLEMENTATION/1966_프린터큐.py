import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    result = 1
    while data:
        if data[0] < max(data):  ## 우선순위가 가장 높은 데이터가 아닐 때
            tmp = data.pop(0)
            data.append(tmp)  ## 맨 뒤로 보냄

        else:  ## 우선 순위가 가장 높은 데이터일 때
            if m == 0:  ## 내가 찾는 순서일 경우
                break

            data.pop(0)  ## 내가 찾는 순서가 아닐 경우 맨 앞을 뺌
            result += 1  ## 처리순서에 1을 더함
        if m > 0:
            m -= 1
        else:  ## m이 0이지만 중요한 문서가 있으면 맨 뒤로 이동, 찾는 것의 인덱스를 따라가는거임
            m = len(data) - 1

    print(result)
# 배열 3개를 사용한 코드
# import sys

# T= int(sys.stdin.readline())

# for _ in range(T):
#     N,M = map(int,sys.stdin.readline().split())
#     imp = list(map(int,sys.stdin.readline().split()))
#     new = sorted(imp,reverse=True)
#     ans = [-1 for i in range(N)]
#     index_i = 0
#     index_n = 0
#     rank = 1
#     while index_n < N:
#         index_i%=N
#         if imp[index_i]==new[index_n] :
#             ans[index_i] = rank
#             index_i+=1
#             index_n+=1
#             rank+=1
#         else : index_i+=1

#     print(ans[M])
