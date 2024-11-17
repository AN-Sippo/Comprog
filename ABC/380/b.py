s = input().split("|")
alst = []
for si in s[1 : len(s) - 1]:
    alst.append(len(si))
print(*alst)
