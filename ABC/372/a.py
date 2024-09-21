s = input()
ans = [""]
for si in s:
    if si == ".":
        continue
    else:
        ans.append(si)

print("".join(ans))
