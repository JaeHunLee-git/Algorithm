import sys

n= int(sys.stdin.readline())

dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
lst=[]
answer=0
pocket=[]

for _ in range(n):
    pocket.append(input())

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 **(len(alphabet)-i-1)
        dict[alphabet[i]]+=num

for value in dict.values():
    if value > 0:
        lst.append(value)

sorted_lst = sorted(lst, reverse=True)
for i in range(len(sorted_lst)):
    answer += sorted_lst[i]*(9-i)

print(answer)