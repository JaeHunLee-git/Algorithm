n = int(input())
word = input()
lst = list(map(int, input().split()))
stack = []

for i in word:
    if "A" <= i <= "Z":
        stack.append(lst[ord(i) - ord("A")])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == "+":
            stack.append(str1 + str2)
        elif i == "-":
            stack.append(str1 - str2)
        elif i == "*":
            stack.append(str1 * str2)
        elif i == "/":
            stack.append(str1 / str2)

print("%.2f" % stack[0])

