import sys

input = sys.stdin.readline


def sol(x, y, width):
    h1 = (x**2 - width**2) ** 0.5
    h2 = (y**2 - width**2) ** 0.5
    c = h1 * h2 / (h1 + h2)
    return c


x, y, c = map(float, input().split())
start, end = 0, min(x, y)

while (end - start)>0.000001:
    width = (start + end) / 2
    if sol(x, y, width) >= c:
        start = width
    else:
        end = width
print(round(end,3))
