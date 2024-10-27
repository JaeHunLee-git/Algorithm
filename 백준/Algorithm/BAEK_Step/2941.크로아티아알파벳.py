a = input()
ans = len(a)
list = ["c=", "c-", "d-", "lj", "nj", "s=", "z="]
for i in list:
    if i in a:
        ans -= a.count(i) * 1
if "dz=" in a:
    ans -= a.count("dz=") * 1
print(ans)
