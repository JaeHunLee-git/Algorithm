n = int(input())


def star(l):
    if l == 3:
        return ["***", "* *", "***"]

    arr = star(l // 3)
    stars = []

    for i in arr:
        stars.append(i * 3)

    for i in arr:
        stars.append(i + " " * (l // 3) + i)

    for i in arr:
        stars.append(i * 3)

    return stars


print("\n".join(star(n)))  # 리스트를 하나의 문자열로 바꿔줌
