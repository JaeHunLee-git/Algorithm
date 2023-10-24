a = int(input())
e = a
cnt = 1
while True:
    b = e // 10
    c = e % 10
    d = (b + c) % 10
    e = 10 * c + d
    if e == a:
        print(f"{cnt}")
        break
    cnt += 1

