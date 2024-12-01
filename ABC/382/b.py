n, d = map(int, input().split())
s = input()
ans = []
cnt = 0
s = reversed(s)
for si in s:
    if si == ".":
        ans.append(".")
    elif si == "@" and cnt < d:
        cnt += 1
        ans.append(".")
    else:
        ans.append("@")

print("".join(reversed(ans)))
