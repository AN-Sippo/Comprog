s = input()
dic = {}
for idx, si in enumerate(s):
    dic[si] = idx

ans = 0
prev = dic["A"]
for si in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    ans += abs(prev - dic[si])
    prev = dic[si]

print(ans)
