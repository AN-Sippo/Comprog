n, d = map(int, input().split())
s = input()
cookies = 0
box = 0
for si in s:
    if si == "@":
        cookies += 1
    else:
        box += 1

print(box + d)
