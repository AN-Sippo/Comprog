s = list(input())
t = list(input())

ans = []
for i in range(len(s)):
    if s[i] > t[i]:
        s[i] = t[i]
        ans.append("".join(s))

for i in reversed(range(len(s))):
    if s[i] < t[i]:
        s[i] = t[i]
        ans.append("".join(s))

print(len(ans))
for i in ans:
    print(i)
