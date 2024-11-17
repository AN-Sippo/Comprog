s = input()
q = int(input())
klst = list(map(int, input().split()))
n = len(s)
clst = []

for ki in klst:
    ki = ki - 1
    bi_ki = bin((ki) // n)
    bi_ki = bi_ki[2:]
    flip = 0
    for i in bi_ki:
        if i == "1":
            flip += 1

    if flip % 2 == 0:
        clst.append(s[ki % n])
    else:
        clst.append(s[ki % n].swapcase())
    # print(f"{ki}->{ki // n }周目->bi:{bi_ki} -> flip:{flip}")
print(*clst)
