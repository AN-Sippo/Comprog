n = int(input())
A = []
S = []
for i in range(n):
    ai, si = input().split()
    A.append(int(ai))
    S.append(si)

l = -1
r = -1
ans = 0
for i in range(n):
    ai = A[i]
    si = S[i]
    if si == "L":
        if l == -1:
            l = ai
            continue
        else:
            ans += abs(l - ai)
            l = ai
    if si == "R":
        if r == -1:
            r = ai
            continue
        else:
            ans += abs(r - ai)
            r = ai
print(ans)
