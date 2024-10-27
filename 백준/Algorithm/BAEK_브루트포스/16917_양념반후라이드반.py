import sys

input = sys.stdin.readline
a, b, c, x, y = map(int, input().split())

if c * 2 < a and c * 2 < b:
    tmp = max(x, y)
    print(c * 2 * tmp)
    exit(0)

if c * 2 > a + b:
    print(a * x + b * y)
else:
    tmp = min(x, y)
    ans = c * 2 * tmp

    if x > y:
        if c * 2 > a:
            ans += a * (x - y)
        else:
            ans += c * 2 * (x - y)
    else:
        if c * 2 > b:
            ans += b * (y - x)
        else:
            ans += c * 2 * (y - x)
    print(ans)
