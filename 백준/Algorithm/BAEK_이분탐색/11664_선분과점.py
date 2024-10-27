ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

ans = float("inf")

while True:
    mx, my, mz = (ax + bx) / 2, (ay + by) / 2, (az + bz) / 2
    l = ((ax - cx) ** 2 + (ay - cy) ** 2 + (az - cz) ** 2) ** 0.5
    h = ((mx - cx) ** 2 + (my - cy) ** 2 + (mz - cz) ** 2) ** 0.5
    r = ((bx - cx) ** 2 + (by - cy) ** 2 + (bz - cz) ** 2) ** 0.5

    if abs(ans - h) <= 1e-6:
        print("%0.10f" % ans)
        exit()
    if h < ans:
        ans = h
    if l > r:
        ax, ay, az = mx, my, mz
    else:
        bx, by, bz = mx, my, mz
