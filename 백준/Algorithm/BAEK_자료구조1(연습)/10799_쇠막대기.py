lst = list(input())
answer = 0
st = []

for i in range(len(lst)):
    if lst[i] == "(":
        st.append("(")

    else:
        if lst[i - 1] == "(":
            st.pop()
            answer += len(st)

        else:
            st.pop()
            answer += 1

print(answer)
